class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        
        for idx in range(len(haystack) - len(needle) + 1):
            if haystack[idx:idx+len(needle)] == needle:
                return idx
        return -1