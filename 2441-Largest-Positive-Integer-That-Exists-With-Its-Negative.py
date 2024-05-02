class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        unique = set(nums)
        maximum = 0
        for num in nums:
            if -num in unique:
                maximum = max(maximum, num)
        return maximum if maximum > 0 else -1