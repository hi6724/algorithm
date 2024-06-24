
import java.util.*;

public class Main {
	public static void main(String[] args) {
//		CCTV 최대 8대
//		4^8 경우의수 => 65536 
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int finalAns = 0;
		int[][] boards = new int[N][M];
		ArrayList<ArrayList<Integer>> cctvPos = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				boards[i][j] = sc.nextInt();
				if (boards[i][j] == 6) {
				} else if (boards[i][j] != 0) {
					ArrayList<Integer> temp = new ArrayList<>();
					temp.add(i);
					temp.add(j);
					temp.add(boards[i][j]);
					temp.add(0);
					cctvPos.add(temp);
				} else {
					finalAns += 1;
				}
			}
		}

		int[] dx = { -1, 0, 1, 0 };
		int[] dy = { 0, 1, 0, -1 };

		if (cctvPos.size() > 0) {

			for (int i = 0; i < Math.pow(4, cctvPos.size()); i++) {
				String bin = Integer.toString(i, 4);
				String temp = "";
				for (int j = bin.length(); j < cctvPos.size(); j++) {
					temp += "0";
				}
				temp += bin;

				for (int j = 0; j < temp.length(); j++) {
					cctvPos.get(j).set(3, (int) temp.charAt(j) - '0');
				}

				int[][] copyBoards = new int[N][M];
				for (int j = 0; j < boards.length; j++) {
					for (int j2 = 0; j2 < boards[0].length; j2++) {
						copyBoards[j][j2] = boards[j][j2];
					}
				}

//			0:up 1:right 2:down 3:left

				for (int k = 0; k < cctvPos.size(); k++) {
					ArrayList<Integer> cctvInfo = cctvPos.get(k);
					int x = cctvInfo.get(0);
					int y = cctvInfo.get(1);
					int type = cctvInfo.get(2);
					int delta = cctvInfo.get(3);
					copyBoards[x][y] = -1;
					int nx;
					int ny;

					while (true) {
						if (type == 1) {
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							break;
						} else if (type == 2) {
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							if (delta >= 2) {
								delta -= 2;
							} else {
								delta += 2;
							}
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							break;
						} else if (type == 3) {
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							if (delta == 3) {
								delta = 0;
							} else {
								delta += 1;
							}
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							break;

						}

						else if (type == 4) {

							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							if (delta == 3) {
								delta = 0;
							} else {
								delta += 1;
							}
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							if (delta == 3) {
								delta = 0;
							} else {
								delta += 1;
							}
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							break;

						} else if (type == 5) {
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							if (delta == 3) {
								delta = 0;
							} else {
								delta += 1;
							}
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							if (delta == 3) {
								delta = 0;
							} else {
								delta += 1;
							}
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							if (delta == 3) {
								delta = 0;
							} else {
								delta += 1;
							}
							nx = x + dx[delta];
							ny = y + dy[delta];
							while (true) {
								if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
									break;
								}
								if (copyBoards[nx][ny] != 6) {
									copyBoards[nx][ny] = -1;
									nx += dx[delta];
									ny += dy[delta];
								} else {
									break;
								}
							}
							if (delta == 3) {
								delta = 0;
							} else {
								delta += 1;
							}
							break;
						}

					}

				} // cctvList 를 돌아가면서 boards를 채움
				int ans = 0;
				for (int j = 0; j < copyBoards.length; j++) {
					for (int j2 = 0; j2 < copyBoards[0].length; j2++) {
						if (copyBoards[j][j2] == 0) {
							ans += 1;
						}
					}
				}
				if (finalAns > ans) {
					finalAns = ans;
				}

			} // 4^cctv 갯수만큼 반복
		}
		System.out.println(finalAns);

		sc.close();
	}
}
