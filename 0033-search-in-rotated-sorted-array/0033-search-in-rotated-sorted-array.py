class Solution(object):
    def search(self, nums, target):
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]== target:
                return mid
            elif nums[left]==target:
                return left
            elif nums[right]==target:
                return right
            else:
                left+=1
                right-=1
        return -1
