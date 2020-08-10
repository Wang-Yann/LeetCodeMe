#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 16:48:35
# @Last Modified : 2020-04-23 16:48:35
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
#
#  空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
#
#  示例 1:
#
#
# 输入: 二叉树: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /
#   4
#
# 输出: "1(2(4))(3)"
#
# 解释: 原本将是“1(2(4)())(3())”，
# 在你省略所有不必要的空括号对之后，
# 它将是“1(2(4))(3)”。
#
#
#  示例 2:
#
#
# 输入: 二叉树: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \
#       4
#
# 输出: "1(2()(4))(3)"
#
# 解释: 和第一个示例相似，
# 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。
#
#  Related Topics 树 字符串
#  👍 128 👎 0

"""
import pytest

from common_utils import TreeNode


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ""
        s = str(t.val)
        if t.left or t.right:
            s += "(" + self.tree2str(t.left) + ")"
        if t.right:
            s += "(" + self.tree2str(t.right) + ")"
        return s


@pytest.mark.parametrize("kw,expected", [
    [dict(t=TreeNode(1, left=TreeNode(2, TreeNode(4)), right=TreeNode(3)), ), '1(2(4))(3)'],
    [dict(t=TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3))), '1(2()(4))(3)'],
])
def test_solutions(kw, expected):
    assert Solution().tree2str(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
