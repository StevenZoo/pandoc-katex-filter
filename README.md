# pandoc-server-side-katex

This project sets up an environment to pre-render [KaTeX](https://katex.org/) markup into HTML with Pandoc. 

## Requirements
- [Pandoc](https://pandoc.org/)
- [Python 3](https://www.python.org/)
- [Node.js](https://nodejs.org/en/)

Please make sure you have Pandoc, Python, and Node.js already installed.

## Installation

Run these commands to install the necessary dependencies.

```
## Node
npm install

## Python
pip3 install -r requirements.txt 
```

## Example Usage
```
# Start the server
npm start
```


Open a second terminal
```
# Pipe TeX input
echo '$a+b$' | pandoc --filter pandoc-filters/python/katex.py

# Process input file
pandoc -i samples/hello.md --filter pandoc-filters/python/katex.py

# Create standalone HTML file
pandoc -i samples/hello.md -H samples/styles/styles.html --filter pandoc-filters/python/katex.py > samples/output/hello.html
```

## Use Cases
- Pre-rendering the math on a site built with a static site generator. (My case with [Hugo](https://gohugo.io/).)

## How does this work?
Pandoc is a software capable of converting documents from one format to another. With filters, we can add custom logic to extend the functionality of Pandoc.

To render KaTeX markup, we have a Node.js server running in the background. This server uses the KaTeX library to render TeX into HTML.

The Python filter is the bridge between Pandoc and Node - it takes the TeX content found by Pandoc, passes it to the server, and returns the rendered HTML back to Pandoc.

Having a server running in the background helps with performance. We avoid the time penalty from creating a new Node process each time we render a math expression.

## Related Links
Thank you to the people in these links for their open contributions.
1) [pandoc-static-katex](https://github.com/Zaharid/pandoc_static_katex) - Python filter
2) [Server-side rendering discussion](https://github.com/jgm/pandoc/issues/6651)
