
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int total = sc.nextInt();
		int pwLength = sc.nextInt();
		String pwList = sc.next();
		int[] required = new int[4];
		required[0] = sc.nextInt();
		required[1] = sc.nextInt();
		required[2] = sc.nextInt();
		required[3] = sc.nextInt();
		int ans = 0;
		int startIndex = 0;
		int[] cnt = { 0, 0, 0, 0 };
		for (int j = 0; j < pwLength; j++) {
			if (pwList.charAt(j) == 'A') {
				cnt[0] += 1;
			} else if (pwList.charAt(j) == 'C') {
				cnt[1] += 1;
			} else if (pwList.charAt(j) == 'G') {
				cnt[2] += 1;
			} else if (pwList.charAt(j) == 'T') {
				cnt[3] += 1;
			}
		}
		boolean isPass = true;
		for (int j = 0; j < 4; j++) {
			if (required[j] > cnt[j]) {
				isPass = false;
			}
		}
		if (isPass) {
			ans += 1;
		}
		for (int i = 0; i < total - pwLength; i++) {
			isPass = true;
			if (pwList.charAt(startIndex) == 'A') {
				cnt[0] -= 1;
			} else if (pwList.charAt(startIndex) == 'C') {
				cnt[1] -= 1;
			} else if (pwList.charAt(startIndex) == 'G') {
				cnt[2] -= 1;
			} else if (pwList.charAt(startIndex) == 'T') {
				cnt[3] -= 1;
			}

			if (pwList.charAt(startIndex + pwLength) == 'A') {
				cnt[0] += 1;
			} else if (pwList.charAt(startIndex + pwLength) == 'C') {
				cnt[1] += 1;
			} else if (pwList.charAt(startIndex + pwLength) == 'G') {
				cnt[2] += 1;
			} else if (pwList.charAt(startIndex + pwLength) == 'T') {
				cnt[3] += 1;
			}

			startIndex += 1;

			for (int j = 0; j < 4; j++) {
				if (required[j] > cnt[j]) {
					isPass = false;
				}
			}
			if (isPass) {
				ans += 1;
			}

		}
		System.out.println(ans);
		sc.close();
	}

}
