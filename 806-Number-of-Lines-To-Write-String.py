class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, width = 1, 0
        for char in s:
            difWidth = widths[ord(char) - ord('a')]
            if width + difWidth > 100:
                lines += 1
                width = difWidth
            else:
                width += difWidth
        return [lines, width]