class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, greater, pivots = [], [], []
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                pivots.append(num)
        return smaller + pivots + greater