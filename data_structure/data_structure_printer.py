from data_structure.link_list import ListNode
from data_structure.link_list import flatten_link_list
from data_structure.binary_tree import TreeNode
from data_structure.binary_tree import flatten_binary_tree


def ds_print(structure):
    transformed_structure = None
    if isinstance(structure, ListNode):
        transformed_structure = flatten_link_list(structure)
    elif isinstance(structure, TreeNode):
        transformed_structure = flatten_binary_tree(structure)
    else:
        pass

    if transformed_structure is None:
        raise RuntimeError("Unsupported type. %s." % transformed_structure)
    else:
        print(transformed_structure)
