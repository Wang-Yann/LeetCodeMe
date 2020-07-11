#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 00:26:58
# @Last Modified : 2020-07-12 00:26:58
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。 
# 
#  
# 
#  示例： 
# 
#  输入：单向链表a->b->c->d->e->f中的节点c
# 结果：不返回任何数据，但该链表变为a->b->d->e->f
#  
#  Related Topics 链表 
#  👍 33 👎 0


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

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (ListNode.initList([1, 2, 3]),
     ListNode.initList([2, 3])),
])
def test_solutions(args, expected):
    Solution().deleteNode(args)
    assert repr(args) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
