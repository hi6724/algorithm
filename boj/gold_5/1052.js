const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  let [n, k] = input.split(" ").map((v) => +v);
  n += 0;
  k += 0;
  let binNum = n.toString(2);
  let cnt = binNum.split("1").length - 1;
  let ans = 0;
  let temp = 1;
  while (cnt > k) {
    ans += n % 2 ** temp;
    n += n % 2 ** temp;
    temp += 1;
    binNum = n.toString(2);
    cnt = binNum.split("1").length - 1;
  }
  console.log(ans);
};

rl.on("line", (answer) => {
  solution(answer);
  rl.close();
});
