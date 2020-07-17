#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 15:52:08
# @Last Modified : 2020-04-20 15:52:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#  例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回锯齿形层次遍历如下：
#
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
#  Related Topics 栈 树 广度优先搜索
#  👍 221 👎 0
from collections import deque
from typing import List

from common_utils import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        def zigzagLevelTraversalRecursive(node, level):
            if len(res) == level:
                res.append([])
            if level % 2 == 1:
                res[level].insert(0, node.val)
            else:
                res[level].append(node.val)
            if node.left:
                zigzagLevelTraversalRecursive(node.left, level + 1)
            if node.right:
                zigzagLevelTraversalRecursive(node.right, level + 1)

        zigzagLevelTraversalRecursive(root, 0)
        return res

    def zigzagLevelOrderIter(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root: return levels
        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if level % 2 == 1:
                    levels[level].insert(0, node.val)
                else:
                    levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return levels


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)])

    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    print(lists)
    # res = [sol.levelOrder(x) for x in lists]
    res = [sol.zigzagLevelOrder(x) for x in lists]
    print(res)
