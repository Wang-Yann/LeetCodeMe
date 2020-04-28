#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 22:54:46
# @Last Modified : 2020-04-24 22:54:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class CBTInserter:

    def __init__(self, root: TreeNode):
        self._tree = [root]
        for node in self._tree:
            if node.left:
                self._tree.append(node.left)
            if node.right:
                self._tree.append(node.right)

    def insert(self, v: int) -> int:
        """[1, 2, 3, 4, 5]"""
        n = len(self._tree)
        self._tree.append(TreeNode(v))
        if n % 2:
            self._tree[(n - 1) // 2].left = self._tree[-1]
        else:
            self._tree[(n - 1) // 2].right = self._tree[-1]
        return self._tree[(n - 1) // 2].val

    def get_root(self) -> TreeNode:
        return self._tree[0]


if __name__ == '__main__':
    root = TreeNode(12)
    obj = CBTInserter(root)
    param_1 = obj.insert(3)
    param_3 = obj.insert(4)
    param_2 = obj.get_root()

    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    ob1 = CBTInserter(root1)
    ob1.insert(7)
    ob1.insert(8)
    print(ob1.get_root())
