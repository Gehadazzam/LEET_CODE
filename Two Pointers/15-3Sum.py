class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums)):
            if idx != 0 and nums[idx] == nums[idx-1]:
                continue
            left, right = idx+1, len(nums)-1
            while left < right:
                calSum = nums[idx] + nums[left] + nums[right]
                if calSum < 0:
                    left += 1
                elif calSum > 0:
                    right -= 1
                else:
                    a = [nums[idx], nums[left], nums[right]]
                    res.append(a)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res