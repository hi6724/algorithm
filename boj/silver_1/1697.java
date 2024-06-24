
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int MAX = 100001;
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] ans = new int[MAX];
		ans[N] = 1;
		Queue<Integer> q = new LinkedList<>();
		q.offer(N);

		while (q.size() > 0) {
			int node = q.poll();
			int nx;
			nx = node + 1;
			if (nx < MAX && ans[nx] == 0) {
				ans[nx] = ans[node] + 1;
				q.offer(nx);
			}
			nx = node * 2;
			if (nx < MAX && ans[nx] == 0) {
				ans[nx] = ans[node] + 1;
				q.offer(nx);
			}
			nx = node - 1;
			if (nx >= 0 && ans[nx] == 0) {
				ans[nx] = ans[node] + 1;
				q.offer(nx);
			}
		}
		System.out.println(ans[K]-1);

		sc.close();
	}
}
