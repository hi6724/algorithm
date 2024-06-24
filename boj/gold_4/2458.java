import java.io.*;
import java.util.*;

public class Main {
	static ArrayList<ArrayList<Integer>> graph1;
	static ArrayList<ArrayList<Integer>> graph2;

	public static void main(String[] args) {
		graph1 = new ArrayList<>();
		graph2 = new ArrayList<>();
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int ans = 0;

		for (int i = 0; i < n; i++) {
			graph1.add(new ArrayList<>());
			graph2.add(new ArrayList<>());
		}

		for (int i = 0; i < m; i++) {
			int from = sc.nextInt() - 1;
			int to = sc.nextInt() - 1;
			graph1.get(from).add(to);
			graph2.get(to).add(from);
		}

		for (int i = 0; i < n; i++) {
			boolean[] visited = new boolean[n];
			Queue<Integer> q = new LinkedList<>();
			q.add(i);
			int cnt = 1;
			visited[i] = true;
			while (q.size() > 0) {
				int cur = q.poll();
				ArrayList<Integer> nextNodes = graph1.get(cur);
				for (int j = 0; j < nextNodes.size(); j++) {
					int nextNode = nextNodes.get(j);
					if (!visited[nextNode]) {
						q.add(nextNode);
						visited[nextNode] = true;
						cnt += 1;
					}
				}
			}

			q.add(i);
			while (q.size() > 0) {
				int cur = q.poll();
				ArrayList<Integer> nextNodes = graph2.get(cur);
				for (int j = 0; j < nextNodes.size(); j++) {
					int nextNode = nextNodes.get(j);
					if (!visited[nextNode]) {
						q.add(nextNode);
						visited[nextNode] = true;
						cnt += 1;
					}
				}
			}

			if (cnt == n) {
				ans += 1;
			}
		}
		System.out.println(ans);
	}
}
