class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for idx in range(len(arr) - 2):
            if arr[idx] % 2 != 0 and arr[idx+1] % 2 != 0 and arr[idx+2] % 2 != 0:
                return True
        return False
