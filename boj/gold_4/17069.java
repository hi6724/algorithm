import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] boards = new int[N][N];
		long[][][] dp = new long[N][N][3];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				boards[i][j] = sc.nextInt();
				for (int j2 = 0; j2 < 3; j2++) {
					dp[i][j][j2] = 0;
				}
			}
		}

		dp[0][1][0]=1;
		for (int i = 2; i < N; i++) {
			if (boards[0][i] == 1) {
				break;
			}
			else {
				dp[0][i][0] = 1;
			}
		}


		for (int i = 1; i < N; i++) {
			for (int j = 1; j < N; j++) {
				if(boards[i][j]==1)continue;
				dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][2];
				dp[i][j][1]=dp[i-1][j][1]+dp[i-1][j][2];
				if (boards[i-1][j]!=1&&boards[i][j-1]!=1) {
				dp[i][j][2]=dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2];
				}
			}
		}
//		for (int i = 0; i < dp.length; i++) {
//			for (int j = 0; j < dp.length; j++) {
//				for (int j2 = 0; j2 < 3; j2++) {
//					System.out.print(dp[i][j][j2]);
//				}
//				System.out.print(" ");
//			}
//			System.out.println("");
//		}
		System.out.println(dp[N-1][N-1][0]+dp[N-1][N-1][1]+dp[N-1][N-1][2]);
	}

}
