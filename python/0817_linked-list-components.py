#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 22:38:04
# @Last Modified : 2020-04-19 22:38:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。
#
#  同时给定列表 G，该列表是上述链表中整型值的一个子集。
#
#  返回列表 G 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 G 中）构成的集合。
#
#
#
#  示例 1：
#
#  输入:
# head: 0->1->2->3
# G = [0, 1, 3]
# 输出: 2
# 解释:
# 链表中,0 和 1 是相连接的，且 G 中不包含 2，所以 [0, 1] 是 G 的一个组件，同理 [3] 也是一个组件，故返回 2。
#
#  示例 2：
#
#  输入:
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# 输出: 2
# 解释:
# 链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。
#
#
#
#  提示：
#
#
#  如果 N 是给定链表 head 的长度，1 <= N <= 10000。
#  链表中每个结点的值所在范围为 [0, N - 1]。
#  1 <= G.length <= 10000
#  G 是链表中所有结点的值的一个子集.
#
#  Related Topics 链表
#  👍 48 👎 0

"""


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
