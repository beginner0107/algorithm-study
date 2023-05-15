import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class 불량사용자 {
    private Set<Set<String>> resultSet = new HashSet<>();

    public int solution(String[] user_id, String[] banned_id) {
        boolean[] visited = new boolean[user_id.length];
        List<String> selected = new ArrayList<>();
        dfs(user_id, banned_id, visited, selected);

        return resultSet.size();
    }

    private void dfs(String[] user_id, String[] banned_id, boolean[] visited, List<String> selected) {
        if (selected.size() == banned_id.length) {
            if (isBanned(selected, banned_id)) {
                resultSet.add(new HashSet<>(selected));
            }
            return;
        }

        for (int i = 0; i < user_id.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                selected.add(user_id[i]);
                dfs(user_id, banned_id, visited, selected);
                selected.remove(selected.size() - 1);
                visited[i] = false;
            }
        }
    }

    private boolean isBanned(List<String> selected, String[] banned_id) {
        for (int i = 0; i < selected.size(); i++) {
            String user = selected.get(i);
            String banned = banned_id[i];
            if (user.length() != banned.length()) {
                return false;
            }
            for (int j = 0; j < user.length(); j++) {
                if (banned.charAt(j) != '*' && banned.charAt(j) != user.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }
}