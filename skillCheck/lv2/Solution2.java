package skillCheck.lv2;

import java.util.LinkedList;
import java.util.Queue;

class Solution2 {
    public static int[] dx = {-1,1,0,0};
    public static int[] dy = {0,0,-1,1};

    public boolean bfs(String[] graph,int i, int j){
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[5][5];
        visited[i][j] = true;
        q.add(new int[] {i,j,0,0});

        while(!q.isEmpty()){
            int[] arr = q.poll();
            int x = arr[0];
            int y = arr[1];
            int cnt = arr[2];
            int p = arr[3];
            
            if(cnt == 2) continue;

            for(int d=0; d<4; d++){
                int nx = x + dx[d];
                int ny = y + dy[d];

                if(0 > nx || nx >= 5 || 0 > ny || ny >= 5 || visited[nx][ny]) continue;
                
                if(graph[nx].charAt(ny) == 'X'){
                    q.offer(new int[] {nx,ny,cnt+1,1});
                    visited[nx][ny] = true;
                }else if(graph[nx].charAt(ny) == 'P'){
                    if(p == 0){
                        return true;
                    }
                }else{
                    q.offer(new int[] {nx,ny,cnt+1,p});
                    visited[nx][ny] = true;
                }
            }
        }

        return false;
    }

    public int[] solution(String[][] places) {
        int[] ans = new int[places.length];
        int idx = 0;
        boolean flag;
        for (String[] place : places) {
            flag = false;
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if(place[i].charAt(j) == 'P'){
                        if(bfs(place,i,j)){
                            flag = true;
                            System.out.println(i + " " + j);
                            break;    
                        }
                    }
                }
                if(flag) break;
            }
            if(flag) ans[idx++] = 0;
            else ans[idx++] = 1;
        }

        return ans;
    }
}