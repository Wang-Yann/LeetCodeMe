#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 18:23:41
# @Last Modified : 2020-04-24 18:23:41
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections

from common_utils import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return root
        Result = collections.namedtuple("Result", ("node", "depth"))

        def dfs(cur):
            """
            Return node,depth
            题意有含糊
            """
            if not cur:
                return Result(None, 0)
            left_res, right_res = dfs(cur.left), dfs(cur.right)
            if left_res.depth > right_res.depth:
                return Result(left_res.node, left_res.depth + 1)
            elif left_res.depth < right_res.depth:
                return Result(right_res.node, right_res.depth + 1)
            else:
                return Result(cur, left_res.depth + 1)

        result = dfs(root)
        return result.node


if __name__ == '__main__':
    sol = Solution()
    target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))
    samples = [
        root, target
    ]
    lists = [x for x in samples]
    res = [sol.subtreeWithAllDeepest(x) for x in lists]
    print(res)
