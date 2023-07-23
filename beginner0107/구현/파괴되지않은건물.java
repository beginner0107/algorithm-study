import java.util.*;
class 파괴되지않은건물 {
    public static int solution(int[][] board, int[][] skill) {
        int N = board.length;
        int M = board[0].length;

        // Create a 2D prefix sum array to keep track of the cumulative changes in building durability
        int[][] prefixSum = new int[N + 1][M + 1];

        // Process the skill array and update the prefix sum array accordingly
        for (int[] s : skill) {
            int type = s[0];
            int r1 = s[1];
            int c1 = s[2];
            int r2 = s[3];
            int c2 = s[4];
            int degree = s[5];

            if (type == 1) {
                // Enemy attack, decrease the durability by degree
                prefixSum[r1][c1] -= degree;
                prefixSum[r1][c2 + 1] += degree;
                prefixSum[r2 + 1][c1] += degree;
                prefixSum[r2 + 1][c2 + 1] -= degree;
            } else if (type == 2) {
                // Ally recovery, increase the durability by degree
                prefixSum[r1][c1] += degree;
                prefixSum[r1][c2 + 1] -= degree;
                prefixSum[r2 + 1][c1] -= degree;
                prefixSum[r2 + 1][c2 + 1] += degree;
            }
        }

        // Update the actual building durability using the prefix sum array
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                prefixSum[i + 1][j] += prefixSum[i][j];
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                prefixSum[i][j + 1] += prefixSum[i][j];
            }
        }

        // Count the undestroyed buildings
        int undestroyed = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] + prefixSum[i][j] > 0) {
                    undestroyed++;
                }
            }
        }

        return undestroyed;
    }
}