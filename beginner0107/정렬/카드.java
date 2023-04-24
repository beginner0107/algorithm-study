import java.util.HashMap;
import java.util.Scanner;

public class 카드 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    HashMap<Long, Integer> map = new HashMap<>();
    while (n -- > 0) {
      long key = sc.nextLong();
      map.put(key, map.getOrDefault(key, 0) + 1);
    }
    int ans = 0;
    long k = 0;
    for (Long key : map.keySet()) {
      if (map.get(key) > ans || (map.get(key) == ans && key < k)) {
        ans = map.get(key);
        k = key;
      }
    }
    System.out.println(k);
  }
}