import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 성지키기 {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    char[][] map = new char[N][M];

    for (int i = 0; i < N; i ++) {
      map[i] = br.readLine().toCharArray();
    }

    // 1. 각 행/열에 대해 경비원이 있는지 확인한다.
    int existRowCount = 0;
    for (int i = 0; i < N; i ++) {
      boolean exist = false;
      for (int j = 0; j < M; j ++) {
        if (map[i][j] == 'X') {
          exist = true;
          break;
        }
      }
      if (exist) existRowCount ++;
    }

    int existColCount = 0;
    for (int i = 0; i < M; i ++) {
      boolean exist = false;
      for (int j  = 0; j < N; j ++) {
        if (map[j][i] == 'X') {
          exist = true;
          break;
        }
      }
      if (exist) existColCount ++;
    }

    // 2. 보호받지 못하는 행/열의 개수를 구한다.
    int needRowCount = N - existRowCount;
    int needColCount = M - existColCount;
    // 3. 둘 중 큰 값을 출력한다.
    System.out.println(Math.max(needColCount, needRowCount));
  }
}
