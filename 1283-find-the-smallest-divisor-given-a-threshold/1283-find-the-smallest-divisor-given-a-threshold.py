class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def ssum(divisor):
            total=0
            round=divisor-1
            for x in nums:
                total+=(x+round)//divisor
            return total
        
        left=(sum(nums)+(threshold-1))//threshold
        right=max(nums)
        while left<right:
            mid=(left+right)//2
            if ssum(mid)<=threshold:
                right=mid
            else:
                left=mid+1
        return left
        