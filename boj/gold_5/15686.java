
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
//	N<50 가로 세로
//	M<13 남길 치킨집의 수
//	치킨집의 최댓값은 13
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		ArrayList<ArrayList<Integer>> chickens = new ArrayList<ArrayList<Integer>>();
		ArrayList<ArrayList<Integer>> positions = new ArrayList<ArrayList<Integer>>();
		ArrayList<ArrayList<Integer>> houses = new ArrayList<ArrayList<Integer>>();
		for (int i = 0; i < N; i++) {
			ArrayList<Integer> temp = new ArrayList<>();
			for (int j = 0; j < N; j++) {
				int store = sc.nextInt();
				if (store == 2) {
					ArrayList<Integer> tempPos = new ArrayList<>();
					tempPos.add(i);
					tempPos.add(j);
					positions.add(tempPos);
				} else if (store == 1) {
					ArrayList<Integer> tempHouse = new ArrayList<>();
					tempHouse.add(i);
					tempHouse.add(j);
					houses.add(tempHouse);
				}
				temp.add(store);
			}
			chickens.add(temp);
		}

//		for (int i = 0; i < positions.size(); i++) {
//			System.out.println(positions.get(i));
//		}

		int maxLength = positions.size();
		int finalAns = 1000000;
		for (int i = (int) 0; i < Math.pow(2, maxLength); i++) {
			String temp = "";
			String bin = Integer.toBinaryString(i);
			for (int j = bin.length(); j < maxLength; j++) {
				temp += "0";
			}
			temp += bin;
			int cnt = 0;
			for (int j = 0; j < temp.length(); j++) {
				if (temp.charAt(j) == '1') {
					cnt += 1;
				}
			}
			if (cnt != M) {
				continue;
			}

//			chickens 리스트 깊은 복사
//			ArrayList<ArrayList<Integer>> copy = new ArrayList<ArrayList<Integer>>();
//			for (int j = 0; j < chickens.size(); j++) {
//				ArrayList<Integer> tempList = new ArrayList<>();
//				for (int j2 = 0; j2 < chickens.get(0).size(); j2++) {
//					tempList.add(chickens.get(j).get(j2));
//				}
//				copy.add(tempList);
//			}

//			positions 리스트 깊은복사

			ArrayList<ArrayList<Integer>> copyPos = new ArrayList<ArrayList<Integer>>();
			for (int j = 0; j < positions.size(); j++) {
				ArrayList<Integer> tempList = new ArrayList<>();
				for (int j2 = 0; j2 < positions.get(0).size(); j2++) {
					tempList.add(positions.get(j).get(j2));
				}
				copyPos.add(tempList);
			}

//			치킨집 M개 남기고 제거
			for (int j = 0; j < temp.length(); j++) {
				if (temp.charAt(j) == '0') {
					copyPos.get(j).set(0, -1);
					copyPos.get(j).set(1, -1);
				}
			}
			int[] ansList = new int[100];
			int ans = 0;

			for (int k = 0; k < houses.size(); k++) {
				int minValue = 10000000;
				int houseX = houses.get(k).get(0);
				int houseY = houses.get(k).get(1);
				for (int j = 0; j < copyPos.size(); j++) {
					int x = copyPos.get(j).get(0);
					int y = copyPos.get(j).get(1);

					if (x == -1 && y == -1) {
						continue;
					}

					int distanceX = Math.abs(houseX - x);
					int distanceY = Math.abs(houseY - y);
					if (minValue > distanceX + distanceY) {
						minValue = distanceX + distanceY;
					}
				}
				ans += minValue;
			}
			if (finalAns > ans) {
				finalAns = ans;
			}
		}
		System.out.println(finalAns);
		sc.close();

	}
}
