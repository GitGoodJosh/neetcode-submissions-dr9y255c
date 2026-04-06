class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        longest = 0
        for num in nums:
            if num == 1:
                counter += 1
            elif num == 0:
                if counter > longest:
                    longest = counter
                counter = 0
        if counter > longest:
            return counter
        else:
            return longest

            


