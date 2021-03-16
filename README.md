# pandoc-server-side-katex

This project sets up an environment to pre-render KaTeX markup into HTML using Pandoc. 

## Installation

This project assumes you have Pandoc, Python, and Node.js installed.

```
## Node
npm install

# Python
pip3 install -r requirements.txt 
```

## Example Usage
```
# Start the server
npm start

# Pipe TeX input
echo '$a+b$' | pandoc --filter pandoc-filters/python/katex.py

# Process input file
pandoc -i samples/hello.md --filter pandoc-filters/python/katex.py

# Create standalone HTML file
pandoc -i samples/hello.md -H samples/styles/styles.html --filter pandoc-filters/python/katex.py > samples/output/hello.html
```

## How does this work?
Pandoc is a software capable of converting documents from one format to another. With filters, we can incorporate custom logic into this process.

To render KaTeX markup, we have a Node.js server running in the background. This server is capable of rendering KaTeX into HTML.

The Python filter is the bridge between Pandoc and Node - it takes the KaTeX content found by Pandoc, passes it to the server, and returns the rendered HTML back to Pandoc.

Having a server running in the background helps with performance. We avoid the time penalty from creating a new Node process each time we render a math expression.


## Related Links
Thank you to the people in these links for their open contributions.
1) [pandoc-static-katex](https://github.com/Zaharid/pandoc_static_katex) - Python filter
2) [Server-side rendering discussion](https://github.com/jgm/pandoc/issues/6651)