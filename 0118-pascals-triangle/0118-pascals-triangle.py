class Solution(object):
    def generate(self, numRows):
        pascal=[[None]*(index+1) for index in range(numRows)]
        i=0
        while i<numRows:
            pascal[i][0]=1
            j=1
            while j<i:
                pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
                j+=1
            pascal[i][i]=1
            i+=1
        return pascal