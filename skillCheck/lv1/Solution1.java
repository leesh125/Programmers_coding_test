package skillCheck.lv1;

import java.util.ArrayList;
import java.util.List;

public class Solution1 {
    static int[] p1 = {1, 2, 3, 4, 5};
    static int[] p2 = {2, 1, 2, 3, 2, 4, 2, 5};
    static int[] p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

    public int[] solution(int[] answers) {
        int[] answer = {0,0,0};
        List<Integer> res = new ArrayList<>();
        int max = -1;
        
        for(int i=0; i<answers.length; i++){
            if(answers[i] == p1[i%5]) answer[0]++;
            if(answers[i] == p2[i%8]) answer[1]++;
            if(answers[i] == p3[i%10]) answer[2]++;
        }
        for (int i = 0; i < 3; i++) {
            if(answer[i] > max) {
                max = answer[i];
                res.clear();
                res.add(i+1);
            }else if(answer[i] == max){
                res.add(i+1);
            }
        }
        int[] realAns = new int[res.size()];
        int idx = 0;
        for (Integer n : res) {
            realAns[idx++] = n;
        }
        return realAns;
    }
}
