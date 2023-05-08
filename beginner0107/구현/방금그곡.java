import java.util.ArrayList;
import java.util.List;

class 방금그곡 {
    public String solution(String m, String[] musicinfos) {
        List<Music> matchedMusics = new ArrayList<>();
        String target = convertSharp(m);
        for (String musicinfo : musicinfos) {
            String[] info = musicinfo.split(",");
            String title = info[2];
            String sheet = convertSharp(info[3]);
            int start = toMinutes(info[0]);
            int end = toMinutes(info[1]);
            int playtime = end - start;
            String played = generatePlayedSheet(sheet, playtime);
            if (played.contains(target)) {
                matchedMusics.add(new Music(title, playtime));
            }
        }
        if (matchedMusics.isEmpty()) {
            return "(None)";
        }
        matchedMusics.sort((m1, m2) -> m2.playtime - m1.playtime);
        return matchedMusics.get(0).title;
    }

    private String convertSharp(String sheet) {
        return sheet.replace("C#", "c").replace("D#", "d")
                .replace("F#", "f").replace("G#", "g")
                .replace("A#", "a");
    }

    private int toMinutes(String time) {
        String[] hm = time.split(":");
        int hour = Integer.parseInt(hm[0]);
        int minute = Integer.parseInt(hm[1]);
        return hour * 60 + minute;
    }

    private String generatePlayedSheet(String sheet, int playtime) {
        int len = sheet.length();
        StringBuilder played = new StringBuilder();
        for (int i = 0; i < playtime; i++) {
            played.append(sheet.charAt(i % len));
        }
        return played.toString();
    }

    private static class Music {
        String title;
        int playtime;

        public Music(String title, int playtime) {
            this.title = title;
            this.playtime = playtime;
        }
    }
}