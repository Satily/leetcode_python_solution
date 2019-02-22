from data_structure import TreeNode, ds_print, build_binary_tree

from queue import Queue


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = Queue()
        if root is not None:
            q.put(root)
        result = []
        while not q.empty():
            node: TreeNode = q.get()
            if node is None:
                value = "null"
            else:
                value = str(node.val)
                q.put(node.left)
                q.put(node.right)
            result.append(value)
        while len(result) > 0 and result[-1] == "null":
            result.pop()
        return '[' + ','.join(result) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        values = list(map(lambda x: x.strip(), data[1:-1].split(',')))
        root = None
        q = Queue()

        for value in values:
            if value == "null":
                current = None
            else:
                current = TreeNode(int(value))
            if q.empty():
                root = current
            else:
                parent, direction = q.get()
                if not direction:
                    parent.left = current
                else:
                    parent.right = current
            if current is not None:
                q.put((current, 0))
                q.put((current, 1))
        return root


if __name__ == "__main__":
    codec = Codec()
    # node = codec.deserialize("[1,2,3,null,null,4,5]")
    # ds_print(node)
    # print(codec.serialize(node))

    print(codec.deserialize(codec.serialize(None)))
