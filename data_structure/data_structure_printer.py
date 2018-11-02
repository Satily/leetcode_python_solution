from data_structure.link_list import ListNode, flatten_link_list
from data_structure.binary_tree import TreeNode, flatten_binary_tree


def ds_print(*args):
    def transform(structure):
        transformed_structure = structure
        if isinstance(structure, ListNode):
            transformed_structure = flatten_link_list(structure)
        elif isinstance(structure, TreeNode):
            transformed_structure = flatten_binary_tree(structure)
        return transformed_structure
    print(*tuple(map(transform, args)))

