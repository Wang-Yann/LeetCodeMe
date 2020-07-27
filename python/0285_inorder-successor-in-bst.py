#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 11:34:54
# @Last Modified : 2020-07-27 11:34:54
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个二叉搜索树和其中的某一个结点，请你找出该结点在树中顺序后继的节点。 
# 
#  结点 p 的后继是值比 p.val 大的结点中键值最小的结点。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  输入: root = [2,1,3], p = 1
# 输出: 2
# 解析: 这里 1 的顺序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
#  
# 
#  示例 2: 
# 
#  
# 
#  输入: root = [5,3,6,2,4,null,null,1], p = 6
# 输出: null
# 解析: 因为给出的结点没有顺序后继，所以答案就返回 null 了。
#  
# 
#  
# 
#  注意: 
# 
#  
#  假如给出的结点在该树中没有顺序后继的话，请返回 null 
#  我们保证树中每个结点的值是唯一的 
#  
#  Related Topics 树 
#  👍 40 👎 0

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
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # the successor is somewhere lower in the right subtree
        # successor: one step right and then left till you can

        if p and p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        successor = None

        while root and root != p:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(p=TreeNode(1), root=TreeNode(2, TreeNode(1), TreeNode(3))), TreeNode(2)],
    [dict(p=TreeNode(6),
          root=TreeNode(5,
                        left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)),
                        right=TreeNode(3)))

        , None],
])
def test_solutions(kw, expected):
    res = Solution().inorderSuccessor(**kw)
    assert res == expected == None or (res and expected and res.val == expected.val)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
