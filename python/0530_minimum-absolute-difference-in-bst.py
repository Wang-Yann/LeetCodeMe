#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 22:09:57
# @Last Modified : 2020-04-22 22:09:57
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
#
#
#
#  示例：
#
#  输入：
#
#    1
#     \
#      3
#     /
#    2
#
# 输出：
# 1
#
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
#
#
#
#
#  提示：
#
#
#  树中至少有 2 个节点。
#  本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
# 相同
#
#  Related Topics 树
#  👍 121 👎 0
from common_utils import TreeNode


class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:

        def in_order_traversal(cur):
            if not cur:
                return []
            stack = []
            res = []
            cur =root
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            return res

        results = in_order_traversal(root)
        # print(results)
        if len(results) <= 1:
            return None
        else:
            delta = float("inf")
            for i in range(1, len(results)):
                delta = min(abs(results[i] - results[i - 1]),delta)
            return delta


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, right=TreeNode(3, TreeNode(2))),
        TreeNode(12),
        None
    ]
    res = [sol.getMinimumDifference(x) for x in samples]
    print(res)
