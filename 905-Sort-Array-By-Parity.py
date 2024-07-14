class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def iseven(num):
            return num %2 == 0
        left, right = 0, len(nums) - 1
        while (left <= right):
            if (iseven(nums[left])):
                left += 1
            elif (not iseven(nums[left]) and iseven(nums[right])):
                nums[left], nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
            else:
                right -= 1
        return nums