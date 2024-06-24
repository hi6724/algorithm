import java.io.*;
import java.util.*;

public class Main {
	static ArrayList<ArrayList<Integer>> graph;
	static int[] values;
	static int totalValue = 0;
	static int N;
	static int ans = 9999999;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		graph = new ArrayList<>();
		values = new int[N];
		for (int i = 0; i < N; i++) {
			values[i] = sc.nextInt();
			totalValue += values[i];
			graph.add(new ArrayList<>());
		}
		for (int i = 0; i < N; i++) {
			int T = sc.nextInt();
			for (int j = 0; j < T; j++) {
				int tt = sc.nextInt();
				graph.get(i).add(tt - 1);
			}
		}

		ArrayList<Integer> A = new ArrayList<>();
		for (int i = 1; i <= N / 2; i++) {
			comb(0, N - 1, i, A);
		}

		if (ans == 9999999) {
			System.out.println(-1);
		} else {
			System.out.println(ans);
		}

	}

	public static void comb(int start, int n, int r, ArrayList<Integer> A) {
		if (r == 0) {
			ArrayList<Integer> B = new ArrayList<>();
			for (int i = 0; i < N; i++) {
				if (!A.contains(i)) {
					B.add(i);
				}
			}
			solution(A, B);
			return;
		}

		for (int i = start; i <= n; i++) {
			A.add(i);
			comb(i + 1, n, r - 1, A);
			A.remove(A.size() - 1);
		}
	}

	private static void solution(ArrayList<Integer> group1, ArrayList<Integer> group2) {
		// group1 합 구하기
		// group1, group2 가 다 연결되어 있는지 확인
		int sum = 0;
		if (isConnect(group1) && isConnect(group2)) {
			for (int i = 0; i < group1.size(); i++) {
				sum += values[group1.get(i)];
			}

			ans = Math.min(ans, Math.abs((totalValue - sum) - sum));
		}

	}

	private static boolean isConnect(ArrayList<Integer> group) {
		if (group.size() <= 1)
			return true;
		boolean[] visited = new boolean[N];
		for (int i = 0; i < N; i++) {
			visited[i] = false;
		}
		Queue<Integer> q = new LinkedList<>();
		q.add(group.get(0));

		while (q.size() > 0) {
			int node = q.poll();
			visited[node] = true;
			ArrayList<Integer> nextNodes = graph.get(node);
			for (int i = 0; i < nextNodes.size(); i++) {
				int nextNode = nextNodes.get(i);
				if (!visited[nextNode] && group.contains(nextNode)) {
					q.add(nextNode);
				}
			}
		}

		for (int i = 0; i < group.size(); i++) {
			if (visited[group.get(i)] == false)
				return false;
		}
		return true;
	}
}
