#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 不使用任何内建的哈希表库设计一个哈希映射 
# 
#  具体地说，你的设计应该包含以下的功能 
# 
#  
#  put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。 
#  get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。 
#  remove(key)：如果映射中存在这个键，删除这个数值对。 
#  
# 
#  
# 示例： 
# 
#  MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // 返回 1
# hashMap.get(3);            // 返回 -1 (未找到)
# hashMap.put(2, 1);         // 更新已有的值
# hashMap.get(2);            // 返回 1 
# hashMap.remove(2);         // 删除键为2的数据
# hashMap.get(2);            // 返回 -1 (未找到) 
#  
# 
#  
# 注意： 
# 
#  
#  所有的值都在 [0, 1000000]的范围内。 
#  操作的总数目在[1, 10000]范围内。 
#  不要使用内建的哈希库。 
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


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 1001
        self.data = [LinkedList() for _ in range(self.key_range)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        l = self.data[key % self.key_range]
        node = l.find(key)
        if not node:
            l.insert(ListNode(key, value))
        else:
            node.val = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        l = self.data[key % self.key_range]
        node = l.find(key)
        if node:
            return node.val
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        l = self.data[key % self.key_range]
        node = l.find(key)
        if node:
            l.delete(node)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    hashMap = MyHashMap()
    assert hashMap.put(1, 1) is None
    assert hashMap.put(2, 2) is None
    assert hashMap.get(1) == 1  # 返回 1
    assert hashMap.get(3) == -1  # 返回 -1 (未找到)
    assert hashMap.put(2, 1) is None  # 更新已有的值
    assert hashMap.get(2) == 1  # 返回 1
    assert hashMap.remove(2) is None  # 删除键为2的数据
    assert hashMap.get(2) == -1  # 返回 -1 (未找到)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
