class ListNumberGenerator(object):
    def __init__(self, nums):
        self.nums = nums

    def __iter__(self):
        internals = [(0, len(self.nums))]
        flags = [False] * len(self.nums)
        yield []
        while len(internals) > 0:
            internal = internals.pop()
            max_i = internal[0]
            for index in range(internal[0] + 1, internal[1]):
                if self.nums[index] > self.nums[max_i]:
                    max_i = index
            if internal[0] < max_i:
                internals.append((internal[0], max_i))
            if max_i + 1 < internal[1]:
                internals.append((max_i + 1, internal[1]))
            flags[max_i] = True
            yield [self.nums[index] for index, flag in enumerate(flags) if flag]


class Solution:
    def maxNumber(self, nums1: 'List[int]', nums2: 'List[int]', k: 'int') -> 'List[int]':
        def combine_number(l1, l2):
            ll1, ll2 = len(l1), len(l2)
            p1, p2 = 0, 0
            result = []
            while p1 < ll1 and p2 < ll2:
                if l1[p1] > l2[p2]:
                    result.append(l1[p1])
                    p1 += 1
                else:
                    result.append(l2[p2])
                    p2 += 1
            if p1 == ll1:
                result += l2[p2:]
            else:
                result += l1[p1:]
            return result

        def max_number(l1, l2):
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            if len(l1) != len(l2):
                return None
            for index in range(len(l1)):
                if l1[index] < l2[index]:
                    return l2
                if l1[index] > l2[index]:
                    return l1
            return l1

        dp1, dp2 = list(ListNumberGenerator(nums1)), list(ListNumberGenerator(nums2))
        result = None
        # print(max(0, k - len(nums2)), min(k + 1, len(nums1)))
        for i in range(max(0, k - len(nums2)), min(k + 1, len(nums1)) + 1):
            current = combine_number(dp1[i], dp2[k - i])
            result = max_number(result, current)
        return result


if __name__ == "__main__":
    print(Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
    print(Solution().maxNumber([6, 7], [6, 0, 4], 5))
    print(Solution().maxNumber([3, 9], [8, 9], 3))
