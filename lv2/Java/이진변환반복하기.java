package lv2.Java;

public class 이진변환반복하기 {
  static String temp,binary;
  static int temp_one_cnt,temp_zero_cnt,oneCnt,zeroCnt,cnt;
  
  public static int[] solution(String s) {
    int[] answer = new int[2];
    
    while(true){
      cnt++;
      temp_one_cnt = 0; temp_zero_cnt=0;
      
      for (int i = 0; i < s.length(); i++) {
        if(s.charAt(i) == '1') temp_one_cnt++;
        else temp_zero_cnt++;
      }
      oneCnt += temp_one_cnt;
      zeroCnt += temp_zero_cnt;
      temp = Integer.toBinaryString(temp_one_cnt);
      
      System.out.println(temp);
      if(temp.equals("1")) break;
      s = temp;  
    }
    answer[0] = cnt; answer[1] = zeroCnt;
    return answer;
  }
  
  public static void main(String[] args) {
	 System.out.println(solution("1111111"));
  }
}
