class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        rows = [{''}]
        for length in range(1, n + 1):
            row = {'(%s)' % item for item in rows[length - 1]}
            for left in range(1, length):
                right = length - left
                for left_item in rows[left]:
                    for right_item in rows[right]:
                        row.add(left_item + right_item)
            rows.append(row)
        return list(rows[n])


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
