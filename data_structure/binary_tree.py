class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_binary_tree(t):
    def is_tuple(_t):
        return isinstance(_t, tuple) or _t is None

    def is_int(_t):
        return isinstance(_t, int)

    if isinstance(t, tuple):
        if len(t) == 3 and is_tuple(t[0]) and is_int(t[1]) and is_tuple(t[2]):
            rt = t
        elif len(t) == 2 and (is_tuple(t[0]) and is_int(t[1]) or is_int(t[0]) and is_tuple(t[1])):
            if is_int(t[0]):
                rt = (None,) + t
            else:
                rt = t + (None,)
        elif len(t) == 1 and is_int(t[0]):
            rt = (None,) + t + (None,)
        else:
            raise RuntimeError("Node ERROR: %s." % t)
        node = TreeNode(rt[1])
        node.left = build_binary_tree(rt[0])
        node.right = build_binary_tree(rt[2])
        return node
    elif t is None:
        return None
    else:
        raise RuntimeError("Unsupported type. %s." % t)


def flatten_binary_tree(binary_tree, with_none=False):
    if binary_tree is not None and not isinstance(binary_tree, TreeNode):
        raise RuntimeError("Unsupported type. %s." % binary_tree)
    if binary_tree is None:
        return None
    result = []
    flatten_left_node = flatten_binary_tree(binary_tree.left, with_none=with_none)
    if flatten_left_node is not None or with_none:
        result.append(flatten_left_node)
    result.append(binary_tree.val)
    flatten_right_node = flatten_binary_tree(binary_tree.right, with_none=with_none)
    if flatten_right_node is not None or with_none:
        result.append(flatten_right_node)
    return tuple(result)
