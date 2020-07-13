class Solution:
    def largestValsFromLabels(self, values: 'List[int]', labels: 'List[int]', num_wanted: int, use_limit: int) -> int:        
        result = 0
        times = {key: 0 for key in set(labels)}
        num = 0
        for label, value in sorted(zip(labels, values), key=lambda x:-x[1]):
            if times[label] < use_limit:
                times[label] += 1
                result += value
                num += 1
            if num == num_wanted:
                break
        return result
        


if __name__ == "__main__":
    print(Solution().largestValsFromLabels([5,4,3,2,1], [1,1,2,2,3], 3, 1))
    print(Solution().largestValsFromLabels([5,4,3,2,1], [1,3,3,3,2], 3, 2))
    print(Solution().largestValsFromLabels([9,8,8,7,6], [0,0,0,1,1], 3, 1))
    print(Solution().largestValsFromLabels([9,8,8,7,6], [0,0,0,1,1], 3, 2))
    # print(Solution().largestValsFromLabels([7,9,8,7,6], [0,0,0,1,1], 3, 2))