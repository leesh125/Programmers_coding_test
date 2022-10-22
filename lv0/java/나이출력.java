package lv0.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 나이출력 {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ;

    public static int solution(int age) {
        return 2022 - age + 1;
    }

    public static void main(String[] args) {
        System.out.println(solution(40));
    }
}
