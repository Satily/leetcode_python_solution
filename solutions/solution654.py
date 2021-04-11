from data_structure import TreeNode, build_binary_tree, ds_print


class Solution:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> TreeNode:
        def construct_tree(nums, left, right):
            if left >= right:
                return None
            max_i = left
            for index in range(left + 1, right):
                if nums[index] > nums[max_i]:
                    max_i = index
            node = TreeNode(nums[max_i])
            node.left = construct_tree(nums, left, max_i)
            node.right = construct_tree(nums, max_i + 1, right)
            return node

        return construct_tree(nums, 0, len(nums))


if __name__ == "__main__":
    ds_print(Solution().constructMaximumBinaryTree([3,2,1,6,0,5]))
