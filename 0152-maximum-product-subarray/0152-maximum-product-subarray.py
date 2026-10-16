class Solution(object):
    def maxProduct(self, nums):
        maax=nums[0]
        cmax=nums[0]
        cmin=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                cmax,cmin=cmin,cmax
            cmax=max(nums[i],cmax*nums[i])
            cmin=min(nums[i],cmin*nums[i])
            maax=max(maax,cmax)
        return maax