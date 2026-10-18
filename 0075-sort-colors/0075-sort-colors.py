class Solution(object):
    def sortColors(self, nums):
        red=0 
        white=0
        blue=0
        for color in nums:
            if color==0:
                red+=1
            elif color==1:
                white+=1
            else:
                blue+=1
        for i in range(len(nums)):
            if i<red:
                nums[i]=0
            elif i<red+white:
                nums[i]=1
            else:
                nums[i]=2         
            

        