

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static void rotate(int[][] boards, int x1, int y1, int x2, int y2) {
		int temp, pastTemp;

		temp = boards[x1][y2];
		for (int y = y2; y > y1; y--) {
			boards[x1][y] = boards[x1][y - 1];
		}
		pastTemp = temp;
		temp = boards[x2][y2];

		for (int x = x2; x > x1; x--) {
			if (x - 1 == x1) {
				boards[x][y2] = pastTemp;
				continue;
			}
			boards[x][y2] = boards[x - 1][y2];
		}
		pastTemp = temp;
		temp = boards[x2][y1];

		for (int y = y1; y < y2; y++) {
			if (y + 1 == y2) {
				boards[x2][y] = pastTemp;
				continue;
			}

			boards[x2][y] = boards[x2][y + 1];
		}
		pastTemp = temp;
		for (int x = x1; x < x2; x++) {
			if (x + 1 == x2) {
				boards[x][y1] = pastTemp;
				continue;
			}

			boards[x][y1] = boards[x + 1][y1];
		}

		return;
	}

	static int[][] copyMap(int[][] map) {
		int[][] nMap = new int[map.length][map[0].length];

		for (int i = 0; i < map.length; i++) {
			System.arraycopy(map[i], 0, nMap[i], 0, map[0].length);
		}

		return nMap;
	}

	private static boolean[] visited;
	private static int[] arr;
	private static int minValue = 99999999;

	private static void permutation(int[] arr, int cnt, int[][] boards, int[][] console) {
		if (cnt == arr.length) {
			int[][] copy = copyMap(boards);
			for (int j = 0; j < arr.length; j++) {
				int r = console[arr[j]][0];
				int c = console[arr[j]][1];
				int s = console[arr[j]][2];
				for (int i = 0; i < s; i++) {
					int x1 = r - s + i;
					int y1 = c - s + i;
					int x2 = r + s - i;
					int y2 = c + s - i;
					rotate(copy, x1, y1, x2, y2);
				}
			}

			int[] ans = new int[copy.length];
			for (int i = 0; i < copy.length; i++) {
				int temp = 0;
				for (int j = 0; j < copy[0].length; j++) {
					temp += copy[i][j];
				}
				if (minValue > temp) {
					minValue = temp;
				}
			}

			return;
		}
		for (int i = 0; i < arr.length; i++) {
			if (!visited[i]) {
				visited[i] = true;
				arr[cnt] = i;
				permutation(arr, cnt + 1, boards, console);
				visited[i] = false;
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int T = sc.nextInt();
		int[][] console = new int[T][3];
		int[][] boards = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				boards[i][j] = sc.nextInt();
			}
		}

		for (int pp = 0; pp < T; pp++) {
			int r = sc.nextInt() - 1;
			int c = sc.nextInt() - 1;
			int s = sc.nextInt();
			console[pp][0] = r;
			console[pp][1] = c;
			console[pp][2] = s;

		}

		arr = new int[console.length];
		visited = new boolean[console.length + 1];
		permutation(arr, 0, boards, console);
// 0~console.length 로 순열 만들기

		System.out.println(minValue);

	}
}
