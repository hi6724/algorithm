import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tc = sc.nextInt();

		for (int T = 0; T < tc; T++) {
			List<int[]> list = new ArrayList<>();
			int n = sc.nextInt();
			for (int i = 0; i < n + 2; i++) {
				int x = sc.nextInt();
				int y = sc.nextInt();
				list.add(new int[] { x, y });
			}
			boolean[][] flag = new boolean[n + 2][n + 2];
			for (int i = 0; i < n + 2; i++) {
				for (int j = 0; j < n + 2; j++) {
					int[] pos = list.get(i), next = list.get(j);
					int dis = Math.abs(pos[0] - next[0]) + Math.abs(pos[1] - next[1]);

					if (dis <= 1000)
						flag[i][j] = true;
				}
			}

			for (int k = 0; k < n + 2; k++) {
				for (int i = 0; i < n + 2; i++) {
					for (int j = 0; j < n + 2; j++) {
						if (flag[i][k] && flag[k][j]) {
							flag[i][j] = true;
						}
					}
				}
			}
			if (flag[0][n + 1]) {
				System.out.println("happy");
			} else {
				System.out.println("sad");
			}
		}
	}
}
