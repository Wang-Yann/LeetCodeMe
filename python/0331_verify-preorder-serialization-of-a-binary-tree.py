#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 09:58:52
# @Last Modified : 2020-04-26 09:58:52
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
#
#       _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
#
#
#  例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
#
#  给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
#
#  每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
#
#  你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。
#
#  示例 1:
#
#  输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# 输出: true
#
#  示例 2:
#
#  输入: "1,#"
# 输出: false
#
#
#  示例 3:
#
#  输入: "9,#,#,1"
# 输出: false
#  Related Topics 栈
#  👍 104 👎 0
import pytest


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
            Good  官方 TODO 
        我们可以定义一个概念，叫做槽位，二叉树中任意一个节点或者空孩子节点都要占据一个槽位。二叉树的建立也伴随着槽位数量的变化。
        开始时只有一个槽位，如果根节点是空节点，就只消耗掉一个槽位，如果根节点不是空节点，除了消耗一个槽位，还要为孩子节点增加两个新的槽位。
        之后的节点也是同理
            初始化可用槽位：slots = 1
        ----------------------------
        更清晰的解释
            slots =出度 - 入度
        在树（甚至图）中，所有节点的入度之和等于出度之和。可以根据这个特点判断输入序列是否为有效的！ 在一棵二叉树中：
            每个空节点（ "#" ）会提供 0 个出度和 1 个入度。
            每个非空节点会提供 2 个出度和 1 个入度

        """
        data_list = preorder.split(",")
        slots = 1
        for char in data_list:
            slots -= 1
            if slots < 0:
                return False
            if char != "#":
                slots += 2

        return slots == 0


@pytest.mark.parametrize("args,expected", [
    ["9,3,4,#,#,1,#,#,2,#,6,#,#", True],
    ["1,#", False],
    ["9,#,#,1", False],
])
def test_solutions(args, expected):
    assert Solution().isValidSerialization(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
