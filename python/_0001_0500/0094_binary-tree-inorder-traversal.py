#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 16:05:59
# @Last Modified : 2020-04-20 16:05:59
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个二叉树，返回它的中序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树 哈希表
#  👍 581 👎 0

"""
import copy
from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    """1.递归"""

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def helper(node, result):
            if node is None:
                return
            helper(node.left, result)
            result.append(node.val)
            helper(node.right, result)

        helper(root, ans)
        return ans


class Solution1:
    """迭代　基于栈"""

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

        return ans


class Solution2:
    """
    莫里斯遍历   (可以只需要O(1)空间)
    本方法中，我们使用一种新的数据结构：线索二叉树

    Step 1: 将当前节点current初始化为根节点
    Step 2: While current不为空，
        若current没有左子节点
            a. 将current添加到输出
            b. 进入右子树，亦即, current = current.right
        否则
            a. 在current的左子树中，令current成为最右侧节点的右子节点
            b. 进入左子树，亦即，current = current.left
    """

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right  # // move to next right node
            else:  # // has a left subtree
                pre = cur.left
                while pre.right:  # // find rightmost
                    pre = pre.right
                pre.right = cur  # // put cur after the pre node
                tmp = cur  # // store cur node
                cur = cur.left  # // move cur to the top of the new tree
                tmp.left = None  # // original cur left be null, avoid infinite loops

        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(1, right=TreeNode(2, left=TreeNode(3)))), [1, 3, 2]],
])
def test_solutions(kw, expected):
    assert Solution().inorderTraversal(**copy.deepcopy(kw)) == expected
    assert Solution2().inorderTraversal(**copy.deepcopy(kw)) == expected
    assert Solution1().inorderTraversal(**copy.deepcopy(kw)) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
