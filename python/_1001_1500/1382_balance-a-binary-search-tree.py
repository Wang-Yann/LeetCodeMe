#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。 
# 
#  如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。 
# 
#  如果有多种构造方法，请你返回任意一种。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：root = [1,null,2,null,3,null,4,null,null]
# 输出：[2,1,3,null,null,null,4]
# 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树节点的数目在 1 到 10^4 之间。 
#  树节点的值互不相同，且在 1 到 10^5 之间。 
#  
#  Related Topics 二叉搜索树

"""

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorderTraversalHelper(node, arr):
            if not node:
                return
            inorderTraversalHelper(node.left, arr)
            arr.append(node.val)
            inorderTraversalHelper(node.right, arr)

        def sortedArrayToBstHelper(arr, i, j):
            if i >= j:
                return None
            mid = (i + j) // 2
            node = TreeNode(arr[mid])
            node.left = sortedArrayToBstHelper(arr, i, mid)
            node.right = sortedArrayToBstHelper(arr, mid + 1, j)
            return node

        arr = []
        inorderTraversalHelper(root, arr)
        return sortedArrayToBstHelper(arr, 0, len(arr))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        1,
        right=TreeNode(2, right=TreeNode(3, right=TreeNode(4)))
    )),
        None],
])
def test_solutions(kw, expected):
    def getHeight(node):
        if not node:
            return 0
        return max(getHeight(node.left), getHeight(node.right)) + 1

    res = Solution().balanceBST(**kw)
    assert abs(getHeight(res.left) - getHeight(res.right)) <= 1


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
