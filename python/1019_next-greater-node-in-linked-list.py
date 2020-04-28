#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 23:04:40
# @Last Modified : 2020-04-19 23:04:40
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

from common_utils import ListNode


class Solution:

    def nextLargerNodesMe(self, head: ListNode) -> List[int]:
        """
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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [2, 1, 5],
        [2, 7, 4, 3, 5],
        [1, 7, 5, 1, 9, 2, 5, 1]

    ]
    res = [sol.nextLargerNodes(ListNode.initList(x)) for x in samples]

    print(res)
