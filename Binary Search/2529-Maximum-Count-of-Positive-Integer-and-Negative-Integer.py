class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        left, right = 0, len(nums) - 1
        posCount, negCount = 0, 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                negCount = mid + 1
                left = mid + 1
            elif nums[mid] > 0:
                posCount = len(nums) - mid
                right = mid - 1   
            else:
                if nums[left] < 0:
                    negCount  +=1
                left+=1
        return max(posCount, negCount)