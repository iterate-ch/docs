Formatting Cheat Sheet
====

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

````{tabs}

```{group-tab} macOS

test
```

```{group-tab} Windows

test
```

````

---

## Quotes and Codeblocks

	This is a codeblock

`this is code`

> this is a single line Quote

## Links und Downloadlinks

[Formatting Cheat Sheet](Formatting_Cheat-Sheet)

```
{download}`Titel<Download_Link>`
```

---

## Admonitions

```{note}
Here is a note!
```

```{warning}
Here is a warning!
```

```{tip}
Here is a tip!
```

```{caution}
Caution!
```

```{attention}
Attention!
```

```{danger}
Here is a danger!
```

```{error}
Here is an error!
```

```{hint}
Here is a hint!
```

```{important}
This is important!
```

```{seealso}
See also here!
```

```{admonition} Custom
:class: tip
Custom content
```