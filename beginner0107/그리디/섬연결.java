import java.util.*;
class 섬연결 {
  public int solution(int n, int[][] costs) {
    int answer = 0;
    // 각 노드의 부모 노드를 자기 자신으로 초기화
    int[] parent = new int[n];
    for (int i = 0; i < n; i++) {
      parent[i] = i;
    }
    // 비용에 따라 간선을 오름차순으로 정렬
    Arrays.sort(costs, Comparator.comparingInt(a -> a[2]));
    // 모든 간선에 대해 노드를 연결
    for (int[] cost : costs) {
      int from = cost[0]; // 간선의 시작 노드
      int to = cost[1]; // 간선의 끝 노드
      int costVal = cost[2]; // 간선의 비용

      // 두 노드의 부모 노드를 찾음
      int fromParent = find(parent, from);
      int toParent = find(parent, to);

      // 두 노드가 같은 집합에 속해 있지 않으면 연결
      if (fromParent != toParent) {
        parent[fromParent] = toParent; // from의 부모를 to로 변경
        answer += costVal; // 비용을 누적
      }
      System.out.println(Arrays.toString(parent));
    }

    return answer;
  }

  public int find(int[] parent, int node) {
    // 부모 노드가 자기 자신이 아니면 부모 노드를 찾음
    if (parent[node] != node) {
      parent[node] = find(parent, parent[node]); // 부모 노드를 갱신
    }
    return parent[node]; // 최종 부모 노드를 반환
  }
}