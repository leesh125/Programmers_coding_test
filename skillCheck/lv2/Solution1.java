package skillCheck.lv2;

import java.util.ArrayList;

class Solution1 {
    public String solution(String s) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        String[] temp = s.split(" ");
        for (int i = 0; i < temp.length; i++) {
            int num = Integer.parseInt(temp[i]);
            if(num < min) min = num;
            if(num > max) max = num;
        }
        sb.append(min);
        sb.append(" ");
        sb.append(max);
        
        return sb.toString();
    }
}
