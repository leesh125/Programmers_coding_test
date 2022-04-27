package Programmers_coding_test.CodingTest.Metanet;

import java.util.*;

class Solution {
    public static int[] solution(int[] waiting) {
        HashMap<Integer,Integer> map = new HashMap<>();
        List<Integer> answer = new ArrayList<Integer>();

        for(int i=0; i<waiting.length;i++){
            if (map.containsKey(waiting[i])){
                continue;
            }else{
                map.put(waiting[i], 1);
                answer.add(waiting[i]);
            }
        }
        int[] arr = new int[answer.size()];
        for(int i=0; i<answer.size();i++){
            arr[i] = answer.get(i);
        } 
        return arr;
    }

}

