#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 23:29:29
# @Last Modified : 2020-04-19 23:29:29
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
#
#  删除完毕后，请你返回最终结果链表的头节点。
#
#
#
#  你可以返回任何满足题目要求的答案。
#
#  （注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）
#
#  示例 1：
#
#  输入：head = [1,2,-3,3,1]
# 输出：[3,1]
# 提示：答案 [1,2,1] 也是正确的。
#
#
#  示例 2：
#
#  输入：head = [1,2,3,-3,4]
# 输出：[1,2,4]
#
#
#  示例 3：
#
#  输入：head = [1,2,3,-3,-2]
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  给你的链表中可能有 1 到 1000 个节点。
#  对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
#
#  Related Topics 链表
#  👍 69 👎 0
import pytest

from common_utils import ListNode


class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        """

        """
        vals = []
        cur = head
        while cur:
            if cur.val != 0:
                vals.append(cur.val)
            cur = cur.next
        i = 0
        while 0 <= i < len(vals):
            sum = vals[i]
            j = i + 1
            while j < len(vals):
                sum += vals[j]
                if sum == 0:
                    vals[i:j + 1] = []
                    i = i - 1
                    break
                j += 1
            i += 1
        dummy = ListNode(-1)
        pos = dummy
        for v in vals:
            pos.next = ListNode(v)
            pos = pos.next
        return dummy.next


class Solution1:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        """
        TODO 前缀和 掌握 ; so Amazing
        我们可以考虑如果给的入参不是链表是数组的话，只需要求出前缀和，对于前缀和相同的项，
        那他们中间的部分即是可以消除掉的，比如以 [1, 2, 3, -3, 4] 为例，其前缀和数组为 [1, 3, 6, 3, 7] ，
        我们发现有两项均为 3，则 6 和 第二个 3 所对应的原数组中的数字是可以消掉的。
        换成链表其实也是一样的思路，把第一个 3 的 next 指向第二个 3 的 next 即可

        """
        seen = dict()
        dummy = ListNode(0)
        dummy.next = head
        # // 首次遍历建立 节点处链表和<->节点 哈希表
        # // 若同一和出现多次会覆盖，即记录该sum出现的最后一次节点
        prefix = 0
        cur = dummy
        while cur:
            prefix += cur.val
            seen[prefix] = cur
            cur = cur.next
        cur2 = dummy
        prefix = 0
        # // 第二遍遍历 若当前节点处sum在下一处出现了则表明两结点之间所有节点和为0 直接删除区间所有节点

        while cur2:
            prefix += cur2.val
            cur2.next = seen[prefix].next
            cur2 = cur2.next
        return dummy.next


@pytest.mark.parametrize("args,expected", [
    [ListNode.initList([1, 2, -3, 3, 1], ), ListNode.initList([3, 1])],
    [ListNode.initList([1, 2, 3, -3, 4], ), ListNode.initList([1, 2, 4])],
    [ListNode.initList([1, 2, 3, -3, -2], ), ListNode.initList([1])],
    [ListNode.initList([], ), ListNode.initList([])],
    [ListNode.initList([0], ), ListNode.initList([])],
    [ListNode.initList([0, 0], ), ListNode.initList([])],
    [ListNode.initList([-1, 1, 0, 1], ), ListNode.initList([1])],
    [ListNode.initList([2, 2, -2, 1, -1, -1], ), ListNode.initList([2, -1])],
    [ListNode.initList([-1, -2, 0, -1, 2, 2, -1, 1], ), ListNode.initList([])],
    [ListNode.initList([-1, 1, 1, -1]), ListNode.initList([])]
])
def test_solutions(args, expected):
    assert repr(Solution().removeZeroSumSublists(args)) == repr(expected)
    assert repr(Solution1().removeZeroSumSublists(args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
