
import java.util.Scanner;

public class Main {
	static String sb = "";
	static int[][] img;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		img = new int[N][N];

		for (int i = 0; i < N; i++) {
			String str = sc.next();

			for (int j = 0; j < N; j++) {
				img[i][j] = str.charAt(j) - '0';
			}
		}

		sol(0, 0, N);
		System.out.println(sb);
	}

	public static void sol(int x, int y, int size) {

		if (isPossible(x, y, size)) {
			sb += img[x][y];
			return;
		}

		int half = size / 2;

		sb += "(";
		sol(x, y, half);
		sol(x, y + half, half);
		sol(x + half, y, half);
		sol(x + half, y + half, half);
		sb += ")";
	}

	private static boolean isPossible(int x, int y, int size) {

		for (int i = x; i < x + size; i++) {
			for (int j = y; j < y + size; j++) {
				if (img[x][y] != img[i][j]) {
					return false;
				}
			}
		}
		return true;
	}
}
