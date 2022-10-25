package lv2.Java;
import java.util.HashMap;
public class 영어끝말잇기 {
  public static int[] solution(int n, String[] words) {
    int[] answer = new int[2];
    char prev = ' ';
    boolean flag = false;
    HashMap<String, Boolean> map = new HashMap<>();
    int idx = 0, time = 1;
    
    for (String word : words) {
      
      if(prev != ' ' && prev != word.charAt(0)) {
        flag = true;
        break;
      }
      if(map.containsKey(word) || word.length() == 1) {
        flag = true;
        break;
      }
      time++;
      idx = (idx + 1) % n;
      prev = word.charAt(word.length()-1);
      map.put(word, true);
}
    if(flag) {
      answer[0] = idx+1; answer[1] = (time-1)/n + 1;
        return answer;
    }else {
        return answer;
    }
}

public static void main(String[] args) {
  
int[] ans = solution(3, new String[] {"tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"});
System.out.println(ans[0] + " " + ans[1]);
}
}
