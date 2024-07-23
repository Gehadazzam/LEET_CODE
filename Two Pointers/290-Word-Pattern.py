class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        patterns = {}
        hashWords = {}
        for p, w in zip(pattern, words):
            if p in patterns and patterns[p] != w:
                    return False
            elif w in hashWords and hashWords[w] != p:
                    return False
            patterns[p] = w
            hashWords[w] = p
        return True
