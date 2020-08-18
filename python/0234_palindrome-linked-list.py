#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-10 23:35:43
# @Last Modified : 2020-04-10 23:35:43
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 请判断一个链表是否为回文链表。
#
#  示例 1:
#
#  输入: 1->2
# 输出: false
#
#  示例 2:
#
#  输入: 1->2->2->1
# 输出: true
#
#
#  进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#  Related Topics 链表 双指针
#  👍 564 👎 0

"""
import copy

import pytest

from common_utils import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        借助二叉树后序遍历的思路，不需要显式反转原始链表 倒序遍历链表
        """
        left = head

        def traversal(right):
            nonlocal left
            if not right:
                return True
            res = traversal(right.next)
            res = res and right.val == left.val
            left = left.next
            return res

        return traversal(head)


class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        reverse, fast = None, head
        # Reverse the first half part of the list.
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next
        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        tail = head.next if fast else head
        # print(head,reverse,tail)

        # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        while reverse:
            if reverse.val != tail.val:
                return False
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next
        return True


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head

        def recursively_check(current_node):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check(head)


class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        return list(reversed(l)) == l


@pytest.mark.parametrize("args,expected", [
    (ListNode.initList([1, 2, 3, 4, 5]), False),
    (ListNode.initList([1, 2, 3, 2, 1]), True),
    (ListNode.initList([1, 2, 3, 3, 2, 1]), True),
])
def test_solutions(args, expected):
    assert Solution().isPalindrome(copy.deepcopy(args)) == expected
    assert Solution1().isPalindrome(copy.deepcopy(args)) == expected
    assert Solution2().isPalindrome(copy.deepcopy(args)) == expected
    assert Solution3().isPalindrome(copy.deepcopy(args)) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
