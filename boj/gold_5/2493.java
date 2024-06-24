

import java.io.*;
import java.util.*;

public class Main {
	@SuppressWarnings("rawtypes")
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] ans = new int[N];
		Stack<ArrayList> stack = new Stack<>();
		ArrayList<Integer> temp = new ArrayList<>();
		StringTokenizer st = new StringTokenizer(br.readLine());

		temp.add(0);
		temp.add(Integer.parseInt(st.nextToken()));

		stack.push(temp);
		ans[0] = -1;

		for (int i = 1; i < N; i++) {
			ArrayList<Integer> income = new ArrayList<>();
			income.add(i);
			income.add(Integer.parseInt(st.nextToken()));
			int tempIndex = 0;
			while (true) {
				if (stack.size() == 0) {
					tempIndex = -1;
					break;
				}
				@SuppressWarnings("unchecked")
				ArrayList<Integer> prev = stack.peek();

				if (income.get(1) >= prev.get(1)) {
					tempIndex = (int) stack.pop().get(0);
				} else {
					tempIndex = (int) prev.get(0);
					break;
				}
			}
			ans[i] = tempIndex;
			stack.push(income);

		}
		for (int i = 0; i < ans.length; i++) {
			System.out.print((ans[i] + 1) + " ");
		}

	}

}

/*
 * 차례대로 list 에 담음 왼쪽이 오른쪽보다 작으면 지워도 무방함 ex) [1,2,3] =>[3], [2,5,1,4] => [5,4]
 * 
 * [1] => 2 => [2] => 1 => [2,1] => 3 => [3] [200]=> 99~1 => [200, 98, 73 ...
 * 13, 1] => 300 =>
 * 
 * 
 * 
 * 6 9 5 7 100 4 3 1 99
 * 
 * [(6,1)] => [(9,2)] => [(9,2),(5,3)] => [(9,2),(7,4)] => [(9,2),(100,5)] =>
 * [(9,2),(100,5),(4,6)] => [(9,2),(100,5),(4,6),(3,7),(1,8)]
 * 
 * 
 * 
 * 
 * 
 */