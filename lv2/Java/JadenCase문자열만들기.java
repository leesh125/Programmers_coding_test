package lv2.Java;

public class JadenCase문자열만들기 {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        String[] temp = s.split(" ");
        for (String string : temp) {
            System.out.println(string);
        }
        for (int i = 0; i < temp.length; i++) {
            if(temp[i].length() == 0){
                sb.append(" ");
                continue;
            }
            sb.append(String.valueOf(temp[i].charAt(0)).toUpperCase());
            for(int j=1; j<temp[i].length(); j++){
                sb.append(String.valueOf(temp[i].charAt(j)).toLowerCase());
            }
            if(i < temp.length-1){
                sb.append(" ");
            }
        }
        if(s.charAt(s.length()-1) == ' '){
            sb.append(" ");
        }
        return sb.toString();
    }
}
