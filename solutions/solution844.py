class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def sync(s):
            result = []
            for ch in s:
                if ch == "#":
                    if len(result) > 0:
                        result.pop()
                else:
                    result.append(ch)
            return ''.join(result)

        return sync(S) == sync(T)


if __name__ == "__main__":
    print(Solution().backspaceCompare("ab#c", "ad#c"))
    print(Solution().backspaceCompare("ab##", "c#d#"))
    print(Solution().backspaceCompare("a##c", "#a#c"))
    print(Solution().backspaceCompare("a#c", "b"))
