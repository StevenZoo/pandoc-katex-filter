# pandoc-katex-filter

This project lets you pre-render [KaTeX](https://katex.org/) markup into HTML with Pandoc. 

## Requirements
- [Pandoc](https://pandoc.org/)
- [Node.js](https://nodejs.org/en/)

Please make sure you have Pandoc and Node.js already installed.

## Installation

```
npm install -g pandoc-katex-filter
```

## Invocation

### MacOS/Linux
```
pandoc --filter pandoc-katex-filter
```

### Windows
```
pandoc --filter pandoc-katex-filter.cmd
```
📌 The `.cmd` suffix is **required** on Windows. Otherwise, Pandoc won't find the filter. Please don't forget! 

The examples below will use the MacOS/Linux syntax.

## Example Usage

```
# Pipe TeX input
echo '$a+b$' | pandoc --filter pandoc-katex-filter

# Process input file
pandoc -i samples/hello.md --filter pandoc-katex-filter

# Create standalone HTML file
pandoc -i samples/hello.md -o samples/output/hello.html -H samples/styles/styles.html --filter pandoc-katex-filter
```

## Error Handling

**Throw now...**

If KaTeX can't render an expression to HTML, it will throw an error. By default, this filter will propagate that error immediately.

**Or handle later...**

Alternatively, to continue processing the rest of the document, add the `katex-batch-errors` metadata flag to direct the error message to the standard error stream. This can be useful if you want to see all errors at once.

When using this flag, you can still produce an output HTML file. Any TeX that causes errors will be highlighted in red.

```
# Throws Error
pandoc -i samples/hello-error.md --filter pandoc-katex-filter

# Direct errors to standard error
pandoc -i samples/hello-error.md --filter pandoc-katex-filter -Mkatex-batch-errors

# Further redirect errors into a file for easier viewing
pandoc -i samples/hello-error.md --filter pandoc-katex-filter -Mkatex-batch-errors 2> errors.txt

# Generate HTML file, even with errors from source.
pandoc -i samples/hello-error.md -o samples/output/hello-error.html -H samples/styles/styles.html --filter pandoc-katex-filter -Mkatex-batch-errors
```

## Use Cases
- Pre-rendering the math on a site built with a static site generator. (My case with [Hugo](https://gohugo.io/).)

## How does this work?
Pandoc is a software capable of converting documents from one format to another. With filters, we can add custom logic to extend the functionality of Pandoc.

To render KaTeX markup, we take the TeX content found by Pandoc, and use the KaTeX library to render TeX into HTML.

## License

`pandoc-katex-filter` is released under the [MIT License](LICENSE).

## Related Links
Thanks to the people in these links for their open contributions.
1) [pandoc-static-katex](https://github.com/Zaharid/pandoc_static_katex) - Python filter
2) [Server-side rendering discussion](https://github.com/jgm/pandoc/issues/6651)
