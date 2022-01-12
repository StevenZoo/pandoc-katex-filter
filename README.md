# pandoc-katex-filter

This project sets up an environment to pre-render [KaTeX](https://katex.org/) markup into HTML with Pandoc. 

## Requirements
- [Pandoc](https://pandoc.org/)
- [Node.js](https://nodejs.org/en/)

Please make sure you have Pandoc and Node.js already installed.

## Installation

Run these commands to install the necessary dependencies.

```
npm install
```

## Example Usage

```
# Pipe TeX input
echo '$a+b$' | pandoc -F src/katex-filter.js

# Process input file
pandoc -i samples/hello.md -F src/katex-filter.js

# Create standalone HTML file
pandoc -i samples/hello.md -o samples/output/hello.html -H samples/styles/styles.html -F src/katex-filter.js
```

## Error Handling

If KaTeX can't render an expression to HTML, it will throw an error. By default, this filter will propagate that error immediately.

Alternatively, to continue processing the rest of the document, add the `batch-katex-error` metadata flag to direct the error message to the standard error stream. This can be useful if you want to see all errors at once.

When using this flag, you can still produce an output HTML file. Any TeX that causes errors will be highlighted in red.

```
# Throws Error
pandoc -i samples/hello-error.md -F src/katex-filter.js

# Direct errors to standard error
pandoc -i samples/hello-error.md -F src/katex-filter.js -Mbatch-katex-errors

# Further redirect errors into a file for easier viewing
pandoc -i samples/hello-error.md -F src/katex-filter.js -Mbatch-katex-errors 2> errors.txt

# Generate HTML file, even with errors from source.
pandoc -i samples/hello-error.md -o samples/output/hello-error.html -H samples/styles/styles.html -F src/katex-filter.js -Mbatch-katex-errors
```

## Use Cases
- Pre-rendering the math on a site built with a static site generator. (My case with [Hugo](https://gohugo.io/).)

## How does this work?
Pandoc is a software capable of converting documents from one format to another. With filters, we can add custom logic to extend the functionality of Pandoc.

To render KaTeX markup, we take the TeX content found by Pandoc, and use the KaTeX library to render TeX into HTML.

## Related Links
Thanks to the people in these links for their open contributions.
1) [pandoc-static-katex](https://github.com/Zaharid/pandoc_static_katex) - Python filter
2) [Server-side rendering discussion](https://github.com/jgm/pandoc/issues/6651)
