public class 기지국 {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int location = 1;

        for (int i = 0; i < stations.length; i++) {
            int left = stations[i] - w; 
            int right = stations[i] + w; 

            if (location < left) {
                int distance = left - location; 
                answer += getRequiredStations(distance, w);
            }

            location = right + 1;
        }


        if (location <= n) {
            int distance = n - location + 1; 
            answer += getRequiredStations(distance, w);
        }

        return answer;
    }

    private int getRequiredStations(int distance, int w) {
        int requiredStations = distance / (2 * w + 1); 
        if (distance % (2 * w + 1) != 0) {
            requiredStations++; 
        }
        return requiredStations;
    }
}
