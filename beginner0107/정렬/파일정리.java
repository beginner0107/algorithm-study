import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class 파일정리 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<File> fileList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String fileName = sc.next();
            String fileExtension = fileName.substring(fileName.lastIndexOf(".") + 1);
            fileList.add(new File(fileExtension));
        }
        Collections.sort(fileList);
        Map<String, Integer> fileCountMap = new LinkedHashMap<>();
        for (File file : fileList) {
            fileCountMap.put(file.getExtension(), fileCountMap.getOrDefault(file.getExtension(), 0) + 1);
        }
        for (Map.Entry<String, Integer> entry : fileCountMap.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }

    static class File implements Comparable<File> {
        private final String extension;

        public File(String extension) {
            this.extension = extension;
        }

        public String getExtension() {
            return extension;
        }

        @Override
        public int compareTo(File o) {
            return extension.compareTo(o.extension);
        }
    }
}