class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pushed_index, popped_index = 0, 0
        while pushed_index < len(pushed) or popped_index < len(popped):
            if len(stack) > 0 and popped_index < len(popped) and stack[-1] == popped[popped_index]:
                stack.pop()
                popped_index += 1
            elif pushed_index < len(pushed):
                stack.append(pushed[pushed_index])
                pushed_index += 1
            else:
                return False
        return True


if __name__ == "__main__":
    print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
