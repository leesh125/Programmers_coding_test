package lv2.Java;

public class TakeGroupPhoto {
    static String[] names = {"A", "C", "F", "J", "M", "N", "R", "T"}; // 프렌즈들
    static boolean[] visited = new boolean[8]; // 방문 표시(경우의 수 모두 표시하기 위해)
    static int depth = 0; // 깊이 == 문자열 길이(최대면 거기서 비교)
    static int answer = 0;
    static String datas[];

    public static void main(String[] args){
        String[] ex = {"N~F=0", "R~T>2"};
        solution(2, ex);
    }

    public static int solution(int n, String[] data) {
        datas = data; 
        answer = 0;
        DFS(""); // 빈 문자열 부터 시작
        return answer;
    }

    public static void DFS(String lines){ // DFS 탐색
        if(depth == 8){ // 문자열 길이가 8이면
            if(check(lines)){ // 조건에 맞는지 확인
                answer++; // 맞으면 answer++
            }
            return; // 더 이상 비교 X
        }

        for(int i=0; i<8; i++){ // 첫번째 ~ 마지막 프렌즈 모두 탐색
            if(!visited[i]){ // 방문하지 않은 프렌드라면
                depth++; // 깊이 == 길이 +=1
                visited[i] = true; // 방문 처리
                DFS(lines + (names[i])); // 해당 프렌즈를 문자열에 추가 시키고 재귀
                visited[i] = false; // 문자열 길이 8을 만들고 나선 false로
                depth--; // 깊이 == 길이 -= 1
            }
        }
    }

    public static boolean check(String lines) { // 조건에 맞는지 확인하는 함수
        for(int i=0; i<datas.length; i++){ // 있는 data들 모두 탐색
            int n = lines.indexOf(datas[i].charAt(0)+""); // charAt(int index) = 문자, indexOf("문자열") = 정수
            int m = lines.indexOf(datas[i].charAt(2)+""); // 프렌즈들
            int dist = Math.abs(n-m)-1; // 둘 사이 거리(붙어있으면 0)
            if(datas[i].charAt(3) == '=' && dist != datas[i].charAt(4)-'0'){ // '문자' -'0' = 정수로 변환(아스키 코드)
                return false; // 둘 사이 거리가 0이 아니면
            }else if(datas[i].charAt(3) == '>' && dist <= datas[i].charAt(4)-'0'){
                return false; // 둘 사이 거리가 일정 수 이상이 아니면
            }else if(datas[i].charAt(3) == '<' && dist >= datas[i].charAt(4)-'0'){
                return false; // 둘 사이 거리가 일정 수 이하가 아니면
            }
        }

        return true; // 조건에 맞으면 true
    }
}
// {A, C, F, J, M, N, R, T}