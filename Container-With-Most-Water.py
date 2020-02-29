class Solution:
    def maxArea(self, height: List[int]) -> int:
        slow=0
        fast=len(height)-1
        max_area = -float('inf')
        area=1
        #Edge case
        if not height:
            return None
        #Base case
        while slow<fast:
            #Calculate maximum area of rectangle(height*width between two indices)
            max_area=max((fast-slow)*min(height[fast],height[slow]),max_area)
            print(max_area)
            if height[fast]>height[slow]:
                slow+=1
            else:
                fast-=1
        return max_area
    
            
            
            
            
            
        