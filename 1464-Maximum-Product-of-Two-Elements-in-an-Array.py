class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def heapify(nums, n, idx):
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != idx:
                nums[idx], nums[largest] = nums[largest], nums[idx]
                heapify(nums, n, largest)

        length = len(nums)
        for idx in range(length // 2 - 1, -1, -1):
            heapify(nums, length, idx)
        largest = nums[0]
        nums[0], nums[-1] = nums[-1], nums[0]
        heapify(nums, length - 1, 0)
        second_largest = nums[0]

        return (largest - 1) * (second_largest - 1)
