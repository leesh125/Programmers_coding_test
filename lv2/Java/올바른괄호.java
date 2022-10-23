package lv2.Java;

import java.util.Stack;

public class 올바른괄호 {
    boolean solution(String s) {
        Stack<Integer> stack = new Stack<>();
        if(s.charAt(0) == ')' || s.charAt(s.length()-1) == '(') return false;

        stack.push(1);
        for (int i = 1; i < s.length(); i++) {
            if(s.charAt(i) == '(') stack.push(1);
            else{
                if(stack.size() == 0) return false;
                if(stack.pop() != 1) return false;
            }
        }
        if(stack.size() == 0) return true;
        else return false;

    }
}
