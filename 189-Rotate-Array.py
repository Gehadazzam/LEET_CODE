class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        length = len(nums)
        k %= length
        reverse(nums, 0, length - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, length - 1)