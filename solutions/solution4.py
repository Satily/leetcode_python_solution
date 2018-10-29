import math


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def find_next(p, q, l1, l2, nums1c, nums2c):
            if p == l1:
                q += 1
                return p, q, nums2c[q]
            elif q == l2:
                p += 1
                return p, q, nums1c[p]
            elif nums1c[p + 1] < nums2c[q + 1]:
                p += 1
                return p, q, nums1c[p]
            else:
                q += 1
                return p, q, nums2c[q]

        p, q = 0, 0
        l1, l2 = len(nums1), len(nums2)
        nums1c, nums2c = [0], [0]
        nums1c.extend(nums1)
        nums2c.extend(nums2)
        num = 0
        while p + q < math.ceil((l1 + l2) / 2):
            p, q, num = find_next(p, q, l1, l2, nums1c, nums2c)
        if (l1 + l2) & 1 == 1:
            return num
        else:
            return (num + find_next(p, q, l1, l2, nums1c, nums2c)[2]) / 2


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
    print(Solution().findMedianSortedArrays([1], [2]))
    print(Solution().findMedianSortedArrays([1], []))
    print(Solution().findMedianSortedArrays([], [2, 3]))
