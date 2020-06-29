#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 
# 'b'，依此类推。 
# 
#  找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。 
# 
#  （小贴士：字符串中任何较短的前缀在字典序上都是较小的：例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。） 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[0,1,2,3,4,3,4]
# 输出："dba"
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[25,1,3,1,3,0,2]
# 输出："adz"
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：[2,2,1,null,1,0,null,0]
# 输出："abc"
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定树的结点数介于 1 和 8500 之间。 
#  树中的每个结点都有一个介于 0 和 25 之间的值。 
#  
#  Related Topics 树 深度优先搜索

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
    def smallestFromLeaf(self, root: TreeNode) -> str:
        candidates = []

        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                candidates.append(path[::-1])
            if node.left:
                dfs(node.left, path + chr(ord("a") + node.left.val))
            if node.right:
                dfs(node.right, path + chr(ord("a") + node.right.val))

        dfs(root, chr(ord("a") + root.val))
        # print(candidates)
        return min(candidates)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.ans = "~"

        def dfs(node, A):
            if node:
                A.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(A)))

                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()

        dfs(root, [])
        return self.ans


@pytest.mark.parametrize("args,expected", [
    (TreeNode(0,
              left=TreeNode(1, TreeNode(3), TreeNode(4)),
              right=TreeNode(2, TreeNode(3), TreeNode(4)))
     , "dba"
     ),
    (TreeNode(25,
              left=TreeNode(1, TreeNode(1), TreeNode(3)),
              right=TreeNode(3, TreeNode(0), TreeNode(2)))
     , "adz"
     ),
    (TreeNode(2,
              left=TreeNode(2, right=TreeNode(1, left=TreeNode(0))),
              right=TreeNode(1, left=TreeNode(0)))
     , "abc"
     )
])
def test_solutions(args, expected):
    assert Solution().smallestFromLeaf(args) == expected
    assert Solution1().smallestFromLeaf(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
