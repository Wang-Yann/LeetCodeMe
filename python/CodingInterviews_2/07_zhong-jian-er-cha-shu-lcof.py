#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 00:04:33
# @Last Modified : 2020-04-23 00:04:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0




# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#
#
#
#  例如，给出
#
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
#  限制：
#
#  0 <= 节点个数 <= 5000
#
#
#
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/
#  Related Topics 树 递归
#  👍 144 👎 0

from typing import List

from common_utils import TreeNode


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and inorder:
            return None
        lookup = {v:idx for idx, v in enumerate(inorder)}
        length = len(inorder)
        ##左闭右开
        def buildRecu(in_start, in_end):
            if in_start == in_end:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            idx = lookup[val]
            root.left = buildRecu(in_start, idx )
            root.right = buildRecu(idx + 1, in_end)
            return root

        return buildRecu(0, length)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        ([1], [1]),
        ([], []),
    ]
    res = [sol.buildTree(*x) for x in samples]
    print(res)
