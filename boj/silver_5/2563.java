

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] board = new int[101][101];
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				board[i][j] = 0;
			}
		}

		int tc = sc.nextInt();

		for (int i = 0; i < tc; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			for (int dx = 0; dx < 10; dx++) {
				for (int dy = 0; dy < 10; dy++) {
					board[x + dx][y + dy] = 1;
				}
			}
		}

		int ans = 0;

		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				ans += board[i][j];
			}
		}
		System.out.println(ans);

	}

}
