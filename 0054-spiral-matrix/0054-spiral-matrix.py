class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        # matrix[row][col]
        top = 0 
        bottom = m-1
        left = 0
        right = n-1
        ans = []
        while top<=bottom and left<=right:
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            top+=1
            if top>bottom:
                continue
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            if right<left:
                continue
        
            for k in range(right,left-1,-1):
                ans.append(matrix[bottom][k])
            bottom-=1
        
            for l in range(bottom,top-1,-1):
                ans.append(matrix[l][left])
            left+=1
        return ans