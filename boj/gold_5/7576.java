import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] dx = { 0, 0, -1, 1 };
		int[] dy = { -1, 1, 0, 0 };

		int M = sc.nextInt();
		int N = sc.nextInt();

		int[][] tomatos = new int[N][M];

		Queue<int[]> q = new LinkedList<>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				tomatos[i][j] = sc.nextInt();
				if (tomatos[i][j] == 1) {
					int[] temp = { i, j };
					q.add(temp);
				}
			}
		}
		while (q.size() > 0) {

			int[] node = q.poll();
			int x = node[0];
			int y = node[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= N || ny < 0 || ny >= M)
					continue;

				if (tomatos[nx][ny] == 0) {
					tomatos[nx][ny] = tomatos[x][y] + 1;
					int[] temp = { nx, ny };
					q.add(temp);
				}

			}
		}

		int ans = -999;

		Loop: for (int i = 0; i < tomatos.length; i++) {
			for (int j = 0; j < tomatos[0].length; j++) {
				if (tomatos[i][j] == 0) {
					ans = 0;
					break Loop;
				} else if (tomatos[i][j] > ans) {
					ans = tomatos[i][j];
				}

			}
		}

		System.out.println(ans - 1);

		sc.close();
	}
}
