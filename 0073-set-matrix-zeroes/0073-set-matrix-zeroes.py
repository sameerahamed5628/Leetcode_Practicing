class Solution(object):
    def setZeroes(self, matrix):
        zerow=[]
        zecol=[]
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                if matrix[i][j]==0:
                    zerow.append(i)
                    zecol.append(j)
        for i in zerow:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for j in zecol:
            for i in range(len(matrix)):
                matrix[i][j]=0
            
        
    """   i=0
        j=0
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                    if matrix[i][j]==0:
                        change=0
                        for change in range(len(matrix)):
                            matrix[change][j]=0
                            change+=1
        row=0
        for row in range (len(matrix)):
            if matrix[row][row]==0:
                k=0
                while k<len(matrix[0]):
                    matrix[row][k]=0
                    k+=1"""
                
                    
            