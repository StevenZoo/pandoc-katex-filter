# pandoc-server-side-katex

This project sets up an environment to render KaTeX markup into HTML using Pandoc. It uses a Python filter to process Math blocks found by Pandoc, and a Node.js server to render KaTeX into HTML.

## Installation

This project assumes you have Pandoc, Python, and Node installed.

```
# Node
npm install

# Python
pip3 install -r requirements.txt 
```

## Usage

This command assumes your working directory is at the root of this project.
```
# Start the server
npm start

pandoc -i <file> --filter pandoc-filters/python/katex.py

echo '$a+b$' | pandoc --filter pandoc-filters/python/katex.py
```