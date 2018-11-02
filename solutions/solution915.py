class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # From Left
        maximum = A[0]
        from_left = [maximum]
        for i in range(1, len(A)):
            maximum = max(maximum, A[i])
            from_left.append(maximum)
        # From Left
        minimum = A[-1]
        from_right = [minimum]
        for i in reversed(range(len(A) - 1)):
            minimum = min(minimum, A[i])
            from_right.append(minimum)
        from_right.reverse()
        # Iteration
        for i in range(len(A) - 1):
            if from_left[i] <= from_right[i + 1]:
                return i + 1
        return len(A)


if __name__ == "__main__":
    print(Solution().partitionDisjoint([5, 0, 3, 8, 6]))
    print(Solution().partitionDisjoint([1, 1, 1, 0, 6, 12]))
    print(Solution().partitionDisjoint([1, 1]))
