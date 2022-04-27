package Programmers_coding_test.CodingTest.Metanet;

class Solution {
    public int[] solution(int day, int k) {
        int[] answer = new int[12];

        int[] months = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int sum_months = 0;
        int cur_day = 0;

        for (int i=0; i<= months.length; i++){
            if (i != 0) {
                sum_months += months[i-1];
            }else{
                sum_months = day + k -1;
            }

            cur_day = sum_months % 7;

            if(cur_day == 5 || cur_day == 6){
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }

        return answer;
    }
}