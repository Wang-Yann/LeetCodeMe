#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-21 21:08:59
# @Last Modified : 2020-04-21 21:08:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 给定一个二叉树
#
#  struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
#  初始状态下，所有 next 指针都被设置为 NULL。
#
#
#
#  进阶：
#
#
#  你只能使用常量级额外空间。
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
#
#
#
#
#  示例：
#
#
#
#  输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
#
#
#
#  提示：
#
#
#  树中的节点数小于 6000
#  -100 <= node.val <= 100
#
#
#
#
#
#
#  Related Topics 树 深度优先搜索
#  👍 172 👎 0
import pytest

from common_utils import TreeNodeWithNext as Node


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        """
        Good
        https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-28/
        """
        if not root:
            return root
        cur = root
        while cur:
            dummy = Node(-1)
            tail = dummy
            # //遍历 cur 的当前层
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = dummy.next
            # //更新 cur 到下一层
        return root


@pytest.mark.parametrize("args,expected", [
    (Node(1, Node(2, None, Node(5), None), Node(3, None, Node(7), None), None), [1, 2, 3, '#', 5, '#', 7])
])
def test_solutions(args, expected):
    assert repr(Solution().connect(args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
