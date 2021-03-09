const net = require("net");
const katex = require("katex");

const HOST = "localhost";
const PORT = 7000;

const EOT_BYTE = "\x04";
const EOT_INT = 4;
let NUM_BYTES_META = 2;

function renderToString(tex, display) {
  return katex.renderToString(tex, {
    displayMode: display,
  });
}

function render(tex, display) {
  let output;
  let errorByte = "\x00";

  try {
    output = renderToString(tex, display);
  } catch (e) {
    console.log(e);
    output = e;
    errorByte = "\x01";
  }

  return output + errorByte + EOT_BYTE;
}

let server = net.createServer((stream) => {
  let chunks = [];

  stream.on("data", (chunk) => {
    chunks += chunk;

    let EOT = chunk[chunk.length - 1] === EOT_INT;

    if (EOT) {
      let buffer = Buffer.from(chunks);
      let display = buffer[buffer.length - 2] === 1;

      let tex = buffer.toString("UTF-8", 0, buffer.length - NUM_BYTES_META);

      stream.write(render(tex, display));
    }
  });

  stream.on("error", (e) => {
    console.error(e);
  });
});

server.on("close", () => {
  console.log("Server closing.");
});

server.on("error", (e) => {
  console.error(e);
});

server.listen(PORT, HOST, () => {
  console.log(`Server started at ${HOST}:${PORT}`);
});
