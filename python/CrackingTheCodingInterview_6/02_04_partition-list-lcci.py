#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 00:32:23
# @Last Modified : 2020-07-12 00:32:23
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。
# 分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。 
# 
#  示例: 
# 
#  输入: head = 3->5->8->5->10->2->1, x = 5
# 输出: 3->1->2->10->5->5->8
#  
#  Related Topics 链表 双指针 
#  👍 21 👎 0


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

    def partition(self, head: ListNode, x: int) -> ListNode:
        p = q = head
        while q:
            if q.val < x:
                p.val, q.val = q.val, p.val
                p = p.next
            q = q.next

        return head


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(head=ListNode.init_list_from_str("3->5->8->5->10->2->1"), x=5),
     ListNode.init_list_from_str("3->1->2->10->5->5->8")],

])
def test_solutions(kwargs, expected):
    res = Solution().partition(**kwargs)
    while res and res.val < kwargs["x"]:
        res = res.next
    while res and res.val >= kwargs["x"]:
        res = res.next
    assert res is None


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
