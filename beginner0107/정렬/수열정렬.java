import java.util.Arrays;
import java.util.Scanner;

public class 수열정렬 {

  static Scanner scan = new Scanner(System.in);
  static StringBuilder sb = new StringBuilder();
  static int N;
  static int[] P;
  static Elem[] B;

  static void input() {
    N = scan.nextInt();
    B = new Elem[N];
    P = new int[N];
    for (int i = 0; i < N; i++) {
      B[i] = new Elem();
      B[i].num = scan.nextInt();
      B[i].idx = i;
    }
  }

  static void pro() {
    Arrays.sort(B);

    for (int b_idx = 0; b_idx < N; b_idx++) {
      P[B[b_idx].idx] = b_idx;
    }

    for (int i = 0; i < N; i++) {
      sb.append(P[i]).append(' ');
    }
    System.out.println(sb.toString());
  }

  public static void main(String[] args) {
    input();
    pro();
  }


  static class Elem implements Comparable<Elem> {
    public int num, idx;

    @Override
    public int compareTo(Elem o) {
      return num - o.num;
    }
  }
}
