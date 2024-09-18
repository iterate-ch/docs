# Documentation source for [Cyberduck](https://cyberduck.io), [Cyberduck CLI](https://duck.sh) & [Mountain Duck](https://mountainduck.io)

[![CI](https://github.com/iterate-ch/docs/actions/workflows/CI.yml/badge.svg)](https://github.com/iterate-ch/docs/actions/workflows/CI.yml)

Libre file transfer client for macOS and Windows. Command line interface (CLI) for Linux, macOS and Windows.

## Prerequisites

- Python
- make
- `pip install sphinx`
- `pip install -r requirements.txt`


## Building

Build the documentation by running

```
make html
```

Output can be found in `_build/html`.

## Contributions

Contributions to this documentation are welcome. Please open a pull request.

---

## General Formatting Guidelines

Add an empty line...
- ...after a heading
- ...before and after an admonition or codeblock
- ...after the admonition class for custom admonitions
- ...after a tab opening and before a tab closing as shown in the [Tabs Section](#tabs)
- ...before and after tables
- ...before and after image inserts with custom properties

Indent codeblocks and admonitions within numbered lists, as the numbers aren't rendered correctly otherwise.

### Footnotes

- This is a manually-numbered footnote reference.[^3]
- This is an auto-numbered footnote reference.[^myref]

[^myref]: This is an auto-numbered footnote definition.
[^3]: This is a manually-numbered footnote definition.

A longer footnote definition.[^mylongdef]

[^mylongdef]: This is the _**footnote definition**_.

    That continues for all indented lines

    - even other block elements

    Plus any preceding unindented lines,
that are not separated by a blank line

### Tabs
Group tabs allow to select a tab for the whole page. As an example: If a page contains three group tabs with macOS and Windows as options and you select macOS for one section then all the sections on the page will switch to macOS.

```
::::{tabs}
:::{group-tab} macOS

text

:::
:::{group-tab} Windows

text

:::
::::
```

Regular tabs are limited to the section and doesn't affect any other tabs on the page.

```
::::{tabs}
:::{tab} Text 1

text

:::
:::{tab} Text 2

text

:::
```

### Quotes and Code

````
```
This is a codeblock
```
````

`this is in line code`

```
> this is a single line Quote
```

### Links und Downloadlinks
Add those inline into the text where needed.

```
[Formatting Cheat Sheet](Formatting_Cheat-Sheet)
```

```
{download}`Title<Download_Link>`
```

### Admonitions
Admonitions are boxes with a colored background that highlight information. Available admonition types are: note, warning, tip, caution, attention, danger, error, hint, important, and seealso

```
:::{<type>}
text
:::
```

Admonitions can also be used with custom titles by using the format below.

```
:::{admonition} Custom Title
:class: tip

text
:::
```