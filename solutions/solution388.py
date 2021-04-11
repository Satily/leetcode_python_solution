class Solution:
    def lengthLongestPath(self, input: 'str') -> 'int':
        files = [(len(line.strip('\t')) + 1, line.count('\t') + 1, '.' in line) for line in input.split('\n')]
        sums = [0] * (max(map(lambda x: x[1], files)) + 1)
        result = 0
        for file_name_length, level, is_file in files:
            sums[level] = sums[level - 1] + file_name_length
            if is_file:
                result = max(result, sums[level])
        return max(0, result - 1)


if __name__ == "__main__":
    print(Solution().lengthLongestPath(""))
    print(Solution().lengthLongestPath("a"))
    print(Solution().lengthLongestPath("dir\n    file.txt"))
    print(Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print(Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
