
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int r = sc.nextInt();
		int c = sc.nextInt();
		int ans = 0;

		while (N > 1) {
			N -= 1;
			int size = (int) Math.pow(2, N);
			if (c < size) {
				if (r >= size) {
					ans += size * size * 2;
					r -= size;
				}
			} else {
				if (r < size) {
					ans += size * size;
					c -= size;
				} else {
					ans += size * size * 3;
					r -= size;
					c -= size;
				}
			}
		}

		ans += r + c;
		if (r == 1 && c == 1) {
			ans += 1;
		}
		if (c == 0 && r == 1) {
			ans += 1;
		}
		System.out.println(ans);

		sc.close();
	}
}
