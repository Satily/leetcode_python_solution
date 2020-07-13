class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        l1, l2 = len(nums1), len(nums2)
        result = []
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result            


if __name__ == "__main__":
    print(Solution().intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
    print(Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
    