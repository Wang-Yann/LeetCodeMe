#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 22:54:28
# @Last Modified : 2020-04-22 22:54:28
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
#
#  你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
#
#
#
#  示例 1：
# 输入:
#
#    5
#  /  \
# 2   -3
#
#
#  返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
#
#  示例 2：
# 输入：
#
#    5
#  /  \
# 2   -5
#
#
#  返回 [2]，只有 2 出现两次，-5 只出现 1 次。
#
#
#
#  提示： 假设任意子树元素和均可以用 32 位有符号整数表示。
#  Related Topics 树 哈希表
#  👍 72 👎 0

"""


import collections
from typing import List

from common_utils import TreeNode


class Solution:

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        lookup = collections.defaultdict(int)
        if not root:
            return []

        def postPreOrderTraversalSum(cur):
            if not cur:
                return 0
            sum_key = sum([postPreOrderTraversalSum(cur.left),
                           cur.val, postPreOrderTraversalSum(cur.right)])
            lookup[sum_key] += 1
            return sum_key

        postPreOrderTraversalSum(root)
        mv = max(lookup.values())

        return [k for k, v in lookup.items() if v == mv]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(5, TreeNode(2), TreeNode(-3)),
        TreeNode(5, TreeNode(2), TreeNode(-5)),
    ]
    res = [sol.findFrequentTreeSum(x) for x in samples]
    print(res)
