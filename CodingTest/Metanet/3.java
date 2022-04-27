package Programmers_coding_test.CodingTest.Metanet;

class Solution {
    public String solution(String vote) {
        int a_cnt = 0;
        int b_cnt = 0;
        int c_cnt = 0;
        
        for(int i=0; i<vote.length(); i++){
            if (vote.charAt(i) == 'A'){
                a_cnt += 1;
            } else if (vote.charAt(i) == 'B'){
                b_cnt += 1;
            } else{
                c_cnt += 1;
            }
            
            if(c_cnt >= vote.length()/2){
                return "C";
            }
        }

        String answer = (a_cnt == b_cnt) ? "AB" : (a_cnt < b_cnt) ? "B" : "A";
        return answer;
    }
}