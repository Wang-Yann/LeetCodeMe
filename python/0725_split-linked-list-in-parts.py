#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 22:06:37
# @Last Modified : 2020-04-19 22:06:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
#
#  每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
#
#  这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
#
#  返回一个符合上述规则的链表的列表。
#
#  举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]
#
#  示例 1：
#
#
# 输入:
# root = [1, 2, 3], k = 5
# 输出: [[1],[2],[3],[],[]]
# 解释:
# 输入输出各部分都应该是链表，而不是数组。
# 例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且 root.ne
# xt.next.next = null。
# 第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
# 最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
#
#
#  示例 2：
#
#
# 输入:
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# 输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# 解释:
# 输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
#
#
#
#
#  提示:
#
#
#  root 的长度范围： [0, 1000].
#  输入的每个节点的大小范围：[0, 999].
#  k 的取值范围： [1, 50].
#
#
#
#  Related Topics 链表
#  👍 81 👎 0

"""
from typing import List

import pytest

from common_utils import ListNode


class Solution:

    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        """Me"""
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


class Solution1:
    def splitListToParts(self, root, k):
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


@pytest.mark.parametrize("kw,expected", [
    [dict(root=ListNode.initList([1, 2, 3]), k=5), [[1], [2], [3], [], []]],
    [dict(root=ListNode.initList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), k=3),
     [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]],
])
def test_solutions(kw, expected):
    expected = [ListNode.initList(x) for x in expected]
    res = Solution().splitListToParts(**kw)
    assert repr(res) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
