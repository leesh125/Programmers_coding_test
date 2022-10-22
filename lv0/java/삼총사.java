package lv0.java;

public class 삼총사 {
    public static int solution(int[] number) {
        int answer = 0;
        int length = number.length;
        for(int i=0; i<length-2; i++){
            for(int j=i+1; j<length-1; j++){
                for(int k=j+1; k<length; k++){
                    if(number[i] + number[j] + number[k] == 0) answer++;
                }
            }
        }
        
        return answer;
    }

    public static void main(String[] args) {
        int[] arr = {-2,3,0,2,-5};
        System.out.println(solution(arr));
    }

}
