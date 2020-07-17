#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 12:25:29
# @Last Modified : 2020-04-19 12:25:29
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
#
#  要求返回这个链表的 深拷贝。
#
#  我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
#
#
#  val：一个表示 Node.val 的整数。
#  random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为 null 。
#
#
#
#
#  示例 1：
#
#
#
#  输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
#  示例 2：
#
#
#
#  输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#
#
#  示例 3：
#
#
#
#  输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#
#
#  示例 4：
#
#  输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
#
#
#
#
#  提示：
#
#
#  -10000 <= Node.val <= 10000
#  Node.random 为空（null）或指向链表中的节点。
#  节点数目不超过 1000 。
#
#  Related Topics 哈希表 链表
#  👍 320 👎 0
from collections import defaultdict

from common_utils import Node


class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        clone = defaultdict(lambda:Node(0))
        clone[None] = None
        cur = head
        while cur:
            clone[cur].val = cur.val
            clone[cur].next = clone[cur.next]
            clone[cur].random = clone[cur.random]
            cur = cur.next
        return clone[head]

    def copyRandomList2(self, head):
        dummy = Node(0)
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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]],
        []
    ]
    lists = [Node.initList(x) for x in samples]
    print(lists)
    # res = [sol.copyRandomList(x) for x in lists]
    res = [sol.copyRandomList2(x) for x in lists]

    print(res)
