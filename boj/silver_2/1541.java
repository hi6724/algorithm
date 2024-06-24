
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String rootStr = sc.next();
		String[] sp = rootStr.split("\\-");
		ArrayList<Integer> sumList = new ArrayList<>();

		for (String reg : sp) {
			String[] nums = reg.split("\\+");
			int temp = 0;
			for (String num : nums) {
				temp += Integer.parseInt(num);
			}
			sumList.add(temp);
		}
		int ans = sumList.get(0);

		for (int i = 1; i < sumList.size(); i++) {
			ans -= sumList.get(i);
		}
		System.out.println(ans);

		sc.close();
	}
}
