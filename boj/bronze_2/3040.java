
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int ans = 1000000000;

		int[] scores = new int[9];

		for (int j = 0; j < 9; j++) {
			scores[j] = sc.nextInt();
		}

		for (int i = (int) Math.pow(2, 7) - 1; i < Math.pow(2, 9) - 1; i++) {
			String temp = "";
			String bin = Integer.toBinaryString(i);
			for (int j = bin.length(); j < 9; j++) {
				temp += "0";
			}
			temp += bin;
			int cnt = 0;
			int cnt2 = 0;
			for (int j = 0; j < temp.length(); j++) {
				if (temp.charAt(j) == '1') {
					cnt += 1;
					cnt2 += scores[j];
				}
			}
			if (cnt == 7 && cnt2 == 100) {
				for (int j = 0; j < temp.length(); j++) {
					if (temp.charAt(j) == '1') {
						System.out.println(scores[j]);
					}
				}
			}
		}
		sc.close();
	}

}
