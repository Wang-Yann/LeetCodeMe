#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 22:06:37
# @Last Modified : 2020-04-19 22:06:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from typing import List

from common_utils import ListNode


class Solution:

    def splitListToPartsMe(self, root: ListNode, k: int) -> List[ListNode]:
        if not root:
            return [None] * k
        n = 0
        cur = root
        while cur:
            n += 1
            cur = cur.next
        rest = n % k
        divide = n // k
        cur_pos = root
        # print(rest,divide)
        res = [ListNode(-1) for _ in range(k)]
        for i in range(k):
            ith_node = res[i % k]
            ith_node.next = cur_pos
            if not cur_pos:
                continue
            else:
                cnt = divide
                if rest > 0:
                    rest -= 1
                    cnt += 1
                for _ in range(cnt - 1):
                    cur_pos = cur_pos.next
                if cur_pos:
                    tmp = cur_pos.next
                    cur_pos.next = None
                    cur_pos = tmp
        return [x.next for x in res]

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n = 0
        curr = root
        while curr:
            curr = curr.next
            n += 1
        width, remainder = divmod(n, k)

        result = []
        curr = root
        for i in range(k):
            head = curr
            for j in range(width - 1 + int(i < remainder)):
                if curr:
                    curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
            result.append(head)
        return result


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, 2, 3], 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)

    ]
    lists = [(ListNode.initList(x), y) for x, y in samples]
    res = [sol.splitListToPartsSP(x, y) for x, y in lists]
    print(res)
