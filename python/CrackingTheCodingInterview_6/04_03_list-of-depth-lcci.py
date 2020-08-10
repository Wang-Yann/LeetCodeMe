#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 21:08:10
# @Last Modified : 2020-07-12 21:08:10
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。 
# 
#  
# 
#  示例： 
# 
#  输入：[1,2,3,4,5,null,7,8]
# 
#         1
#        /  \ 
#       2    3
#      / \    \ 
#     4   5    7
#    /
#   8
# 
# 输出：[[1],[2,3],[4,5,7],[8]]
#  
#  Related Topics 树 广度优先搜索 
#  👍 12 👎 0


"""

from typing import List

import pytest

from common_utils import ListNode, TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        res = []
        if not tree:
            return res
        stack = [tree]
        while stack:
            n = len(stack)
            head = ListNode(-1)
            cur = head
            for i in range(n):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                cur.next = ListNode(node.val)
                cur=cur.next
            res.append(head.next)
        return res



# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(tree=TreeNode(
        1,
        left=TreeNode(2, TreeNode(4, left=TreeNode(8)), TreeNode(5)),
        right=TreeNode(3, right=TreeNode(7))
    )),
        [
            ListNode(1),
            ListNode.initList([2, 3]),
            ListNode.initList([4, 5, 7]),
            ListNode.initList([8]),

        ]],

])
def test_solutions(kwargs, expected):
    res = Solution().listOfDepth(**kwargs)
    # print(res)
    assert all(repr(x) == repr(y) for x, y in zip(res, expected))


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
