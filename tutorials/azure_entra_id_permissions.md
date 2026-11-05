Set Up Permissions for Microsoft Entra ID Authentication to Azure Blob Storage
====

> Assign the Azure roles a user needs to connect to Azure Blob Storage with the *Azure (Microsoft Entra ID)* connection profile.

:::{admonition} Requirements
:class: warning
* Cyberduck [9.6.0](https://cyberduck.io/changelog/) or later required
* You must be allowed to create role assignments on the storage account, for example with the *Owner* or *User Access Administrator* role. Creating the custom role in [step 1](#step-1-create-the-custom-role) requires the same permission on the subscription.
:::

Refer to [Azure Blob Storage](../protocols/azure.md#microsoft-entra-id) for how to connect.

## Required Permissions

A user needs the following two permissions on the storage account:

| Permission | Granted by | Used for |
|---|---|---|
| Read, write and delete containers and blobs | A data role such as [*Storage Blob Data Reader*](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-reader) (read only), [*Storage Blob Data Contributor*](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor) or *Storage Blob Data Owner* | Browsing and transferring files |
| `Microsoft.Storage/storageAccounts/blobServices/getInfo/action` | The custom role created below, or the *Owner* role | [Get Account Information](https://learn.microsoft.com/en-us/rest/api/storageservices/get-account-information), which Cyberduck uses to detect whether the account has a hierarchical namespace enabled |

None of the data roles includes the action `getInfo/action`, which is why it is granted with a separate custom role containing only that action.

:::{warning}
Avoid assigning *Storage Account Contributor* only to obtain this permission. It includes `Microsoft.Storage/storageAccounts/*`, which allows to create and delete storage accounts, change their configuration and to list and regenerate the account keys.
:::

## Step 1: Create the Custom Role

Create the role once per subscription. It contains the single action `Microsoft.Storage/storageAccounts/blobServices/getInfo/action`.

Replace `<subscription-id>` with the ID of the subscription containing the storage account.

::::{tabs}
:::{group-tab} Azure CLI

1. Sign in and select the subscription.

   ```
   az login
   az account set --subscription <subscription-id>
   ```

2. Save the role definition as `storage-account-info-reader.json`.

   ```json
   {
     "Name": "Storage Account Information Reader",
     "Description": "Allows to read the account information of a storage account such as whether a hierarchical namespace is enabled.",
     "Actions": [
       "Microsoft.Storage/storageAccounts/blobServices/getInfo/action"
     ],
     "NotActions": [],
     "DataActions": [],
     "NotDataActions": [],
     "AssignableScopes": [
       "/subscriptions/<subscription-id>"
     ]
   }
   ```

3. Create the role.

   ```
   az role definition create --role-definition @storage-account-info-reader.json
   ```

:::
:::{group-tab} Azure portal

1. Save the role definition as `storage-account-info-reader.json`.

   ```json
   {
     "properties": {
       "roleName": "Storage Account Information Reader",
       "description": "Allows to read the account information of a storage account such as whether a hierarchical namespace is enabled.",
       "assignableScopes": [
         "/subscriptions/<subscription-id>"
       ],
       "permissions": [
         {
           "actions": [
             "Microsoft.Storage/storageAccounts/blobServices/getInfo/action"
           ],
           "notActions": [],
           "dataActions": [],
           "notDataActions": []
         }
       ]
     }
   }
   ```

2. Open the subscription in the [Azure portal](https://portal.azure.com/) and choose *Access control (IAM)*.
3. Choose *Add → Add custom role*.
4. For *Baseline permissions* choose *Start from JSON* and select the file `storage-account-info-reader.json`.
5. Choose *Review + create* and then *Create*.

:::
::::

## Step 2: Assign the Roles

Assign both the data role and the custom role to the user or group on the storage account. Assigning a role to a group avoids repeating the steps for every user.

::::{tabs}
:::{group-tab} Azure CLI

1. Look up the resource ID of the storage account.

   ```
   az storage account show --name <account> --query id --output tsv
   ```

2. Assign the data role. Replace `<assignee>` with the user principal name (such as `user@example.com`), or with the object ID of a user or group, and `<scope>` with the resource ID from the previous step.

   ```
   az role assignment create --assignee <assignee> --role "Storage Blob Data Contributor" --scope <scope>
   ```

   Use `Storage Blob Data Reader` instead for read-only access.

3. Assign the custom role created in step 1.

   ```
   az role assignment create --assignee <assignee> --role "Storage Account Information Reader" --scope <scope>
   ```

:::
:::{group-tab} Azure portal

1. Open the storage account in the [Azure portal](https://portal.azure.com/) and choose *Access control (IAM)*.
2. Choose *Add → Add role assignment*.
3. In *Role*, select *Storage Blob Data Contributor* (or *Storage Blob Data Reader* for read-only access) and choose *Next*.
4. In *Members*, choose *Select members*, pick the user or group and choose *Select*, then *Review + assign*.
5. Repeat the steps to assign the custom role *Storage Account Information Reader*, which is listed in the *Job function roles* tab.

:::
::::

:::{note}
It can take several minutes until a new role assignment takes effect. If the user is already signed in with Cyberduck, disconnect and connect again to use a new access token.
:::

## Step 3: Verify the Assignments

::::{tabs}
:::{group-tab} Azure CLI

List the assignments of the user on the storage account, including those inherited from the subscription or a group.

```
az role assignment list --assignee <assignee> --scope <scope> --include-inherited --include-groups --output table
```

The output must list the data role and *Storage Account Information Reader*. Test that the data role works by listing the containers.

```
az storage container list --account-name <account> --auth-mode login
```

:::
:::{group-tab} Azure portal

In the storage account choose *Access control (IAM) → Check access*, select the user and verify that both roles are listed under *Role assignments*. Roles inherited from the subscription or a resource group are listed with their scope.

:::
::::

Connect with the *Azure (Microsoft Entra ID)* connection profile in Cyberduck to confirm.

## Troubleshooting

### AuthorizationPermissionMismatch for `/?restype=account&comp=properties`

The user is authenticated but lacks the action `Microsoft.Storage/storageAccounts/blobServices/getInfo/action`. Assign the custom role from [Step 2](#step-2-assign-the-roles). Listing containers might still work because the data role is assigned.

### AuthorizationPermissionMismatch when opening a container

The user lacks a data role for the container or the role assignment has a condition excluding it. Check the assignments as described in [Step 3](#step-3-verify-the-assignments) and whether an [attribute-based access control (ABAC) condition](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-overview) is set on the assignment. The roles *Owner* and *Contributor* do not grant access to blob data.

### Hierarchical namespace (Azure Data Lake Storage)

Accounts with a hierarchical namespace additionally evaluate [POSIX-like access control lists (ACLs)](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-access-control) when no data role grants access. Assign a data role to avoid maintaining ACLs.
