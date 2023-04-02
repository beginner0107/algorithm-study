import java.util.*;

class 여행경로 {
    public List<String> solution(String[][] tickets) {
        Map<String, List<String>> graph = new HashMap<>();
        for (String[] ticket : tickets) {
            String start = ticket[0];
            String end = ticket[1];
            if (graph.containsKey(start)) {
                graph.get(start).add(end);
            } else {
                List<String> destinations = new ArrayList<>();
                destinations.add(end);
                graph.put(start, destinations);
            }
        }

        for (List<String> destinations : graph.values()) {
            Collections.sort(destinations, Collections.reverseOrder());
        }

        List<String> answer = new ArrayList<>();
        Deque<String> stack = new ArrayDeque<>();
        stack.push("ICN");

        while (!stack.isEmpty()) {
            String node = stack.peek();
            if (!graph.containsKey(node) || graph.get(node).isEmpty()) {
                answer.add(stack.pop());
            } else {
                String next = graph.get(node).remove(graph.get(node).size() - 1);
                stack.push(next);
            }
        }

        Collections.reverse(answer);
        return answer;
    }
}
