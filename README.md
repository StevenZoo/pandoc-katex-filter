# pandoc-katex-filter

This project sets up an environment to pre-render [KaTeX](https://katex.org/) markup into HTML with Pandoc. 

## Requirements
- [Pandoc](https://pandoc.org/)
- [Node.js](https://nodejs.org/en/)

Please make sure you have Pandoc and Node.js already installed.

## Installation

Run these commands to install the necessary dependencies.

```
## Node
npm install
```

## Example Usage

```
# Pipe TeX input
echo '$a+b$' | pandoc --filter src/katex-filter.js

# Process input file
pandoc -i samples/hello.md --filter src/katex-filter.js

# Create standalone HTML file
pandoc -i samples/hello.md -H samples/styles/styles.html --filter src/katex-filter.js > samples/output/hello.html
```

## Error Handling

If KaTeX can't render an expression to HTML, it will throw an error. By default, this filter will propagate that error immediately.

Alternatively, add the `batch-katex-error` flag to direct the error message to standard error, and continue processing. This can be useful if you want to see all errors at once.

```
# Process input file with error
pandoc -i samples/hello-error.md --filter src/katex-filter.js

# Pipe errors to standard error
pandoc -i samples/hello-error.md --filter src/katex-filter.js -Mbatch-katex-errors

# Create standalone HTML file. (Incorrect TeX will be highlighted in red.)
pandoc -i samples/hello-error.md -H samples/styles/styles.html --filter src/katex-filter.js -Mbatch-katex-errors > samples/output/hello-error.html
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
