import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static void comb(int[] arr, boolean[] visited, int depth, int n, int r) {
		int[] dx = { 0, 0, -1, 1 };
		int[] dy = { -1, 1, 0, 0 };

		if (r == 0) {
			int[][] newMap = new int[N][M];
			Queue<int[]> q = new LinkedList<>();
			for (int j = 0; j < newMap.length; j++) {
				for (int j2 = 0; j2 < newMap[0].length; j2++) {
					newMap[j][j2] = map[j][j2];
					if (map[j][j2] == 2) {
						int[] tmp = { j, j2 };
						q.add(tmp);
					}
				}
			}

			for (int i = 0; i < arr.length; i++) {

				if (visited[i]) {
					newMap[walls.get(i)[0]][walls.get(i)[1]] = 1;
				}
			}

			while (q.size() > 0) {
				int[] curNode = q.poll();
				int x = curNode[0];
				int y = curNode[1];
				for (int j = 0; j < 4; j++) {
					int nx = x + dx[j];
					int ny = y + dy[j];
					if (nx >= N || ny >= M || nx < 0 || ny < 0) {
						continue;
					}

					if (newMap[nx][ny] == 0) {
						newMap[nx][ny] = 2;
						int[] tmp = { nx, ny };
						q.add(tmp);
					}
				}
			}
			int cnt = 0;
			for (int j = 0; j < newMap.length; j++) {
				for (int j2 = 0; j2 < newMap[0].length; j2++) {
//					System.out.print(newMap[j][j2]+" ");
					if (newMap[j][j2] == 0)
						cnt += 1;
				}
//				System.out.println("");
			}
			if (cnt > ans) {
				ans = cnt;
			}
			return;
		}

		if (depth == n) {
			return;
		}

		visited[depth] = true;
		comb(arr, visited, depth + 1, n, r - 1);

		visited[depth] = false;
		comb(arr, visited, depth + 1, n, r);
	}

	static int N;
	static int M;
	static int[] arr;
	static boolean[] visited;
	static int[][] map;
	static int ans = 0;
	static ArrayList<int[]> walls;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		map = new int[N][M];
		walls = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				map[i][j] = sc.nextInt();
				if (map[i][j] == 0) {
					int[] tmp = { i, j };
					walls.add(tmp);
				}
			}
		}

		arr = new int[walls.size()];
		for (int i = 0; i < walls.size(); i++) {
			arr[i] = i;
		}
		visited = new boolean[walls.size()];
		comb(arr, visited, 0, walls.size(), 3);
		System.out.println(ans);

	}
}
