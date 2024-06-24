

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] board = new int[1001][1001];
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				board[i][j] = 0;
			}
		}

		int tc = sc.nextInt();

		for (int i = 0; i < tc; i++) {
			int y = sc.nextInt();
			int x = sc.nextInt();
			int height = sc.nextInt();
			int width = sc.nextInt();
			for (int dx = 0; dx < width; dx++) {
				for (int dy = 0; dy < height; dy++) {
					board[x + dx][y + dy] = i + 1;
				}
			}
		}

		int[] ans = new int[tc + 1];

		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				ans[board[i][j]] += 1;
			}
		}
		for (int i = 1; i < ans.length; i++) {
			System.out.println(ans[i]);

		}
	}

}
