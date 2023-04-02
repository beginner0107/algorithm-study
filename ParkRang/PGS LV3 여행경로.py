'''
import java.util.*;
class Solution {
    static boolean used[];
    static List<String> A;
    public String[] solution(String[][] tickets) {
        used = new boolean[tickets.length];
        String[] answer = {};
        A = new ArrayList<>();
        DFS("ICN", "ICN", tickets, 0);
        Collections.sort(A);
        answer = A.get(0).split(" ");
        return answer;
    }
    
    public static void DFS(String start, String end, String[]
                          []tickets, int n){
        if(n==tickets.length){
            A.add(end);
            return;
        }
        for(int i = 0; i<tickets.length; i++){
            if(!used[i]&&start.equals(tickets[i][0])){
                used[i]=true;
                DFS(tickets[i][1], end + " " + tickets[i][1],
                   tickets,n+1);
                used[i] = false;
            }
        }
            
    }
}
'''

def solution(tickets) :
    used = [False for _ in range(len(tickets))]
    A = []

    # DFS
    def DFS(start, end, tickets, n) :
        # 1. 종료 조건
        if n == len(tickets) :
            A.append(end)
            return
        # 2. 수행 동작
        for i in range(len(tickets)) :
            if not used[i] and start == tickets[i][0] :
                used[i] = True
                DFS(tickets[i][1], end + ' ' + tickets[i][1],
                    tickets, n+1)
                used[i] = False
    # DFS를 ICN에서 시작, ICN으로 종료
    DFS('ICN', 'ICN', tickets, 0)
    A.sort()
    return A[0].split(' ')
