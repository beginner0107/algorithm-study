import java.util.LinkedList;
import java.util.Queue;

public class 숫자변환하기 {
    public static int bfs(int start, int end, int increment) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        int[] visited = new int[end + 1];

        while (!queue.isEmpty()) {
            int node = queue.poll();
            int oneStep = node + increment;
            int twoStep = node * 2;
            int threeStep = node * 3;

            for (int i : new int[]{oneStep, twoStep, threeStep}) {
                if (i <= end && visited[i] == 0) {
                    visited[i] = visited[node] + 1;
                    queue.add(i);
                }
            }
        }
        return visited[end];
    }

    public static int solution(int x, int y, int n) {
        if (x == y) {
            return 0;
        }
        int answer = bfs(x, y, n);
        if (answer == 0) {
            return -1;
        }
        return answer;
    }
}
