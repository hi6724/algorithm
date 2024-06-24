
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int range = sc.nextInt();
		int[] lamps = new int[range];
		sc.nextLine();
		String firstInput = sc.nextLine();
		String[] newStr = firstInput.split("\\s+");

		for (int i = 0; i < newStr.length; i++) {
			if (Integer.parseInt(newStr[i]) == 1) {
				lamps[i] = 1;
			}
		}

		int studentsNum = sc.nextInt();
		sc.nextLine();
		for (int i = 0; i < studentsNum; i++) {
			firstInput = sc.nextLine();
			newStr = firstInput.split("\\s+");
			int gender = Integer.parseInt(newStr[0]);
			int index = Integer.parseInt(newStr[1]);

			if (gender == 1) {
				for (int j = 1; j < range + 1; j++) {
					if (j % index == 0) {
						if (lamps[j - 1] == 0) {
							lamps[j - 1] = 1;
						} else {
							lamps[j - 1] = 0;
						}
					}
				}
			}
			if (gender == 2) {
				if (lamps[index - 1] == 0) {
					lamps[index - 1] = 1;
				} else {
					lamps[index - 1] = 0;
				}

				int prevIndex = index - 2;
				int nextIndex = index;
				while (true) {
					if(prevIndex<0) {break;}
					if(nextIndex>=range) {break;}
					if (lamps[prevIndex] == lamps[nextIndex]) {
						if (lamps[prevIndex] == 0) {
							lamps[prevIndex] = 1;
						} else {
							lamps[prevIndex] = 0;
						}
						if (lamps[nextIndex] == 0) {
							lamps[nextIndex] = 1;
						} else {
							lamps[nextIndex] = 0;
						}
						prevIndex -= 1;
						nextIndex += 1;

					} else {
						break;
					}
				}
			}
		}

//		남학생은 스위치 번호가 자기가 받은수의 배수이면 스위치를 토글
//		여학생은 
		int cnt=0;
		for (int i = 0; i < lamps.length; i++) {
			cnt+=1;
			System.out.print(lamps[i]+" ");
			if(cnt==20) {
				System.out.println();
				cnt=0;
			}
		}
	}

}
