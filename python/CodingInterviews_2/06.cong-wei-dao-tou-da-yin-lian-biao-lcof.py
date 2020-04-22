#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 23:58:12
# @Last Modified : 2020-04-22 23:58:12
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

from common_utils import ListNode


class Solution:

    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        cur = head
        while cur:
            res.insert(0, cur.val)
            cur = cur.next
        return res


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ListNode.initList([1, 3, 2]),
        ListNode.initList([1]),
        ListNode.initList([]),
    ]
    res = [sol.reversePrint(x) for x in samples]
    print(res)
