#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 23:42:39
# @Last Modified : 2020-05-04 23:42:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest

from common_utils import ListNode


class Solution:

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """没有 kk 大于链表长度的 case ，因此不用考虑越界问题"""
        prev, later = head, head
        for _ in range(k):
            prev = prev.next
        while prev:
            prev, later = prev.next, later.next
        return later


@pytest.mark.parametrize("args,expected", [
    ([ListNode.init_list_from_str("1->2->3->4->5"), 2], ListNode.initList([4, 5])),
])
def test_solutions(args, expected):
    res = Solution().getKthFromEnd(*args)
    while res and expected:
        assert res.val == expected.val
        res, expected = res.next, expected.next
    assert res is None and expected is None


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
