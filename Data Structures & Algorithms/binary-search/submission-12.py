class Solution:
    def search(self, nums: List[int], target: int) -> int:
        listlen = len(nums) - 1
        indexCheck = 0
        step = listlen // 2
        for i in range(listlen+1):
            indexCheck = indexCheck + step
            print(indexCheck, step)
            if indexCheck > listlen:
                return -1 
            if nums[indexCheck] == target :
                return indexCheck
            if nums[indexCheck] < target:
                step = step // 2
                if step == 0:
                    step =1
                print(f"m next step : {step}")

            if nums[indexCheck] > target:
                step = -(abs(step)//2)
                if step == 0:
                    step = -1
                print(f"l next step : {step}")
        return -1
        

            
