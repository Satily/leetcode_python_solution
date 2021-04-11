# Time Limit Exceeded
# Need force pruning? That's crazy!
class Solution:
    def fourSum(self, nums: 'List[int]', target: int) -> 'List[List[int]]':
        nums.sort()
        ln = len(nums)
        result = []

        for i in range(0, ln - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in reversed(range(i + 3, ln)):
                if j != ln - 1 and nums[j] == nums[j + 1]:
                    continue
                n0, n3 = nums[i], nums[j]
                nt = target - n0 - n3
                if nums[i + 1] + nums[i + 2] > nt:
                    continue
                k, l = i + 1, j - 1
                while k < l:
                    s = nums[k] + nums[l]
                    if s > nt:
                        l -= 1
                    elif s < nt:
                        k += 1
                    else:
                        result.append([n0, nums[k], nums[l], n3])
                        k += 1
                        while k < l and nums[k - 1] == nums[k]:
                            k += 1
        return result


if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
    print(Solution().fourSum([0, 0, 0, 0], 1))
    print(Solution().fourSum([5, 5, 3, 5, 1, -5, 1, -2], 4))
    print(Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
    print(Solution().fourSum(
        [-497, -481, -481, -472, -471, -465, -422, -420, -413, -405, -388, -381, -366, -361, -359, -348, -334, -334,
         -318, -310, -305, -280, -273, -272, -262, -254, -248, -223, -208, -202, -196, -192, -189, -167, -165, -165,
         -156, -143, -136, -122, -120, -120, -108, -77, -50, -44, -34, -26, -17, -5, 13, 46, 46, 53, 54, 56, 66, 71, 72,
         75, 89, 115, 130, 139, 149, 151, 154, 196, 209, 219, 230, 240, 245, 246, 253, 267, 277, 289, 299, 302, 303,
         304, 342, 349, 360, 361, 361, 375, 392, 400, 407, 408, 408, 426, 427, 429, 443, 451, 481],
        -5617))
