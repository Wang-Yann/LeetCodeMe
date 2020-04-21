#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 19:03:40
# @Last Modified : 2020-04-21 19:03:40
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def sumNumbersMe(self, root: TreeNode) -> int:
        results = []

        def dfs(path, cur):
            if not cur:
                return
            cur_val = cur.val
            if not cur.left and not cur.right:
                path = path * 10 + cur_val
                results.append(path)
                return
            path = path * 10 + cur_val
            dfs(path, cur.left)
            dfs(path, cur.right)
            path //= 10

        dfs(0, root)
        # print(results)
        return sum(results, 0)

    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, path_sum):
            if not node: return 0
            if not node.left and not node.right:
                return path_sum * 10 + node.val
            return helper(node.left, path_sum * 10 + node.val)\
                   + helper(node.right, path_sum * 10 + node.val)

        return helper(root, 0)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)]),
        ([1], [], [])

    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.sumNumbers(x) for x in lists]
    print(res)
