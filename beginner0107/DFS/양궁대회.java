class 양궁대회 {
    static int[] lion;
    static int max = -1000;

    static int[]res = {-1};


    public int[] solution(int n, int[] info) {
        lion = new int[11];
        dfs(info, n, 0);

        return res;
    }

    private void dfs(int[]info, int n,int cnt) {
        if(n==cnt){
            int aSum = 0;
            int lSum = 0;
            for(int i=0;i<11;i++){
                if(info[i]!=0 || lion[i]!=0){
                    if(info[i]<lion[i]){
                        lSum += 10-i;
                    }else aSum += 10 - i;
                }
            }


            if(aSum<lSum){
                if(max<=lSum-aSum){
                    max = lSum - aSum;
                    res = lion.clone();
                }
            }
            return;
        }

        for(int i=0;i<11&&lion[i]<=info[i];i++){
            lion[i]++;
            dfs(info, n, cnt+1);
            lion[i]--;
        }
    }
  }