
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int tc = sc.nextInt();
		int[] arr = new int[N + 1];
		arr[0] = 0;

		for (int i = 1; i < N + 1; i++) {
			int num = sc.nextInt();
			arr[i] = arr[i - 1] + num;
		}
		for (int i = 0; i < tc; i++) {
			int start = sc.nextInt() - 1;
			int end = sc.nextInt();
			int ans = arr[end] - arr[start];
			System.out.println(ans);
		}

		sc.close();
	}
}
