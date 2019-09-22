class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        li, tmp, res = arr.copy(), abs(arr[1] - arr[0]), []
        arr.sort()
        i = 1
        while i < len(arr):
            if arr[i] - arr[i - 1] < tmp:
                tmp = arr[i] - arr[i - 1]
            i += 1
        # print(tmp)
        j = 1
        while j < len(arr):
            if arr[j] - arr[j - 1] == tmp:
                res.append([arr[j - 1], arr[j]])

            j += 1
        res.sort()
        return res