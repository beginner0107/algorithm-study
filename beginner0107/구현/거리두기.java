class 거리두기 {
    static int dr[] = {1,-1,0,0};
    static int dc[] = {0,0,-1,1};

    static boolean visited[][];
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        visited = new boolean[5][5];
        for(int i=0;i<places.length;i++){
            boolean fs = true;
            loop:
            for(int j=0;j<places[i].length;j++){
                for(int k=0;k<5;k++){
                    if(places[i][j].charAt(k)=='P'){
                        visited[j][k] = true;
                        fs = dfs(places, i, j, k, 2);
                        visited[j][k] = false;
                        if(!fs){
                            answer[i] = 0;
                            break loop;
                        }
                    }
                }
            }
            if(fs){
                answer[i] = 1;
            }
        }

        return answer;
    }

    public boolean dfs(String[][]places,int o, int x, int y, int cnt){
        if(cnt==0) return true;
        for(int i=0;i<4;i++){
            int dx = x + dr[i];
            int dy = y + dc[i];

            if(dx>=0&&dy>=0&&dx<5&&dy<5&&!visited[dx][dy]){
                if(places[o][dx].charAt(dy)=='O'){
                    visited[dx][dy] = true;
                    boolean fs = dfs(places, o, dx, dy, cnt - 1);
                    visited[dx][dy] = false;
                }
                else if(places[o][dx].charAt(dy)=='P'){
                    return false;
                }
            }
        }
        return true;
    }


}