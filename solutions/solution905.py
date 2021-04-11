class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        q = 0
        for p in range(len(A)):
            if A[p] & 1 == 0:
                A[p], A[q] = A[q], A[p]
                q += 1
        return A


if __name__ == "__main__":
    print(Solution().sortArrayByParity([3,1,2,4]))