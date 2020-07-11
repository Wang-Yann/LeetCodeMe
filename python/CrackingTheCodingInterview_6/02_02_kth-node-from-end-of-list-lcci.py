#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 00:14:14
# @Last Modified : 2020-07-12 00:14:14
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。 
# 
#  注意：本题相对原题稍作改动 
# 
#  示例： 
# 
#  输入： 1->2->3->4->5 和 k = 2
# 输出： 4 
# 
#  说明： 
# 
#  给定的 k 保证是有效的。 
#  Related Topics 链表 双指针 
#  👍 33 👎 0


"""

import pytest

from common_utils import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def kthToLast(self, head: ListNode, k: int) -> int:
        fast = slow = head
        for i in range(k):
            if not fast:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(head=ListNode.init_list_from_str("1->2->3->4->5"), k=2), 4],

])
def test_solutions(kwargs, expected):
    assert Solution().kthToLast(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
