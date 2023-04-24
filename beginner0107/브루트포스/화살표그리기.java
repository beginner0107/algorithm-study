import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class 화살표그리기 {

  public static void main(String[] args) {
    // N을 입력 받음
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    // 위치, 색깔을 입력받음
    Map<Integer, ArrayList<Integer>> map = new LinkedHashMap<>();
    while (N -- > 0) {
      int pos = sc.nextInt();
      int color = sc.nextInt();
      if (!map.containsKey(color)) {
        map.put(color, new ArrayList<>(List.of(pos)));
      } else{
        map.get(color).add(pos);
      }
    }

    int ans = 0;
    for (int key : map.keySet()) {
      ArrayList<Integer> tmp = map.get(key);
      Collections.sort(tmp);
      for (int i = 0; i < tmp.size(); i ++) {
        int comparison1 = Integer.MAX_VALUE;
        int comparison2 = Integer.MAX_VALUE;
        if (i - 1 >= 0) {
          comparison1 = Math.abs(tmp.get(i) - tmp.get(i - 1));
        }
        if(i + 1 < tmp.size()) {
          comparison2 = Math.abs(tmp.get(i + 1) - tmp.get(i));
        }
        ans += Math.min(comparison1, comparison2);
      }
    }
    System.out.println(ans);
  }
}
