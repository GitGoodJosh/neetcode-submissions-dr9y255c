class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keydict = { "]":"[",
                    ")":"(",
                    "}":"{"}
        for i in s:
            if i not in keydict:
                stack.append(i)
            else:
                if len(stack)>0 and keydict.get(i) == stack[-1]:
                    stack = stack[0:-1]
                else:
                    return False    
        return stack == []