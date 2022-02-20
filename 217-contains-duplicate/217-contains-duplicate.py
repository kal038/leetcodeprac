class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                return True
        return False
        