#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 18:02:36
# @Last Modified : 2020-07-29 18:02:36
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 你需要从一个包括括号和整数的字符串构建一棵二叉树。
# 
#  输入的字符串代表一棵二叉树。它包括整数和随后的0，1或2对括号。整数代表根的值，一对括号内表示同样结构的子树。 
# 
#  若存在左子结点，则从左子结点开始构建。 
# 
#  示例: 
# 
#  输入: "4(2(3)(1))(6(5))"
# 输出: 返回代表下列二叉树的根节点:
# 
#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5   
#  
# 
#  
# 
#  注意: 
# 
#  
#  输入字符串中只包含 '(', ')', '-' 和 '0' ~ '9' 
#  空树由 "" 而非"()"表示。 
#  
# 
#  
#  Related Topics 树 字符串 
#  👍 22 👎 0


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
    def str2tree(self, s: str) -> TreeNode:

        i = 0

        def build():
            nonlocal i
            if i == len(s):
                return
            val = ''
            # 提取数字
            while i < len(s) and (s[i].isdigit() or s[i] == '-'):
                val += s[i]
                i += 1
            # 建立根节点
            root = TreeNode(val)
            # 如果有左子树
            if i < len(s) and s[i] == '(':
                # 跳过左括号
                i += 1
                root.left = build()
                # 跳过右括号
                i += 1
            # 如果有右子树
            if i < len(s) and s[i] == '(':
                # 跳过左括号
                i += 1
                root.right = build()
                # 跳过右括号
                i += 1
            return root

        return build()


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="4(2(3)(1))(6(5))"),
     TreeNode(
         4,
         left=TreeNode(2, TreeNode(3), TreeNode(1)),
         right=TreeNode(6, left=TreeNode(5))
     )],
])
def test_solutions(kw, expected):
    assert repr(Solution().str2tree(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
