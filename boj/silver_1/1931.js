const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  input.shift();
  const newInput = input.map((v) => v.split(" ").map((v) => v * 1));
  newInput.sort(function (a, b) {
    if (a[1] == b[1]) return a[0] - b[0];
    return a[1] - b[1];
  });
  let cnt = 0;
  let currentTime = 0;
  newInput.forEach((time) => {
    if (time[0] >= currentTime) {
      cnt += 1;
      currentTime = time[1];
    }
  });
  console.log(cnt);
};

const input = [];
rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  solution(input);
  process.exit();
});
