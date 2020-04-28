#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 19:10:30
# @Last Modified : 2020-04-20 19:10:30
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        """
        乍一看，这是一个平凡的问题。只需要遍历整棵树，检查 node.right.val > node.val
        和 node.left.val < node.val 对每个结点是否成立。
        问题是，这种方法并不总是正确。不仅右子结点要大于该节点，整个右子树的元素都应该大于该节点。
        TODO 这里犯过错

        """

        def isValidRecursive(node, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not isValidRecursive(node.right, val, upper):
                return False
            if not isValidRecursive(node.left, lower, val):
                return False
            return True

        return isValidRecursive(root)


class Solution2(object):

    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))

    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True

        return low < root.val and root.val < high \
               and self.isValidBSTRecu(root.left, low, root.val) \
               and self.isValidBSTRecu(root.right, root.val, high)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([2, 1, 3], [(1, 0)], [(1, 2)]),
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)])

    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.isValidBST(x) for x in lists]
    print(res)
