class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        timercount = time % (2 * n - 2)
        if timercount < n:
            return timercount + 1
        else:
            return 2 * n - timercount - 1