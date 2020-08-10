#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 23:04:40
# @Last Modified : 2020-04-19 23:04:40
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给出一个以头节点 head 作为第一个节点的链表。链表中的节点分别编号为：node_1, node_2, node_3, ... 。
#
#  每个节点都可能有下一个更大值（next larger value）：对于 node_i，如果其 next_larger(node_i) 是 node_j.
# val，那么就有 j > i 且 node_j.val > node_i.val，而 j 是可能的选项中最小的那个。如果不存在这样的 j，那么下一个更大值为 0
#  。
#
#  返回整数答案数组 answer，其中 answer[i] = next_larger(node_{i+1}) 。
#
#  注意：在下面的示例中，诸如 [2,1,5] 这样的输入（不是输出）是链表的序列化表示，其头节点的值为 2，第二个节点值为 1，第三个节点值为 5 。
#
#
#
#  示例 1：
#
#  输入：[2,1,5]
# 输出：[5,5,0]
#
#
#  示例 2：
#
#  输入：[2,7,4,3,5]
# 输出：[7,0,5,5,0]
#
#
#  示例 3：
#
#  输入：[1,7,5,1,9,2,5,1]
# 输出：[7,9,9,9,0,5,0,0]
#
#
#
#
#  提示：
#
#
#  对于链表中的每个节点，1 <= node.val <= 10^9
#  给定列表的长度在 [0, 10000] 范围内
#
#  Related Topics 栈 链表
#  👍 91 👎 0

"""
from typing import List

import pytest

from common_utils import ListNode


class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        """
        ME
        TODO
        单调栈

        """
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        length = len(vals)
        result = []
        increase_stack = []
        for i in range(length):
            cur_val = vals[i]
            while increase_stack and increase_stack[-1][1] < cur_val:
                idx, v = increase_stack.pop()
                result[idx] = cur_val
            increase_stack.append((len(result), cur_val))
            result.append(0)
        return result


class Solution1:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result, stack = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                idx, v = stack.pop()
                result[idx] = head.val
            stack.append((len(result), head.val))
            result.append(0)
            head = head.next
        # print(stack)
        return result


@pytest.mark.parametrize("args,expected", [
    (ListNode.initList([2, 1, 5]), [5, 5, 0]),
    (ListNode.initList([2, 7, 4, 3, 5]), [7, 0, 5, 5, 0]),
    (ListNode.initList([1, 7, 5, 1, 9, 2, 5, 1]), [7, 9, 9, 9, 0, 5, 0, 0]),
])
def test_solutions(args, expected):
    assert Solution().nextLargerNodes(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
