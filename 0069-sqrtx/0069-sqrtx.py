class Solution(object):
    def mySqrt(self, x):
        if x<=1:
            return x
        left=0
        right=x
        while left<right:
            mid=(left+right)//2
            s=mid*mid
            if s==x:
                return mid
            elif s>x:
                right=mid
            else:
                left=mid+1
        return right-1

        