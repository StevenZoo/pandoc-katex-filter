#!/usr/bin/env node
const pandoc = require("pandoc-filter");
const katex = require("katex");

const BATCH_ERRORS = "katex-batch-errors";

function getMetadataProperty(meta, property) {
  return meta.hasOwnProperty(property) && meta[property].c;
}

function logError(message, input) {
  console.error(message);
  console.group();
  console.error("Input:");
  console.group();
  console.error(input + "\n");
  console.groupEnd();
  console.groupEnd();
}

function render(tex, options) {
  try {
    return [katex.renderToString(tex, options)];
  } catch (err) {
    let errOptions = { ...options, throwOnError: false };
    return [katex.renderToString(tex, errOptions), err];
  }
}

function action({ t: type, c: value }, format, meta) {
  if (type === "Math") {
    let [attr, tex] = value;
    let options = { displayMode: attr.t === "DisplayMath", throwOnError: true };

    let [html, err] = render(tex, options);

    // Handle error if needed. 
    // Either log to stderr or throw immediately.
    if (err !== undefined) {
      let shouldBatchErrors = getMetadataProperty(meta, BATCH_ERRORS);
      if (shouldBatchErrors) logError(err.message, tex);
      else throw err;
    }

    // Return HTML generated from KaTeX
    return pandoc.RawInline("html", html);
  }
}

pandoc.stdio(action);
