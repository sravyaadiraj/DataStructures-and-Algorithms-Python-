#Flood Fill Using BFS
#Time and Space complexity - O(m*n)


from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #Base Case
        if image[sr][sc]== newColor:
            return image
        
        
        row=len(image)
        col=len(image[0])
        q= deque([[sr,sc]])
        #Declaring Directions Array
        direct_array=[[1,0],[-1,0],[0,1],[0,-1]]
        color=image[sr][sc]
        while len(q):
            x,y=q.pop()
            image[x][y]=newColor
            for dirc in direct_array:
                new_x,new_y=x+ dirc[0],y+dirc[1]
                if 0<=new_x<row and 0<=new_y<col and image[new_x][new_y]==color:
                    q.append([new_x,new_y])
        return image
                
            
        
        
        
        
        
        
        