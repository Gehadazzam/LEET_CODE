class Solution:
    def minOperations(self, logs: List[str]) -> int:
        foldersStack = []
        for log in logs:
            if (log == "../"):
                if foldersStack:
                    foldersStack.pop()
            elif (log == "./"):
                continue
            else:
                foldersStack.append(log)
        return len(foldersStack)