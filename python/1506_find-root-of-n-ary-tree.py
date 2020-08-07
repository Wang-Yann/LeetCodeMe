#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 18:42:48
# @Last Modified : 2020-08-07 18:42:48
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一棵 N 叉树 的所有节点在一个数组 Node[] tree 中，树中每个节点都有唯一的值。 
# 
#  找到并返回 N 叉树的根节点。 
# 
#  
# 
#  N 叉树的输入序列为其层序遍历序列，每组子节点用 null 分隔（见示例）。 
# 
#  
# 
#  上图中的 N 叉树的序列化描述为 [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,
# null,12,null,13,null,null,14] 。 
# 
#  进阶：你可以使用 O(1) 额外内存空间找到该树的根节点吗？ 
# 
#  备注： 
# 
#  
#  下列输入仅用于测试。 
#  你会以任意顺序接收到 N 叉树全部节点的列表。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：[1,null,3,2,4,null,5,6]
# 输出：[1,null,3,2,4,null,5,6]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13
# ,null,null,14]
# 输出：[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13
# ,null,null,14]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点的总个数在 [1, 5*10^4] 之间。 
#  每个节点都有唯一的值。 
#  
#  👍 2 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
        GOOD TODO
        对于非根节点，它会在 tree 列表中出现一次，并且在某个节点的 children 列表中出现一次，一共出现两次。
        遍历所有的节点以及它们的子节点，进行按位异或运算，由于一个数按位异或两次等于没有进行任何运算，因此最后运算的结果就是根节点的权值。


        """
        root = 0
        for node in tree:
            root ^= node.val
            for child in node.children:
                root ^= child.val
        for node in tree:
            if node.val == root:
                return node


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        tree=[Node(1, children=[
            Node(3, children=[Node(5), Node(6)]),
            Node(2), Node(4)
        ]), Node(3, children=[Node(5), Node(6)]), Node(2), Node(4), Node(5), Node(6)]
    ), Node(1)],
])
def test_solutions(kw, expected):
    res = Solution().findRoot(**kw)
    # print(res)
    assert res.val == expected.val


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
