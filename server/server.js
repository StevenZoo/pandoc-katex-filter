const net = require("net");
const katex = require("katex");

const HOST = "localhost";
const PORT = 7000;

const ERROR_PREFIX = 'error:';


function renderToString(tex, display) {
  return katex.renderToString(tex, {
    displayMode: display,
  });
}

function render(tex, display) {
  try {
    return renderToString(tex, display);
  } catch (e) {
    console.error(e);
    return ERROR_PREFIX + e;
  }
}

let server = net.createServer((stream) => {
  let chunks = [];

  stream.on("data", (chunk) => {
    chunks += chunk;
  });

  stream.on("end", (e) => {
    let buffer = Buffer.from(chunks);
    let display = buffer[0] === 1;

    let tex = buffer.toString("UTF-8", 1, buffer.length);
    stream.write(render(tex, display));
  }) 

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
