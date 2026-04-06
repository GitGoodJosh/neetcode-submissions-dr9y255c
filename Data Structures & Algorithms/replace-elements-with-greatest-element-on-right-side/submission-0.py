class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lena =len(arr) + 1
        ans = [0] * lena 
        ans[lena-1] = -1
        print(ans)
        for i in range(len(arr)-1,0,-1):
            if arr[i] > ans[i+1]:
                ans[i] = arr[i]
            else:
                ans[i] = ans[i+1]
        return ans[1:]