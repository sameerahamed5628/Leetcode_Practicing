class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []
        nums.sort()
        m=(len(nums))/3
        maj=[]
        count=1
        i=0
        
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                count+=1
            else:
                if count>m:
                    maj.append(nums[i])
                count=1
            i+=1
        if count>m:
            maj.append(nums[len(nums)-1])
        return maj

