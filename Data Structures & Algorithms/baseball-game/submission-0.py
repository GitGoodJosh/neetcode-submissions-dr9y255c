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
                print(stack)
            elif type(val) == str:
                val = val.upper()
                match val:
                    case "+":
                        print(sum(stack[-2:]))
                        stack.append(sum(stack[-2:]))
                        print(stack)
                    case "D":
                        stack.append(stack[-1]*2)
                        print(stack)
                    case "C":
                        stack = stack[0:-1]
                        print(stack)
        return sum(stack)
            

    