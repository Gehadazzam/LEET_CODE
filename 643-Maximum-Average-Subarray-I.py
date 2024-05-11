class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maximum = total
        for idx in range(k, len(nums)):
            total += nums[idx] - nums[idx - k]
            maximum = max(maximum, total)
        return maximum / k