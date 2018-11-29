class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx <= tx and sy <= ty:
            if tx == sx and ty == sy:
                return True
            elif ty > tx:
                r = (ty - sy) // tx
                if r == 0:
                    return False
                ty -= tx * r
            elif tx > ty:
                r = (tx - sx) // ty
                if r == 0:
                    return False
                tx -= ty * r
            elif tx == ty:
                return False
        return False


if __name__ == "__main__":
    print(Solution().reachingPoints(10, 2, 2, 11))          # False
    print(Solution().reachingPoints(1, 1, 3, 5))            # True
    print(Solution().reachingPoints(1, 1, 2, 2))            # False
    print(Solution().reachingPoints(1, 1, 1, 1))            # True
    print(Solution().reachingPoints(1, 2, 3, 5))            # True
    print(Solution().reachingPoints(2, 1, 3, 5))            # False
    print(Solution().reachingPoints(38, 44, 3, 5))          # False
    print(Solution().reachingPoints(1, 1, 1000000000, 1))   # True
