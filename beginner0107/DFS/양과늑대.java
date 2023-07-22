import java.util.*;
class Solution {
    
    static int[] gInfo;
    static int answer;
    public int solution(int[] info, int[][] edges) {
        answer = 0;
        gInfo = info;
        boolean [] visited = new boolean[info.length + 1];
        
        dfs(visited, edges, 0, 0, 0);
        
        return answer;
    }
    
    public void dfs(boolean[] visited, int[][] edges, int idx, int sheep, int wolf) {
        if (gInfo[idx] == 0) { // 양일 때
            sheep ++;
        } else { // 늑대일 때
            wolf ++;
        }
        
        if (sheep <= wolf || visited[idx]) return;
        if (sheep > wolf) {
            answer = Math.max(answer, sheep);
        }
        
        visited[idx] = true;
        for (int[] edge : edges) {
            if (visited[edge[0]] && !visited[edge[1]]) {
                boolean tmpVisited[] = new boolean[visited.length];
                for (int i = 0; i < visited.length; i++) {
                    tmpVisited[i] = visited[i];
                }
                
                dfs(tmpVisited, edges, edge[1], sheep, wolf);
            }
        }
        
    }
    
}