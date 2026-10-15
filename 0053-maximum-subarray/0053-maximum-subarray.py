class Solution(object):
    def maxSubArray(self, nums):
        #kadanes algorithm
        maax=nums[0]
        count=nums[0]
        for i in range(1,len(nums)):
            count=max(nums[i],count+nums[i])
            maax=max(count,maax)
        return maax
        
        
        
        
        
        
        
        """maax=nums[0]
        i=0
        for i in range(len(nums)):
            j=i+1
            count=0
            for j in range(i,len(nums)):
                count+=nums[j]
                if count>maax:
                    maax=count
        return maax"""
     