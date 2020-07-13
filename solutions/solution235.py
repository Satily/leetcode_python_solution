from data_structure import TreeNode, build_binary_tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while(not (p.val <= root.val <= q.val)):
            if q.val < root.val:
                root = root.left
            else:
                root = root.right
        return root


if __name__ == "__main__":
    def find(node, val):
        if node is None:
            return None
        if node.val == val:
            return node
        return find(node.left, val) or find(node.right, val)
    tree = build_binary_tree("[6,2,8,0,4,7,9,null,null,3,5]")
    print(Solution().lowestCommonAncestor(tree, find(tree, 2), find(tree, 8)).val)
    print(Solution().lowestCommonAncestor(tree, find(tree, 2), find(tree, 4)).val)
