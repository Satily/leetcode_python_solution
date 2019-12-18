from data_structure import TreeNode, build_binary_tree, ds_print

class MidOrderTravel(object):
    def __init__(self):
        self.result = None

    def dfs(self, node):
        if node is None:
            return        
        self.dfs(node.left)
        self.result.append(node)
        self.dfs(node.right)

    def mid_order_traval(self, root):
        self.result = []
        self.dfs(root)
        return self.result

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = MidOrderTravel().mid_order_traval(root)
        peak, foot = None, None
        for index, node in enumerate(nodes):
            if index != len(nodes) - 1 and (index == 0 or nodes[index - 1].val < node.val) and nodes[index + 1].val < node.val and peak is None:
                peak = node
            if index != 0 and nodes[index - 1].val > node.val and (index == len(nodes) - 1 or nodes[index + 1].val > node.val):
                foot = node
        peak.val, foot.val = foot.val, peak.val



if __name__ == "__main__":
    # root = build_binary_tree('[1,3,null,null,2]')
    # Solution().recoverTree(root)
    # ds_print(root, mode='leetcode')
    
    # root = build_binary_tree('[3,1,4,null,null,2]')
    # Solution().recoverTree(root)
    # ds_print(root, mode='leetcode')

    root = build_binary_tree('[146,71,-13,55,null,231,399,321,null,null,null,null,null,-33]')
    Solution().recoverTree(root)
    ds_print(root, mode='leetcode')

    
