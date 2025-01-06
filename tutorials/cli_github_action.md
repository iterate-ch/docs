Use Cyberduck CLI GitHub Action
===

Use Cyberduck CLI in a [GitHub Actions](https://docs.github.com/en/actions) workflow conveniently in a docker container.

## Usage in Custom Workflow

1. Add the `cyberduck-cli-action` action to a workflow `.yml` with a step like 

   ```
    - name: Upload
      uses: iterate-ch/cyberduck-cli-action@v1
      env:
          USERNAME: ${{secrets.S3_ACCESS_KEY}}
          PASSWORD: ${{secrets.S3_SECRET_KEY}}
      with:
          mode: upload
          url: 's3:/bucket/path/'
          path: 'release/*'
          args: '--verbose'
   ```    

2. Choose a `mode`. Several modes are supported like `download`, `list` and `upload` probably the most common usage. If you want to any of the supported command line parameters use `raw` and omit the `path` and `url` options. 

3. Set the `url` input option to a valid URI that references the protocol, optional server and destination upload file or directory as [documented](https://docs.duck.sh/cli/#uri). For [S3](https://docs.duck.sh/protocols/s3/) this would be `s3:/<bucket>/<key>` or for [SFTP](https://docs.duck.sh/protocols/sftp/) `sftp://<server>/<directory>/`. 

    :::{attention}
    Make sure to include a trailing `/` in `url` input to denote a directory.
    :::

4. Specify credentials in the environment with `USERNAME`, `PASSWORD`. Additionally `IDENTITY` can be used for SFTP connections equivalent to the `--identity` parameter. The example assumes you have `S3_ACCESS_KEY` and `S3_SECRET_KEY` defined as a [secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions). Alternatively specify `--username ${{secrets.USER}} --password ${{secrets.PASSWORD}}` in `args`.

5. Add additional arguments for Cyberduck CLI. Any of the available [generic options](https://docs.duck.sh/cli/#generic-options) can be passed with the `args` input.

    :::{tip}
    Only overwrite existing files on changes using  `args: '--existing compare'`.
    :::

6. Read output in a next step using the key `log` using `jobs.<job_id>.outputs.log` [output](https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions#outputsoutput_id).

## References 

* Cyberduck CLI GitHub Action [README](https://github.com/iterate-ch/cyberduck-cli-action/blob/main/README.md)