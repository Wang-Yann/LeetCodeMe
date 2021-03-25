#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。 
# 
#  如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 
# 。 
# 
#  一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null
# ,1,3]
# 输出：true
# 解释：树中蓝色的节点构成了与链表对应的子路径。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,nu
# ll,1,3]
# 输出：true
#  
# 
#  示例 3： 
# 
#  输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,
# null,1,3]
# 输出：false
# 解释：二叉树中不存在一一对应链表的路径。
#  
# 
#  
# 
#  提示： 
# 
#  
#  二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。 
#  链表包含的节点数目在 1 到 100 之间。 
#  二叉树包含的节点数目在 1 到 2500 之间。 
#  
#  Related Topics 树 链表 动态规划

"""

import pytest

from common_utils import ListNode, TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(cur_list, cur_tree):
            if cur_list is None:
                return True
            if not cur_tree:
                return False
            if cur_tree.val != cur_list.val:
                return False
            return dfs(cur_list.next, cur_tree.left) or dfs(cur_list.next, cur_tree.right)

        if not head:
            return True
        if not root:
            return False

        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        head=ListNode.initList([4, 2, 8]),
        root=TreeNode(1,
                      left=TreeNode(4, right=TreeNode(2, left=TreeNode(1))),
                      right=TreeNode(4, left=TreeNode(2, left=TreeNode(6), right=TreeNode(8, TreeNode(1), TreeNode(3))))
                      )
    ), True),
    pytest.param(dict(
        head=ListNode.initList([1, 4, 2, 6]),
        root=TreeNode(1,
                      left=TreeNode(4, right=TreeNode(2, left=TreeNode(1))),
                      right=TreeNode(4, left=TreeNode(2, left=TreeNode(6), right=TreeNode(8, TreeNode(1), TreeNode(3))))
                      )
    ), True),
    pytest.param(dict(
        head=ListNode.initList([1, 4, 2, 6, 8]),
        root=TreeNode(1,
                      left=TreeNode(4, right=TreeNode(2, left=TreeNode(1))),
                      right=TreeNode(4, left=TreeNode(2, left=TreeNode(6), right=TreeNode(8, TreeNode(1), TreeNode(3))))
                      )
    ), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isSubPath(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
