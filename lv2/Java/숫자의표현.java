package lv2.Java;

class Solution {
    public int solution(int n) {
        int answer = 1;
        
        for(int i=1; i<=n/2; i++) {
        	int temp = i;
        	int total = 0;
        	while(true) {
        		total += temp++;
        		if(total == n) {
        			answer++;
        			break;
        		}
        		if(total > n) break;
        	}
        }
        
        return answer;
    }
}

