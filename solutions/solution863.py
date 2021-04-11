from data_structure import TreeNode, build_binary_tree


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        def search(node, path):
            if node is None:
                return None
            path.append(node)
            if node == target:
                return path
            r = search(node.left, path)
            if r is not None:
                return r
            r = search(node.right, path)
            if r is not None:
                return r
            path.pop()
            return None

        def get_length(node, deep):
            if node is None:
                return []
            if deep == 0:
                return [node.val]
            result = []
            result.extend(get_length(node.left, deep - 1))
            result.extend(get_length(node.right, deep - 1))
            return result

        path = search(root, [])
        path.reverse()
        result = []
        for length, node in enumerate(path):
            if K - length == 0:
                result.append(node.val)
                break
            if length == 0:
                result.extend(get_length(node.left, K - length - 1))
                result.extend(get_length(node.right, K - length - 1))
            elif node.left == path[length - 1]:
                result.extend(get_length(node.right, K - length - 1))
            elif node.right == path[length - 1]:
                result.extend(get_length(node.left, K - length - 1))
            # result.extend(get_length(node, K - length - 1))
        return result


if __name__ == "__main__":
    # root = build_binary_tree(
    #     (((6,), 5, ((7,), 2, (4,))), 3, ((0,), 1, (8,)))
    # )
    # target = root.left
    # K = 2
    # print(Solution().distanceK(root, target, K))

    root = build_binary_tree(
        (((3,), 1, (2,)), 0)
    )
    target = root.left.right
    K = 1
    print(Solution().distanceK(root, target, K))
