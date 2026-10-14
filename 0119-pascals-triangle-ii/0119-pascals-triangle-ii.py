class Solution(object):
    def getRow(self, rowIndex):
        pascal=[[None]*(index+1) for index in range(rowIndex+1)]
        i=0
        while i<rowIndex+1:
            pascal[i][0]=1
            j=1
            while j<i:
                pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
                j+=1
            pascal[i][i]=1
            i+=1
        n=rowIndex
        return pascal[n]