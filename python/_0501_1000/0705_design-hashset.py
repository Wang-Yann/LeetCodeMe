#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 不使用任何内建的哈希表库设计一个哈希集合 
# 
#  具体地说，你的设计应该包含以下的功能 
# 
#  
#  add(value)：向哈希集合中插入一个值。 
#  contains(value) ：返回哈希集合中是否存在这个值。 
#  remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。 
#  
# 
#  
# 示例: 
# 
#  MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);     
# hashSet.add(2);     
# hashSet.contains(1); // 返回 true
# hashSet.contains(3); // 返回 false (未找到)
# hashSet.add(2);     
# hashSet.contains(2); // 返回 true
# hashSet.remove(2);     
# hashSet.contains(2); // 返回  false (已经被删除)
#  
# 
#  
# 注意： 
# 
#  
#  所有的值都在 [0, 1000000]的范围内。 
#  操作的总数目在[1, 10000]范围内。 
#  不要使用内建的哈希集合库。 
#  
#  Related Topics 设计 哈希表

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        node.next, node.prev = None, None
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next, node.prev = None, None

    def find(self, key):
        cur = self.head
        while cur:
            if cur.key == key:
                break
            cur = cur.next
        return cur


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 1001
        self.data = [LinkedList() for _ in range(self.key_range)]

    def add(self, key: int) -> None:
        l = self.data[key % self.key_range]
        node = l.find(key)
        if not node:
            l.insert(ListNode(key, 0))

    def remove(self, key: int) -> None:
        l = self.data[key % self.key_range]
        node = l.find(key)
        if node:
            l.delete(node)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        l = self.data[key % self.key_range]
        node = l.find(key)
        return node is not None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    hashSet = MyHashSet()
    assert hashSet.add(1) is None
    assert hashSet.add(2) is None
    assert hashSet.contains(1)  # 返回 true
    assert hashSet.contains(3) is False  # 返回 false (未找到)
    assert hashSet.add(2) is None  #
    assert hashSet.contains(2)  # 返回 true
    assert hashSet.remove(2) is None  #
    assert hashSet.contains(2) is False  # 返回  false (已经被删除)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
