import java.util.*;

public class Main {
	static boolean isLine = false;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int T = sc.nextInt();

		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < T; i++) {
			int from = sc.nextInt();
			int to = sc.nextInt();

			graph.get(from).add(to);
			graph.get(to).add(from);

		}

		for (int startNode = 0; startNode < N; startNode++) {
			boolean[] visited = new boolean[N];
			dfs(startNode, graph, visited, 1);
			if (isLine) {
				break;
			}
		}
		System.out.println(isLine ? 1 : 0);
		sc.close();
	}

	static void dfs(int start, ArrayList<ArrayList<Integer>> graph, boolean[] visited, int cnt) {
		if (cnt == 5) {
			isLine = true;
			return;
		}

		visited[start] = true;
		for (int i : graph.get(start)) {
			if (!visited[i]) {
				dfs(i, graph, visited, cnt + 1);
			}

			if (isLine) {
				return;
			}
		}
		visited[start] = false;
	}
}
