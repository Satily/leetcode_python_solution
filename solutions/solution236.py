from data_structure import TreeNode, build_binary_tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if node is None:
                return 0, None          
            lcode, lnode = dfs(node.left, p, q)
            if lcode == 2:
                return lcode, lnode
            rcode, rnode = dfs(node.right, p, q) 
            if rcode == 2:
                return rcode, rnode            
            code = (node.val in {p, q}) + lcode + rcode
            if code == 2:
                return code, node
            return code, None
        return dfs(root, p.val, q.val)[1]


if __name__ == "__main__":
    print(Solution().lowestCommonAncestor(build_binary_tree('[3,5,1,6,2,0,8,null,null,7,4]'), 5, 1).val)
    print(Solution().lowestCommonAncestor(build_binary_tree('[3,5,1,6,2,0,8,null,null,7,4]'), 5, 4).val)
