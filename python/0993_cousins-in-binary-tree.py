#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。 
# 
#  如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。 
# 
#  我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。 
# 
#  只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。 
# 
#  
# 
#  示例 1： 
#  
# 
#  输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
#  
# 
#  示例 2： 
#  
# 
#  输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的节点数介于 2 到 100 之间。 
#  每个节点的值都是唯一的、范围为 1 到 100 的整数。 
#  
# 
#  
#  Related Topics 树 广度优先搜索

"""

import collections

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        lookup = {}
        dq = collections.deque([(root, None, 0)])
        while dq:
            if len(lookup) == 2:
                break
            for _ in range(len(dq)):
                node, parent, level = dq.popleft()
                if node.val == x:
                    lookup[x] = (parent, level)
                elif node.val == y:
                    lookup[y] = (parent, level)

                if node.left:
                    dq.append((node.left, node, level + 1))
                if node.right:
                    dq.append((node.right, node, level + 1))
        # print(lookup)
        return lookup and lookup[x][1] == lookup[y][1] and lookup[x][0] != lookup[y][0]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def isCousins(self, root, x, y):
        """节省内存比我的"""
        parent = {}
        depth = {}

        def dfs(node, parent_node=None):
            if node:
                depth[node.val] = 1 + depth[parent_node.val] if parent_node else 0
                parent[node.val] = parent_node
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(1,
                        left=TreeNode(2, left=TreeNode(4)),
                        right=TreeNode(3)), x=4, y=3), False],
    [dict(root=TreeNode(1,
                        left=TreeNode(2, right=TreeNode(4)),
                        right=TreeNode(3, right=TreeNode(5))), x=5, y=4), True],
    [dict(root=TreeNode(1,
                        left=TreeNode(2, right=TreeNode(4)),
                        right=TreeNode(3)), x=2, y=3), False],
])
def test_solutions(kw, expected):
    assert Solution().isCousins(**kw) == expected
    assert Solution1().isCousins(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
