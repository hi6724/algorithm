const readline = require("readline");

const solution = (input) => {
  const [inputX, inputY] = input[0].split(" ").map((v) => v * 1);

  let boards = [];
  for (let index = 0; index < inputY; index++) {
    boards.push(input[index + 1].split(""));
  }
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];

  const dfs = (i, j) => {
    const current = boards[i][j];
    boards[i][j] = "0";
    if (current == "0") {
      return [0, 0];
    }
    let q = [[i, j]];
    let cnt = 1;
    while (q.length > 0) {
      const [x, y] = q.pop();
      for (let d = 0; d < 4; d++) {
        const nx = x + dx[d];
        const ny = y + dy[d];
        if (nx < 0 || nx >= inputY || ny < 0 || ny >= inputX) {
          continue;
        }
        if (boards[nx][ny] == current) {
          q.push([nx, ny]);
          cnt += 1;
          boards[nx][ny] = "0";
        }
      }
    }

    return [current, cnt ** 2];
  };

  let myTeam = 0;
  let opposite = 0;
  for (let i = 0; i < inputY; i++) {
    for (let j = 0; j < inputX; j++) {
      const result = dfs(i, j);
      if (result[0] == "W") {
        myTeam += result[1];
      } else {
        opposite += result[1];
      }
    }
  }

  console.log(myTeam, opposite);
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];
rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  solution(input);
  process.exit();
});
