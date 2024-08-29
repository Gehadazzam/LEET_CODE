class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        res = []
        for i in range(1, n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]
        for i in range(n):
            res.append(abs(leftSum[i] - rightSum[i]))
        return res