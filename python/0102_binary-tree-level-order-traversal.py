#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 15:52:08
# @Last Modified : 2020-04-20 15:52:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from collections import deque
from typing import List

from common_utils import TreeNode


class SolutionMe:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans = []
        Q = []
        cur_level = 0
        Q.append((cur_level, root))
        tmp = []
        while Q:
            level, node = Q.pop(0)
            if not node:
                continue
            if level == cur_level:
                tmp.append(node.val)
            else:
                ans.append(tmp)
                tmp = [node.val]
                cur_level = level
            if node.left:
                Q.append((cur_level + 1, node.left))
            if node.right:
                Q.append((cur_level + 1, node.right))
        if tmp:
            ans.append(tmp)
        return ans


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        def levelOrderTraversalRecursive(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                levelOrderTraversalRecursive(node.left, level + 1)
            if node.right:
                levelOrderTraversalRecursive(node.right, level + 1)

        levelOrderTraversalRecursive(root, 0)
        return res

    def levelOrderIter(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root: return levels
        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
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
    res = [sol.levelOrderIter(x) for x in lists]
    print(res)
