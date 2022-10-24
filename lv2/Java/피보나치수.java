package lv2.Java;

public class 피보나치수 {
  public static int solution(int n) {
      int dp[] = new int[n+1];
      dp[0] = 0; dp[1] = 1;
      for(int i=2; i<=n; i++) {
        dp[i] = dp[i-2] % 1234567 + dp[i-1] % 1234567;
      }
      
      return dp[n] % 1234567;
  }
  
  public static void main(String[] args) {
  System.out.println(solution(10000));
}
}
