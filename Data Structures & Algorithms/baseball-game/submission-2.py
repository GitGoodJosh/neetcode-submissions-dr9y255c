class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            #print(operations[i])
            try:
                val = int(operations[i])
            except: 
                val = str(operations[i])
            if type(val) == int:
                stack.append(val)
            elif type(val) == str:
                val = val.upper()
                match val:
                    case "+":
                        stack.append(sum(stack[-2:]))
                    case "D":
                        stack.append(stack[-1]*2)
                    case "C":
                        stack.pop()

        return sum(stack)