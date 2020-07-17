#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-21 22:16:57
# @Last Modified : 2020-04-21 22:16:57
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
#
#  调用 next() 将返回二叉搜索树中的下一个最小的数。
#
#
#
#  示例：
#
#
#
#  BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false
#
#
#
#  提示：
#
#
#  next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
#  你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
#
#  Related Topics 栈 树 设计
#  👍 213 👎 0

"""

from common_utils import TreeNode


class BSTIterator1:
    """LeetCode 运行有问题"""

    def __init__(self, root: TreeNode):
        self.stack = []
        self.cur = root

    def next(self) -> int:

        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        val = self.cur.val
        self.cur = self.cur.right
        return val

    def hasNext(self) -> bool:

        return self.cur is not None or self.stack

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.vals = []
        if root:
            self._inorder_traversal(root)
        self.cnt =len(self.vals)

    def _inorder_traversal(self, root):
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            self.vals.append(cur.val)
            cur = cur.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.cnt:
            self.cnt-=1
            return self.vals.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return  self.cnt>0



if __name__ == '__main__':
    root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
    iterator = BSTIterator(root)
    iterator.next()
    iterator.next()
    iterator.hasNext()
    iterator.next()
    iterator.hasNext()
    iterator.next()
    iterator.hasNext()
    iterator.next()
    iterator.hasNext()
