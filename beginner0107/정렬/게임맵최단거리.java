import java.util.*;

public class 게임맵최단거리 {
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    public int solution(int[][] maps) {
        int cnt = bfs(maps);
        return cnt == 0 ? -1 : cnt;
    }

    public int bfs(int[][]maps){
        int visited[][] = new int[maps.length][maps[0].length];
        Queue q = new ArrayDeque();
        q.add(new int[]{0, 0});
        visited[0][0] = 1;
        while (!q.isEmpty()) {
            int[] xy = (int[])q.poll();
            int x = xy[0];
            int y = xy[1];

            for (int i = 0; i < 4; i ++ ){
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 범위 안에 있는지 1일 경우에만 이동
                if (nx >= 0 && nx < maps.length && ny >= 0 && ny < maps[0].length) {
                    if (maps[nx][ny] != 1 || visited[nx][ny] != 0) {
                        continue;
                    }
                    visited[nx][ny] = visited[x][y] + 1;
                    q.add(new int[]{nx, ny});
                }
            }
        }
        return visited[maps.length - 1][maps[0].length - 1];
    }

    public static void main(String[] args) {
        게임맵최단거리 s = new 게임맵최단거리();
        System.out.println(s.solution(new int[][]{{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}}));
    }
}
