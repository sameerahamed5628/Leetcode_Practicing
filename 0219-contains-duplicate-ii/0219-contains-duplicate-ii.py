class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        slider=set()
        for i in range(len(nums)):
            if nums[i] in slider:
                return True
            slider.add(nums[i])
            if len(slider)>k:
                slider.remove(nums[i-k])
        return False