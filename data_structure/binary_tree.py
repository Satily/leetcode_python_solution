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

    def build_by_list(_t):
        from queue import Queue
        if not _t:
            return None
        elif len(_t) == 1:
            return TreeNode(_t[0])
        head = TreeNode(_t[0])
        q = Queue()
        q.put((head, 0))
        q.put((head, 1))
        for num in _t[1:]:
            current, child_flag = q.get()
            if num is not None:
                new_node = TreeNode(num)
                q.put((new_node, 0))
                q.put((new_node, 1))
                if child_flag == 0:
                    current.left = new_node                    
                else:
                    current.right = new_node
        return head

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
    elif isinstance(t, list):
        return build_by_list(t)
    elif isinstance(t, str):
        return build_by_list(eval(t.replace("null", "None")))
    elif t is None:
        return None
    else:
        raise RuntimeError("Unsupported type. %s." % t)


def flatten_binary_tree(binary_tree, mode=None):
    if binary_tree is None:
        return None
    if not isinstance(binary_tree, TreeNode):
        raise RuntimeError("Unsupported type. %s." % binary_tree)    
    if mode in {'leetcode', 'leetcode_null_str'}:
        from queue import Queue
        result = []
        q = Queue()
        q.put(binary_tree)
        while not q.empty():
            current = q.get()
            if current is None:
                result.append(None)
            else:
                result.append(current.val)            
                q.put(current.left)            
                q.put(current.right)
        while result and result[-1] is None:
            result.pop()
        if mode == 'leetcode_null_str':
            result = str(result).replace('None', 'null')
        return result
    else:
        result = []
        flatten_left_node = flatten_binary_tree(binary_tree.left, mode=mode)
        if flatten_left_node is not None or mode == 'with_none':
            result.append(flatten_left_node)
        result.append(binary_tree.val)
        flatten_right_node = flatten_binary_tree(binary_tree.right, mode=mode)
        if flatten_right_node is not None or mode == 'with_none':
            result.append(flatten_right_node)
        return tuple(result)
