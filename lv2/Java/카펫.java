package lv2.Java;

public class 카펫 {
  class Pos{
		public int width;
		public int height;
		
		public Pos(int width, int height) {
			this.width = width;
			this.height = height;
		}
	}
	
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int total = brown + yellow;
        List<Pos> candidate = new ArrayList<>();
        
        for(int i=3; i<total+1; i++) {
        	if(total % i == 0) {
        		candidate.add(new Pos(i,total/i));
        		
        	}
        }
        
        for (Pos pos : candidate) {
			int width = pos.width; int height = pos.height;
			if((width + height) * 2 - 4  == brown) {
				if(width >= height) {
					answer[0] = width;
					answer[1] = height;
				}else {
					answer[0] = height;
					answer[1] = width;
				}
				
				break;
			}
		}
        
        return answer;
    }
}
