class 연속펄스부분수열의합 {
    public long solution(int[] sequence) {
        long answer = Long.MIN_VALUE;
        
        long s1 = 0;
        long s2 = 0;
        
        int palse = 1;
        long s1_min = 0;
        long s2_min = 0;
        for (int i = 0; i < sequence.length; i++) {
            s1 += sequence[i] * palse;
            s2 += sequence[i] * -palse;
            
            answer = Math.max(Math.max(answer, s1 - s1_min), s2 - s2_min);
            
            s1_min = Math.min(s1, s1_min);
            s2_min = Math.min(s2, s2_min);
            
            palse *= -1;
        }
        return answer;
    }
}