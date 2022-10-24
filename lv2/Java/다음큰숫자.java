package lv2.Java;

public class 다음큰숫자 {
  public int countBin(String s, int n) {
		s = Integer.toBinaryString(n);
        int binCnt = 0;
        for (int i = 0; i < s.length(); i++) {
        	if(s.charAt(i) == '1') binCnt++;
		}
        return binCnt;
	}
	
    public int solution(int n) {
        String s = Integer.toBinaryString(n);
        int binCnt = countBin(s, n);
        
        while(true) {
        	s = Integer.toBinaryString(n++);
        	int comBinCnt = countBin(s, n);
        	if(binCnt == comBinCnt) return n;
        }
    }
}
