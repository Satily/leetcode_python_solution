class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        for p in filter(lambda x: len(x) > 0 and x != '.', path.split('/')):
            if p == '..':
                if len(result) > 0:
                    result.pop()
            else:
                result.append(p)
        return '/' + '/'.join(result)


if __name__ == "__main__":
    print(Solution().simplifyPath("/home/"))
    print(Solution().simplifyPath("/a/./b/../../c/"))
    print(Solution().simplifyPath("/a/../../b/../c//.//"))
    print(Solution().simplifyPath("/a//b////c/d//././/.."))
