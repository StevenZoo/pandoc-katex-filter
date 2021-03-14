# pandoc-server-side-katex

<<<<<<< Updated upstream
This project sets up an environment to render KaTeX markup into HTML using Pandoc. It uses a Python filter to process Math blocks found by Pandoc, and a Node.js server to render KaTeX into HTML.

## Installation

This project assumes you have Pandoc, Python, and Node installed.

```
# Node
=======
This project sets up an environment to pre-render KaTeX markup into HTML using Pandoc. 

## Installation

This project assumes you have Pandoc, Python, and Node.js installed.

```
## Node
>>>>>>> Stashed changes
npm install

# Python
pip3 install -r requirements.txt 
```

<<<<<<< Updated upstream
## Usage
=======
## Example Usage
>>>>>>> Stashed changes

This command assumes your working directory is at the root of this project.
```
# Start the server
npm start

<<<<<<< Updated upstream
pandoc -i <file> --filter pandoc-filters/python/katex.py

echo '$a+b$' | pandoc --filter pandoc-filters/python/katex.py
```
=======
# Pipe TeX input
echo '$a+b$' | pandoc --filter pandoc-filters/python/katex.py

# Process input file
pandoc -i samples/hello.md --filter pandoc-filters/python/katex.py

# Create standalone HTML file
pandoc -i samples/hello.md -H samples/styles/styles.html --filter pandoc-filters/python/katex.py > samples/output/hello.html
```

## How does this work?
Pandoc supports custom filters. Here, we use a filter written in Python. If it receives a math block from Pandoc, it sends it over to a Node.js server that is capable of rendering KaTeX into HTML.

Having a server running in the background helps with performance. We avoid the time penalty from creating a new Node process each time we render a math expression.
>>>>>>> Stashed changes
