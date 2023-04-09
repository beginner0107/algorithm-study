class 쿼드압축 {
    static int[] answer;
    public int[] solution(int[][] arr) {
        answer = new int[2];
        divided(arr, 0, 0, arr.length);
        return answer;
    }

    private void divided(int[][] arr, int x, int y, int size) {
        if (check(x, y, size, arr)) {
            answer[arr[x][y]] ++;
            return;
        }
        int dSize = size / 2;
        divided(arr, x, y, dSize);
        divided(arr, x + dSize, y, dSize);
        divided(arr, x, y + dSize, dSize);
        divided(arr, x + dSize, y + dSize, dSize);
    }

    private boolean check(int x, int y, int size, int[][]arr) {
        int value = arr[x][y];
        boolean isOk = true;
        for (int i = x; i < x + size; i ++) {
            for (int j = y; j < y + size; j ++) {
                if (value != arr[i][j]) {
                    isOk = false;
                    break;
                }
            }
        }
        return isOk;
    }
}