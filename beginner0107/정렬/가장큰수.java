import java.util.Arrays;

public class 가장큰수 {
    public String solution(int[] numbers) {
        String answer = "";
        String[] nums = new String[numbers.length];
        for (int i = 0; i < nums.length; i ++) {
            nums[i] = String.valueOf(numbers[i]);
        }
        Arrays.sort(nums, (a, b) -> (b + 1).compareTo(a + b));

        return answer;
    }
}
