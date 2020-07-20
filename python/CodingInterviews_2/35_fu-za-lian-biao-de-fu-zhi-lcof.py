#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-09 22:30:22
# @Last Modified : 2020-05-09 22:30:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指
# 向链表中的任意节点或者 null。
#
#
#
#  示例 1：
#
#
#
#  输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
#  示例 2：
#
#
#
#  输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#
#
#  示例 3：
#
#
#
#  输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#
#
#  示例 4：
#
#  输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
#
#
#
#
#  提示：
#
#
#  -10000 <= Node.val <= 10000
#  Node.random 为空（null）或指向链表中的节点。
#  节点数目不超过 1000 。
#
#
#
#
#  注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-point
# er/
#
#
#  Related Topics 链表
#  👍 65 👎 0
import pytest

from common_utils import Node


class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(-1)
        current, prev, copies = head, dummy, {}
        while current:
            copied = Node(current.val)
            copies[current] = copied
            prev.next = copied
            prev, current = prev.next, current.next
        current = head
        while current:
            if current.random:
                copies[current].random = copies[current.random]
            current = current.next
        return dummy.next


@pytest.mark.parametrize("args,expected", [
    [
        Node.initList([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
        Node.initList([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
     ]
])
def test_solutions(args, expected):
    res = Solution().copyRandomList(args)
    cur_res = res
    cur_expected = expected
    while cur_res and cur_expected:
        assert cur_res.val == cur_expected.val
        if cur_res.random:
            assert cur_res.random.val == cur_expected.random.val
        cur_res, cur_expected = cur_res.next, cur_expected.next
    assert cur_res is None and cur_expected is None


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
