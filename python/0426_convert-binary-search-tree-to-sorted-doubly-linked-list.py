#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 11:43:33
# @Last Modified : 2020-07-29 11:43:33
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。 
# 
#  对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。 
# 
#  特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。 
# 
#  
# 
#  示例 1： 
# 
#  输入：root = [4,2,5,1,3] 
# 
# 输出：[1,2,3,4,5]
# 
# 解释：下图显示了转化后的二叉搜索树，实线表示后继关系，虚线表示前驱关系。
# 
#  
# 
#  示例 2： 
# 
#  输入：root = [2,1,3]
# 输出：[1,2,3]
#  
# 
#  示例 3： 
# 
#  输入：root = []
# 输出：[]
# 解释：输入是空树，所以输出也是空链表。
#  
# 
#  示例 4： 
# 
#  输入：root = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  -1000 <= Node.val <= 1000 
#  Node.left.val < Node.val < Node.right.val 
#  Node.val 的所有值都是独一无二的 
#  0 <= Number of Nodes <= 2000 
#  
#  Related Topics 树 链表 分治算法 
#  👍 48 👎 0

"""

import pytest

from common_utils import TreeNode

Node = TreeNode

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            nonlocal first, last
            if node:
                helper(node.left)
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node
                last = node
                helper(node.right)

        if not root:
            return None
        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        left_head, left_tail, right_head, right_tail = root, root, root, root
        if root.left:
            left_head = self.treeToDoublyList(root.left)
            left_tail = left_head.left
        if root.right:
            right_head = self.treeToDoublyList(root.right)
            right_tail = right_head.left
        left_tail.right, right_head.left = root, root
        root.left, root.right = left_tail, right_head
        left_head.left, right_tail.right = right_tail, left_head
        # print(left_head.val)
        return left_head


@pytest.mark.parametrize("CLS", [Solution, Solution1])
def test_solution(CLS):
    root = TreeNode(4, left=TreeNode(2, TreeNode(1), TreeNode(3)), right=TreeNode(5))
    sol = CLS()
    res = sol.treeToDoublyList(root)
    # print(res.val)
    assert res


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
