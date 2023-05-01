import java.util.*;
class 빛의경로 {
    
    static int X, Y;
    static boolean visited[][][];
    static int[]dy = {-1,0,1,0};
    static int[]dx = {0,-1,0,1};
    public int[] solution(String[] grid) {
        X = grid.length;
        Y = grid[0].length();
        
        visited = new boolean[X][Y][4];
        ArrayList<Integer>list = new ArrayList<>();
        for(int i=0;i<X;i++){
            for(int j=0;j<Y;j++){
                for(int k=0;k<4;k++){
                    if(!visited[i][j][k]){
                        list.add(dfs(grid, i, j, k));
                    }
                }
            }
        }
        
        return list.stream().sorted().mapToInt(s -> s).toArray();
    }
    
    public int dfs(String[]grid, int i, int j, int k){
        int cnt = 0;
        while(!visited[i][j][k]){
            visited[i][j][k] = true;
            cnt++;
            if(grid[i].charAt(j)=='L'){
                k = k==0?3:k-1;
            }
            else if(grid[i].charAt(j)=='R'){
                k = k==3?0:k+1;
            }
            
            i = (i + dy[k] + X) % X;
            j = (j + dx[k] + Y) % Y;
        }
        return cnt;
    }
}