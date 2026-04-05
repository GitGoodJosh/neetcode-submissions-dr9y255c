class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key2 =" ({[]})"
        for i in s:
            if i in key2[1:4]:
                stack.append(i)
            else:
                if len(stack)>0 and key2[-key2.find(stack[-1])] == i:
                    stack = stack[0:-1]
                else:
                    return False
        if len(stack)>0:
            return False        
        return True
                
