

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] costs = new int[N][3];
		for (int i = 0; i < N; i++) {
			costs[i][0] = sc.nextInt();
			costs[i][1] = sc.nextInt();
			costs[i][2] = sc.nextInt();
		}
		for (int i = 1; i < N; i++) {
			for (int j = 0; j < 3; j++) {
				if (j == 0) {
					costs[i][j] = Math.min(costs[i-1][1], costs[i-1][2]) + costs[i][j];
				}
				else if (j == 1) {
					costs[i][j] = Math.min(costs[i-1][0], costs[i-1][2]) + costs[i][j];

				} else {
					costs[i][j] = Math.min(costs[i-1][0], costs[i-1][1]) + costs[i][j];
				}
			}
			
		}
		
		System.out.println(Math.min(costs[N-1][2],Math.min(costs[N-1][1],costs[N-1][0])));
	}
}
