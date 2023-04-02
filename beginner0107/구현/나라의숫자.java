class 나라의숫자 {
    public String solution(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            int mod = (n - 1) % 3;
            sb.insert(0, "124".charAt(mod));
            n = (n - 1) / 3;
        }
        return sb.toString();
    }
}