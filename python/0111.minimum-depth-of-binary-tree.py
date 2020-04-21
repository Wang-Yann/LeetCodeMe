#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 14:45:55
# @Last Modified : 2020-04-21 14:45:55
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def minDepthRecursive(self, root):
        if root is None:
            return 0

        if root.left and root.right:
            return min(self.minDepthRecursive(root.left), self.minDepthRecursive(root.right)) + 1
        else:
            return max(self.minDepthRecursive(root.left), self.minDepthRecursive(root.right)) + 1

    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [(root, 1)]
        levels = []
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node, level = queue.pop(0)
                if not node.left and not node.right:
                    levels.append(level)
                    continue
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        return min(levels)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([3, 9, 20, 15, 7], [(0, 1), (2, 3)], [(0, 2), (2, 4)]),
        ([1, None, 2, 4], [(2, 3)], [(0, 2)]),
        ([1, 2], [(0, 1)], []),
        ([1, 2, 3, 4, 5], [(0, 1), (1, 3)], [(0, 2), (2, 4)])
    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.minDepth(x) for x in lists]
    print(res)
