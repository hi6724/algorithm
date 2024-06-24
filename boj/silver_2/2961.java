
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int ans = 1000000000;
		int n = sc.nextInt();

		int[] scores = new int[n];
		int[] kcal = new int[n];

		for (int j = 0; j < n; j++) {
			scores[j] = sc.nextInt();
			kcal[j] = sc.nextInt();
		}

		for (int i = 1; i < Math.pow(2, n); i++) {
			String temp = "";
			String bin = Integer.toBinaryString(i);
			for (int j = bin.length(); j < n; j++) {
				temp += "0";
			}
			temp += bin;
			int tempScore = 1;
			int tempKcal = 0;
			for (int j = 0; j < temp.length(); j++) {
				if (temp.charAt(j) == '1') {
					tempScore *= scores[j];
					tempKcal += kcal[j];
				}
			}
			int gap = Math.abs(tempScore - tempKcal);
			if (gap < ans) {
				ans = gap;
			}

		}
		System.out.println(ans);
		sc.close();
	}

}
