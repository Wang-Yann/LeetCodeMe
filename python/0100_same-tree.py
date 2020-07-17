#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 21:42:33
# @Last Modified : 2020-04-20 21:42:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
#  示例 1:
#
#  输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# 输出: true
#
#  示例 2:
#
#  输入:      1          1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# 输出: false
#
#
#  示例 3:
#
#  输入:       1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# 输出: false
#
#  Related Topics 树 深度优先搜索
#  👍 398 👎 0

from common_utils import TreeNode


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val \
               and self.isSameTree(p.left, q.left) \
               and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([1, None, 2, 4], [(2, 3)], [(0, 2)]),
    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.isSameTree(lists[0], lists[1]), sol.isSameTree(lists[0], lists[0])]
    print(res)
