import java.util.*;
class 숫자게임 {
  public int solution(int[] A, int[] B) {
    int answer = 0;
    Arrays.sort(A);
    Arrays.sort(B);


    int startA = A.length - 1;
    int startB = B.length - 1;

    // B 가 이기는 경우를 찾아야 함
    while(true) {
      if (A[startA] >= B[startB]) {
        startA --;
      }
      else {
        startA --;
        startB --;
        answer ++;
      }
      if (startA == -1 || startB == -1) break;
    }


    return answer;
  }
}