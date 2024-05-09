class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0

        for idx, h in enumerate(happiness):
            if k == idx:
                return total
            total += max(0, h - idx)

        return total
