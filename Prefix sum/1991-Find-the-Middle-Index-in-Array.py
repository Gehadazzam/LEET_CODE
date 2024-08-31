class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        idxSum = 0
        for idx in range(len(nums)):
            sums = totalSum - idxSum -nums[idx]
            if (sums == idxSum):
                return idx
            idxSum += nums[idx]
        return -1
