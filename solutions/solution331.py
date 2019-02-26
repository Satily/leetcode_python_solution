class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        def dfs(preorder_list, index) -> int:
            if index >= len(preorder_list) or index == -1:
                return -1
            if preorder_list[index] == "#":
                return index + 1
            index = dfs(preorder_list, index + 1)
            return dfs(preorder_list, index)

        preorders = preorder.split(',')
        result = dfs(preorders, 0)
        return result == len(preorders)


if __name__ == "__main__":
    print(Solution().isValidSerialization("1"))
    print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    print(Solution().isValidSerialization("1,#"))
    print(Solution().isValidSerialization("9,#,#,1"))
