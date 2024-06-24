import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] dx = { 0, 0, -1, 1 };
		int[] dy = { -1, 1, 0, 0 };

		int N = sc.nextInt();
		int[][] map = new int[N][N];
		int[][] map2 = new int[N][N];

		Queue<int[]> q = new LinkedList<int[]>();

		for (int i = 0; i < N; i++) {
			String temp = sc.next();
			for (int j = 0; j < temp.length(); j++) {
				map[i][j] = temp.charAt(j);
				map2[i][j] = temp.charAt(j);
			}
		}
		// 색맹이 아닌경우
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int[] startNode = { i, j };
				if (map[i][j] != 0) {
					cnt += 1;
					q.add(startNode);
				}
				while (q.size() > 0) {
					int[] node = q.poll();
					int x = node[0];
					int y = node[1];
					int cur = map[x][y];
					map[x][y] = 0;
					for (int k = 0; k < 4; k++) {
						int nx = x + dx[k];
						int ny = y + dy[k];

						if (nx < 0 || nx >= N || ny < 0 || ny >= N || map[nx][ny] == 0)
							continue;
						if (map[nx][ny] == cur) {
							int[] next = { nx, ny };
							q.add(next);
						}
					}
				}
			}

		}
		System.out.print(cnt + " ");

		// 색맹인 경우

		cnt = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int[] startNode = { i, j };
				if (map2[i][j] != 0) {
					cnt += 1;
					q.add(startNode);
				}
				while (q.size() > 0) {
					int[] node = q.poll();
					int x = node[0];
					int y = node[1];
					int cur = map2[x][y];
					map2[x][y] = 0;
					for (int k = 0; k < 4; k++) {
						int nx = x + dx[k];
						int ny = y + dy[k];

						if (nx < 0 || nx >= N || ny < 0 || ny >= N || map2[nx][ny] == 0)
							continue;
						if (cur == 82 || cur == 71) {
							if (map2[nx][ny] == 82 || map2[nx][ny] == 71) {
								int[] next = { nx, ny };
								q.add(next);
							}
						}

						else if (map2[nx][ny] == cur) {
							int[] next = { nx, ny };
							q.add(next);
						}
					}
				}
			}

		}
		System.out.println(cnt);

		sc.close();
	}
}
