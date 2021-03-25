#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 18:15:11
# @Last Modified : 2020-08-07 18:15:11
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一棵 N 叉树的根节点 root ，返回该树的深拷贝（克隆）。 
# 
#  N 叉树的每个节点都包含一个值（ int ）和子节点的列表（ List[Node] ）。 
# 
#  
# class Node {
#     public int val;
#     public List<Node> children;
# }
#  
# 
#  N 叉树的输入序列用层序遍历表示，每组子节点用 null 分隔（见示例）。 
# 
#  进阶：你的答案可以适用于克隆图问题吗？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[1,null,3,2,4,null,5,6]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,
# null,13,null,null,14]
# 输出：[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13
# ,null,null,14]
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定的 N 叉树的深度小于或等于 1000。 
#  节点的总个数在 [0, 10^4] 之间 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 哈希表 
#  👍 1 👎 0

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

    def __repr__(self):
        if self:
            return "{}{}".format(self.val, self.children)


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        """AC"""
        lookup = collections.defaultdict(lambda: Node())
        lookup[None] = None
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            lookup[node].val = node.val
            if not node.children:
                continue
            for child in node.children:
                lookup[child].val = node.val
                lookup[node].children.append(lookup[child])
                stack.append(child)
        return lookup[root]


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def cloneTree(self, root):
        def dfs(node):
            if not node:
                return None
            copied = Node(node.val)
            for child in node.children:
                copied.children.append(dfs(child))
            return copied

        return dfs(root)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=Node(1, [
            Node(3,
                 children=[Node(5), Node(6),
                           Node(2),
                           Node(4), ]
                 )])
    ), None],
])
def test_solutions(kw, expected):
    root = kw["root"]
    assert repr(Solution().cloneTree(root)) == repr(root)
    assert repr(Solution1().cloneTree(root)) == repr(root)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
