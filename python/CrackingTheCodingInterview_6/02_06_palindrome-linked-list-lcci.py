#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-11 23:36:55
# @Last Modified : 2020-07-11 23:36:55
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 编写一个函数，检查输入的链表是否是回文的。 
# 
#  
# 
#  示例 1： 
# 
#  输入： 1->2
# 输出： false 
#  
# 
#  示例 2： 
# 
#  输入： 1->2->2->1
# 输出： true 
#  
# 
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 
#  👍 26 👎 0


"""

import pytest

from common_utils import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next

        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (ListNode.init_list_from_str("1->2"), False),
    (ListNode.init_list_from_str("1->2->2->1"), True),
])
def test_solutions(args, expected):
    assert Solution().isPalindrome(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
