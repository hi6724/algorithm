import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] dx = { 0, 0, -1, 1 };
		int[] dy = { -1, 1, 0, 0 };

		int N = sc.nextInt();
		int M = sc.nextInt();
		int[][] map = new int[N][M];

		Queue<int[]> q = new LinkedList<int[]>();

		for (int i = 0; i < N; i++) {
			String temp = sc.next();
			for (int j = 0; j < temp.length(); j++) {
				map[i][j] = temp.charAt(j);
				if (map[i][j] == '*') {
					int[] tempPos = { i, j };
					q.add(tempPos);
				}
			}
		}

		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				if (map[i][j] == 'S') {
					map[i][j] = -1;
					int[] tempPos = { i, j };
					q.add(tempPos);
				}
			}
		}
		int ans = 9999;
		loop: while (q.size() > 0) {
			int[] node = q.poll();
			int x = node[0];
			int y = node[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= N || ny < 0 || ny >= M)
					continue;
				if (map[x][y] == 42) {
					// 물 이동
					if (map[nx][ny] == 46) {
						map[nx][ny] = 42;
						int[] temp = { nx, ny };
						q.add(temp);
					}
				} else if (map[x][y] < 0) {
					// 고슴이 이동
					if (map[nx][ny] == 46) {
						map[nx][ny] = map[x][y] - 1;
						int[] temp = { nx, ny };
						q.add(temp);
					} else if (map[nx][ny] == 68) {
						ans = -map[x][y];
						break loop;
					}
				}

			}

//			System.out.println("++++++");
//			for (int i = 0; i < map.length; i++) {
//				System.out.println(Arrays.toString(map[i]));
//			}
		}

		if (ans == 9999) {
			System.out.println("KAKTUS");
		} else {
			System.out.println(ans);
		}

	}
}

//5 4
//...*
//....
//D.X.
//S.*.
//....
