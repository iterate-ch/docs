Spotlight (macOS)
===

# Search bookmarks with Spotlight

Cyberduck includes a custom *Spotlight Importer Plugin* to search the contents of its bookmarks files.

# Using the Spotlight Menu

```{note}
The *Spotlight Menu* does return no results for recently connected servers in Cyberduck because it excludes indexed files located in `~/Library/Application Support/Cyberduck/History`. This is also an issue for Adium.
```

As a workaround, you have to export all bookmarks to another location such as your *Documents* folder. Select all bookmarks *(⌘A)* in the bookmark list and drag these somewhere in your *Documents* folder in the Finder. You can then search bookmarks in the *Spotlight Menu* by nickname and hostname. Additionally, to display all bookmarks as a result search for `kind:"Cyberduck Bookmark"`.

# Create a Smart Folder in Finder to Search Bookmark Files

Using custom search criteria, you can create a smart folder in *Finder.app* to display all recently connected servers and other bookmarks you have manually exported from Cyberduck.

Follow these steps:

- Choose *File → Find* in the *Finder*.
- Select *Contents* as a search criteria matching the text `kind: "Cyberduck Bookmark"`.
- Add another criteria using the `+` button.
- Select to include system files in the custom search by choosing *Other...* in the criteria drop-down menu.

```{image} _images/system_files_criteria.png
:alt: Send Command
:width: 600px
```

- Choose *System files* as search criteria and choose *are included* as the value.

When configured, the saved search looks the following:

```{image} _images/Cyberduck_saved_search.png
:alt: Send Command
:width: 800px
```