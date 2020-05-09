#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-09 22:30:22
# @Last Modified : 2020-05-09 22:30:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
