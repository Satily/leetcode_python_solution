from data_structure import Node


class Solution:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        if root.children is None or len(root.children) == 0:
            return 1
        return max([self.maxDepth(child) for child in root.children]) + 1


if __name__ == "__main__":
    pass