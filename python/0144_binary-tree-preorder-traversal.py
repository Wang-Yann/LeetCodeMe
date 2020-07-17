#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 15:52:08
# @Last Modified : 2020-04-20 15:52:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树
#  👍 312 👎 0

from typing import List

from common_utils import TreeNode


class Solution0:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def preorderTraversalRecursive(node, result):
            if node is None:
                return
            result.append(node.val)
            preorderTraversalRecursive(node.left, result)
            preorderTraversalRecursive(node.right, result)

        preorderTraversalRecursive(root, res)
        return res


class Solution:
    """迭代　基"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)

        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)])

    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.preorderTraversal(x) for x in lists]
    print(res)
