import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] map = new int[N][N];

		int[] dx = { 0, 0, -1, 1 };
		int[] dy = { -1, 1, 0, 0 };
		int startX = -1;
		int startY = -1;
		Queue<int[]> curPoses = new LinkedList<>();

		int move = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] = sc.nextInt();
				if (map[i][j] == 9) {
					startX = i;
					startY = j;
				}
			}
		}
		int curSize = 2;
		int sizeUp = 0;
		while (true) {
			int[] startNode = { startX, startY };
			curPoses.add(startNode);
			int[][] bfsMap = new int[N][N];
			while (curPoses.size() > 0) {
				int[] curPos = curPoses.poll();
				int x = curPos[0];
				int y = curPos[1];

				for (int i = 0; i < 4; i++) {
					int nx = x + dx[i];
					int ny = y + dy[i];
					int[] newPos = { nx, ny };
					if (nx < 0 || nx >= N || ny < 0 || ny >= N || map[nx][ny] > curSize)
						continue;
					if (bfsMap[nx][ny] == 0) {
						bfsMap[nx][ny] = bfsMap[x][y] + 1;
						curPoses.add(newPos);
					}

				}
			}
			int nextPosX = -1;
			int nextPosY = -1;
			int nextDistance = 9999;
			for (int i = 0; i < bfsMap.length; i++) {
				for (int j = 0; j < bfsMap[0].length; j++) {
					if (curSize > map[i][j] && map[i][j] > 0 && bfsMap[i][j] > 0 && bfsMap[i][j] < nextDistance) {
						nextPosX = i;
						nextPosY = j;
						nextDistance = bfsMap[i][j];
					}
				}
			}

			if (nextPosX == -1 && nextPosY == -1) {
				break;
			}

			move += nextDistance;
			map[nextPosX][nextPosY] = 9999;
			map[startX][startY] = 0;
			sizeUp += 1;
			if (sizeUp == curSize && curSize < 10) {
				sizeUp = 0;
				curSize += 1;
			}

			startX = nextPosX;
			startY = nextPosY;
//			System.out.println("++++++++++++++++++++++++");
//			for (int i = 0; i < map.length; i++) {
//				System.out.println(Arrays.toString(map[i]));
//			}

		}
		System.out.println(move);

		sc.close();
	}
}
