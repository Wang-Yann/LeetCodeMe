#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 23:58:12
# @Last Modified : 2020-04-22 23:58:12
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#
#
#
#  示例 1：
#
#  输入：head = [1,3,2]
# 输出：[2,3,1]
#
#
#
#  限制：
#
#  0 <= 链表长度 <= 10000
#  Related Topics 链表
#  👍 42 👎 0


from typing import List

import pytest

from common_utils import ListNode


class Solution:

    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        cur = head
        while cur:
            res.insert(0, cur.val)
            cur = cur.next
        return res


@pytest.mark.parametrize("args,expected", [
    [ListNode.initList([1, 3, 2]), [2, 3, 1]],
    [ListNode.initList([1]), [1]],
    [ListNode.initList([]), []],
])
def test_solutions(args, expected):
    assert Solution().reversePrint(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
