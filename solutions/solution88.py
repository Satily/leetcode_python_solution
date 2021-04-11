class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p, q = m - 1, n - 1
        for index in reversed(range(m + n)):
            if p < 0:
                nums1[index] = nums2[q]
                q -= 1
            elif q < 0:
                nums1[index] = nums1[p]
                p -= 1
            elif nums1[p] > nums2[q]:
                nums1[index] = nums1[p]
                p -= 1
            else:
                nums1[index] = nums2[q]
                q -= 1





if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
