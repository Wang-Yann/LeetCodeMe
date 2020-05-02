#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 22:07:15
# @Last Modified : 2020-05-02 22:07:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest

from common_utils import ListNode


class Solution:

    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            if cur.val == val:
                break
            prev, cur = cur, cur.next
        prev.next = cur.next
        return dummy.next


@pytest.mark.parametrize("head,val,expected", [
    (ListNode.initList([4, 5, 1, 9]), 5, ListNode.initList([4, 1, 9]))
])
def test_solutions(head, val, expected):
    res = Solution().deleteNode(head, val)
    while res and expected:
        assert res.val == expected.val
        res, expected = res.next, expected.next
    assert res is None and expected is None


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
