class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        else:
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid-1]<target<nums[mid]:
                    return mid
                if nums[mid]>target:
                    right=mid-1
                    
                if nums[mid]<target:
                    left=mid+1
            else:
                if target>nums[right]:
                    return right+1
                elif target<nums[left]:
                    return left
                    
        