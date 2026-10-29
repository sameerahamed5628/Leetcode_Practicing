class Solution(object):
    def fourSum(self, nums, target):
        ans=[]
        nums.sort()
        i=0
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=len(nums)-1
                while left<right:
                    add=nums[i]+nums[j]+nums[left]+nums[right]
                    if add==target:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif add<target:
                        left+=1
                    else:
                        right-=1
        return ans      

