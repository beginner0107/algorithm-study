import java.util.*;
/*
무지 -> 파일 저장소 서버 관리

파일을 이름 순으로 정렬하면 나중에 만들어진 ver-10.zip이 ver-9.zip보다 먼저 표시되기 때문

버전 번호 외에도 숫자가 포함된 파일목록은 관리하기 불편

단순한 문자 코드 순 X
파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현하기로 함

소스파일 저장소에 저장된 파일면 100글자 이내

영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있음

파일명은 영문자로 시작하며, 숫자 하나이상 포함

파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성

- HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
- NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 
  앞쪽에 0이 올 수 있다. 0부터 99999사이의 숫자로, 00000이나 0101등도 가능하다
- TAIL은 그 나머지 부분으로 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다

파일명을 세 부분으로 나눈 후, 다음 기준에 따라 파일을 정렬

- 파일명은 HEAD 부분을 기준으로 사전 순으로 정렬
   문자열 비교 시 대소문자 구분을 하지 않는다

- 파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬
  9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬
  숫자 앞의 0은 무시, 012 == 12

- 두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지
  MUZI01.zip, muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서 바뀌면 안 됨

무지를 도와 파일명 정렬 프로그램을 구현하라
 */
public class 파일명정렬 {
    public ArrayList<String> solution(String[] files) {
        ArrayList<String> answer = new ArrayList<>();
        List<File> fileList = new ArrayList<>();
        for (String file : files) { // O(N)
            fileList.add(new File(file));
        }
        Collections.sort(fileList, new FileComparator()); // O(N)
        for (File f : fileList) { // O(N)
            answer.add(f.getFileName());
        }
        return answer; 
    }
}

class File {
    private Map<Character, Integer> num
            = Map.of('0', 0,'1', 0,'2', 0,'3', 0,'4',
            0,'5', 0,'6', 0,'7', 0,'8', 0,'9', 0);
    private String filename;
    private String head;
    private int number;
    private String tail;

    public File(String filename) {
        this.filename = filename;
        int headIndex = -1;
        int numberIndex = filename.length();
        boolean isStart = false;
        for (int i = 0; i < filename.length(); i ++ ) {
            if (num.containsKey(filename.charAt(i)) && !isStart) {
                headIndex = i;
                isStart = true;
            }
            else if(!num.containsKey(filename.charAt(i)) && isStart) {
                numberIndex = i;
                break;
            }
        }
        this.head = filename.substring(0, headIndex).toUpperCase();
        this.number = Integer.parseInt(filename.substring(headIndex, numberIndex));
        this.tail = filename.substring(numberIndex);
    }

    public String getHead() {
        return head;
    }

    public int getNumber() {
        return number;
    }

    public String getFileName() {
        return filename;
    }
}

class FileComparator implements Comparator<File> {
    @Override
    public int compare(File o1, File o2) {
        if (o1.getHead().compareTo(o2.getHead()) > 0) {
            return 1;
        }
        else if(o1.getHead().compareTo(o2.getHead()) < 0) {
            return -1;
        }
        else {
            return Integer.compare(o1.getNumber(), o2.getNumber());
        }
    }
}