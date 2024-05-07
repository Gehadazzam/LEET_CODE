class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = "aAeEoOuUiI"
        for char in s[:min(k, len(s))]:
            if char in vowels:
                count += 1
        maximum = count
        for idx in range(k, len(s)):
            if s[idx] in vowels:
                count += 1
            if s[idx - k] in vowels:
                count -= 1
            maximum = max(maximum, count)
        return maximum
