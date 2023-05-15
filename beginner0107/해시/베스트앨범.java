import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class 베스트앨범 {
  public ArrayList<Integer> solution(String[] genres, int[] plays) {
    ArrayList<Integer> answer = new ArrayList<>();

    // 고유 번호를 저장
    int[] pk = new int[genres.length + 1];
    for (int i = 0; i <= genres.length; i++) {
      pk[i] = i;
    }

    Map<String, Integer> map = new HashMap<>();
    for (int i = 0; i < genres.length; i++) {
      map.put(genres[i], map.getOrDefault(genres[i], 0) + plays[i]);
    }
    List<Entry<String, Integer>> entryList = new LinkedList<>(map.entrySet());
    entryList.sort((o1, o2) -> o2.getValue() - o1.getValue());
    ArrayList<List<Music>> an = new ArrayList<>();
    for(Map.Entry<String, Integer> entry : entryList){
      List<Music> li = new ArrayList<>();
      for (int i = 0; i < genres.length; i++) {
        if (genres[i].equals(entry.getKey())) {
          li.add(new Music(pk[i + 1], genres[i], plays[i], i));
        }
      }
      an.add(li);
    }
    for (List<Music> music : an) {
      music.sort((o1, o2) -> {
        if (o1.play != o2.play) {
          return o2.play - o1.play;
        } else {
          return o1.id - o2.id;
        }
      });
      for (int i = 0; i < music.size(); i++) {
        if (i <= 1) {
          answer.add(music.get(i).location);
        }
      }
    }
    return answer;
  }
  public static class Music {
    int id;
    String genre;
    int play;
    int location;

    public Music(int id, String genre, int play, int location) {
      this.id = id;
      this.genre = genre;
      this.play = play;
      this.location = location;
    }
  }
}


