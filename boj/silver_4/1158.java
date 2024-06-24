
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int repeat = sc.nextInt();
		Queue<Integer> q = new LinkedList<>();
		for (int i = 0; i < N; i++) {
			q.add(i + 1);
		}
		ArrayList<Integer> ans = new ArrayList<>();
		while (q.size() > 0) {
			for (int i = 0; i < repeat; i++) {
				int temp = q.poll();
				if (i == repeat - 1) {
					ans.add(temp);
				} else {
					q.add(temp);
				}
			}
		}
		System.out.print("<");
		for (int i = 0; i < ans.size()-1; i++) {
			System.out.print(ans.get(i)+", ");
		}
		System.out.print(ans.get(ans.size()-1));
		System.out.print(">");

	}
}
