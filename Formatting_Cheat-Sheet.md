---
orphan: true
---

Formatting Cheat Sheet
====

## General Formatting Guidelines

Add an empty line...
- ...after a heading
- ...before and after an admonition or codeblock
- ...after the admonition class for custom admonitions
- ...after a tab opening and before a tab closing as shown in the [Tabs Section](#tabs)
- ...before and after tables
- ...before and after image inserts with custom properties

Don't add an empty line around admonitions within lists

Indent codeblocks within numbered lists, as the numbers aren't rendered correctly otherwise.

## Footnotes

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

---

## Tabs

::::{tabs}
:::{group-tab} macOS

test

:::
:::{group-tab} Windows

test

:::
::::

---

## Quotes and Codeblocks

	This is a codeblock

`this is code`

> this is a single line Quote

## Links und Downloadlinks

[Formatting Cheat Sheet](Formatting_Cheat-Sheet)

```
{download}`Title<Download_Link>`
```

---

## Admonitions

:::{note}
Here is a note!
:::

:::{warning}
Here is a warning!
:::

:::{tip}
Here is a tip!
:::

:::{caution}
Caution!
:::

:::{attention}
Attention!
:::

:::{danger}
Here is a danger!
:::

:::{error}
Here is an error!
:::

:::{hint}
Here is a hint!
:::

:::{important}
This is important!
:::

:::{seealso}
See also here!
:::

:::{admonition} Custom
:class: tip
Custom content
:::