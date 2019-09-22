class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        res, tmp = [], 0
        for i in range(len(mat[0])):
            j = 1
            while j < len(mat):
                if mat[0][i] in mat[j]:
                    tmp = mat[0][i]
                elif mat[0][i] not in mat[j]:
                    tmp = None
                    break
                j += 1
            if tmp is not None: res.append(mat[0][i])

        if not res:
            return -1
        else:
            return min(res)
