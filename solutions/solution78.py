class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        ln = len(nums)
        selectors = [0] * ln
        for time in range(2 ** ln):
            # Append new Item
            result_item = []
            for index, selector in enumerate(selectors):
                if selector == 1:
                    result_item.append(nums[index])
            result.append(result_item)
            # Add selectors
            index, c = 0, 1
            while c == 1 and index < ln:
                selectors[index] += c
                c, selectors[index] = selectors[index] >> 1, selectors[index] & 1
                index += 1
        return result


if __name__ == "__main__":
    print(Solution().subsets([1, 2, 4]))

