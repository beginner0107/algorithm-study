import java.util.*;
/*
n명의 권수선수 : 권투 대회 
1 ~ n번까지 번호 받음

권투 경기는 1대 1

만약 A 선수가 B선수보다 실력이 좋다면 A선수는 B선수를 항상 이김
심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 함
하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매실 수 없음

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는
선수의 수를 return
*/
class 순위 {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int INF = 10000000;

        int[][] dist = new int[n+1][n+1];
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                dist[i][j] = INF;
            }
        }

        for(int[] res : results){
            dist[res[0]][res[1]] = 1;
        }

        for(int k=1; k<=n; k++){
            for(int i=1; i<=n; i++){
                for(int j=1; j<=n; j++){
                    if(dist[i][k] + dist[k][j] < dist[i][j]){
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        for(int i=1; i<=n; i++){
            boolean flag = true;
            for(int j=1; j<=n; j++){
                if(i == j) continue;
                if(dist[i][j] == INF && dist[j][i] == INF){
                    flag = false;
                    break;
                }
            }
            if(flag) answer++;
        }

        return answer;
    }
}