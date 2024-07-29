class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        def reverse(arr, left, right):
            while (left < right):
                arr[left] ^= arr[right]
                arr[right] ^= arr[left]
                arr[left] ^= arr[right]
                left += 1
                right -= 1
        k = k % len(nums)
        reverse(nums,0, len(nums)-1)
        reverse(nums,0, k-1)
        reverse(nums,k, len(nums)-1)

