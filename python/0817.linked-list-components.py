#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 22:38:04
# @Last Modified : 2020-04-19 22:38:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

from common_utils import ListNode


class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        """
        TODO 题义转换
        我们对链表进行一次扫描，一个组件在链表中对应一段极长的连续节点，因此如果当前的节点在列表 G 中，
        并且下一个节点不在列表 G 中，我们就找到了一个组件的尾节点，可以将答案加 1
        """
        lookup = set(G)
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        result = 0
        while cur and cur.next:
            if cur.val not in lookup and cur.next.val in lookup:
                result += 1
            cur = cur.next
        return result


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ("0->1->2->3", [0, 1, 3]),
        ("0->1->2->3->4", [0, 3, 1, 4]),
    ]
    args_list = [(ListNode.init_list_from_str(x), y) for x, y in samples]
    res = [sol.numComponents(x, y) for x, y in args_list]
    print(res)
