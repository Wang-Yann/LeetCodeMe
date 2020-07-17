#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 21:25:13
# @Last Modified : 2020-04-24 21:25:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
#
#
#
#  举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
#
#  如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
#
#  如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
#
#
#
#  提示：
#
#
#  给定的两颗树可能会有 1 到 200 个结点。
#  给定的两颗树上的值介于 0 到 200 之间。
#
#  Related Topics 树 深度优先搜索
#  👍 60 👎 0

"""
from common_utils import TreeNode


class Solution:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def isLeaf(node):
            return node and not node.left and not node.right

        def dfs(node, results):
            if not node:
                return
            if isLeaf(node):
                results.append(node.val)
            dfs(node.left, results)
            dfs(node.right, results)

        res1, res2 = [], []
        dfs(root1, res1)
        dfs(root2, res2)
        # print(res1, res2)
        return res1 == res2


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [TreeNode(1, TreeNode(2)),
         TreeNode(3, TreeNode(4, TreeNode(2)))]
    ]
    res = [sol.leafSimilar(*args) for args in samples]
    print(res)
