class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bk(start, idx):
            res.append(idx)
            for i in range(start, len(nums)):
                bk(i + 1, idx + [nums[i]])
        bk(0, [])
        return res
