class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def is_palindrome(s):
            return s == s[::-1]
        
        def bk(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    bk(i + 1, path)
                    path.pop()
        
        bk(0, [])
        return res
