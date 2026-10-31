class Solution(object):
    def subtractProductAndSum(self, n):
        ssum=0
        prod=1
        while n>0:
            ssum+=n%10
            prod*=n%10
            n=n//10
        return prod-ssum