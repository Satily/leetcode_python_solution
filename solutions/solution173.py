from data_structure import TreeNode, build_binary_tree, ds_print


class BSTIterator:
    def __init__(self, root: TreeNode):
        if root:
            self.path = [root]
            while self.path[-1].left is not None:
                self.path.append(self.path[-1].left)
        else:
            self.path = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        result = self.path[-1].val
        if self.path[-1].right is not None:
            self.path.append(self.path[-1].right)
            while self.path[-1].left is not None:
                self.path.append(self.path[-1].left)
        else:
            node = self.path.pop()
            while self.path and self.path[-1].right == node:
                node = self.path.pop()
        return result
                            

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.path) != 0
        


if __name__ == '__main__':
    # iterator = BSTIterator(build_binary_tree(((3,), 7, ((9,),15,(20,)))))
    # print(iterator.next())
    # print(iterator.next())
    # print(iterator.hasNext())
    # print(iterator.next())
    # print(iterator.hasNext())
    # print(iterator.next())
    # print(iterator.hasNext())
    # print(iterator.next())
    # print(iterator.hasNext())
    iterator = BSTIterator(None)
    print(iterator.hasNext())
