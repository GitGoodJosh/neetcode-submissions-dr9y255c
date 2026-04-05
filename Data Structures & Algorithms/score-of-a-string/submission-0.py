class Solution:
    def scoreOfString(self, s: str) -> int:
        revStr = s[::-1]
        print(revStr)

        def AcsciValue(input : str):
            value = ord(str(input).lower())
            #print(f"{input} , {value}")
            return value


        ### o - c , d - o, e - d
        ### e - d, d - o, o - c

        pairedValue = []
        Result = 0
        for chars in revStr:
            print(pairedValue)
            print(AcsciValue(chars))
            if len(pairedValue) < 2:
               pairedValue.append(AcsciValue(chars))
               
            if len(pairedValue) == 2:
                score = abs(pairedValue[0] - pairedValue[1])
                Result = Result + score
                pairedValue.pop(0)
                print(f"Current result: {Result}")
        
        return Result

           

        