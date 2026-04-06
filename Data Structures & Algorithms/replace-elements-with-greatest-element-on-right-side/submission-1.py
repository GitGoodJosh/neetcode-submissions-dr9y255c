class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxxi = -1
        for i in range(len(arr)-1,-1,-1):
            curr = arr[i]
            arr[i] = maxxi
            if curr > maxxi:
                maxxi = curr
        return arr
