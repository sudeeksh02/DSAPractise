//no. of islands
/*
class Solution {
public:
    int directions[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
    int numIslands(vector<vector<char>>& grid) {
        int islands=0;
        int row=grid.size(),col=grid[0].size();
        for(int r=0;r<row;r++){
            for(int c=0;c<col;c++){
                if(grid[r][c]=='1'){
                    islands++;
                    dfs(grid,r,c);
                }
            }
        }return islands;
    }

    void dfs(vector<vector<char>>& grid,int r,int c){
        if (r<0 || c<0 || r>=grid.size() || c>=grid[0].size() || grid[r][c]=='0'){
            return;
        }
        grid[r][c]='0';
        for(int i=0;i<4;i++){
            dfs(grid,r+directions[i][0],c+directions[i][1]);
        }
    }
};
*/

