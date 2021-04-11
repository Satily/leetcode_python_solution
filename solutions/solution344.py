class Solution:
    def reverseString(self, s: 'List[str]') -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ls = len(s)
        for i in range(ls // 2):
            s[i], s[ls - i - 1] = s[ls - i - 1], s[i]        


if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    Solution().reverseString(s)
    print(s)

    s = ["H","a","n","n","a","h"]
    Solution().reverseString(s)
    print(s)