class Solution: 
    def isValid(self, s: str) ->bool: 
        stack=[] 
        for idx in range(0,len(s)): 
            if (s[idx]==\(\ or s[idx]==\{\ or s[idx]==\[\): 
                stack.append(s[idx])
            elif (s[idx]==\)\ and stack and stack[-1] == \(\):
                stack.pop()
            elif (s[idx]==\}\ and stack and stack[-1]==\{\):
                stack.pop()
            elif (s[idx]==\]\ and stack and stack[-1]==\[\):
                stack.pop()
            else:
                return False
        return (len(stack)==0)