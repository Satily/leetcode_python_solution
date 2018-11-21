class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, last_candidate_index, path, result):
            if target == 0:
                result.append(path.copy())
                return
            for index in range(last_candidate_index, len(candidates)):
                if target >= candidates[index]:
                    path.append(candidates[index])
                    dfs(candidates, target - candidates[index], index, path, result)
                    path.pop()

        candidates.sort()
        result = []
        dfs(candidates, target, 0, [], result)
        return result


if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum([2, 3, 5], 8))
