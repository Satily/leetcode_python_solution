class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n > 45:
            return []
        result = []

        def dfs(current, rest, path):
            if len(path) + 1 == k:
                if current <= rest <= 9:
                    path.append(rest)
                    result.append(path.copy())
                    path.pop()
                return
            rest_deep = (k - len(path))
            top = int(rest / rest_deep)
            if top > 9:
                return
            for i in range(current, top + 1):
                path.append(i)
                dfs(i + 1, rest - i, path)
                path.pop()

        dfs(1, n, [])
        return result


if __name__ == "__main__":
    print(Solution().combinationSum3(2, 18))
    print(Solution().combinationSum3(2, 6))
    print(Solution().combinationSum3(3, 7))
    print(Solution().combinationSum3(3, 9))
