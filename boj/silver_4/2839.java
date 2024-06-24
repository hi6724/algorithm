

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int ans = 0;
		int count3 = 0;
		int count5 = 0;

		while (N > 0) {
			if (N % 5 == 0) {
				count5 = N / 5;
				N = 0;
			} else if (N < 3) {
				ans = -1;
				break;
			} else {
				count3 += 1;
				N -= 3;
			}
		}
		if (N > 0) {
			System.out.println(-1);
		} else {

			System.out.println(count3 + count5);
		}

		sc.close();
	}
}
