#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。 
# 
#  获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。 
# 写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写
# 入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
# 
#  
# 
#  进阶: 
# 
#  你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  
# 
#  示例: 
# 
#  LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#  
#  Related Topics 设计

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class DoubleListNode(object):

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
        # make node clean
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
        # make node clean
        node.next, node.prev = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.__list = LinkedList()
        self.__dict = {}
        self.__capacity = capacity

    def _insert(self, key, val):
        node = DoubleListNode(key, val)
        self.__list.insert(node)
        self.__dict[key] = node

    def get(self, key: int) -> int:
        if key in self.__dict:
            val = self.__dict[key].val
            self.__list.delete(self.__dict[key])
            self._insert(key, val)
            return val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.__dict:
            self.__list.delete(self.__dict[key])
        elif len(self.__dict) == self.__capacity:
            self.__dict.pop(self.__list.head.key)
            self.__list.delete(self.__list.head)
        self._insert(key, value)

    # Your LRUCache object will be instantiated and called as such:


# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)

class LRUCache1:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.__cache:
            return -1
        val = self.__cache.pop(key)
        self.__cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.__cache:
            self.__cache.pop(key)
        elif len(self.__cache) == self.__capacity:
            self.__cache.popitem(last=False)
        self.__cache[key] = value


@pytest.mark.parametrize("CLS", [LRUCache, LRUCache1])
def test_solution(CLS):
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # // 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    assert cache.get(2) == -1  # // 返回 -1 (未找到)
    cache.put(4, 4)  # // 该操作会使得密钥 1 作废
    assert cache.get(1) == -1  # // 返回 -1 (未找到)
    assert cache.get(3) == 3  # // 返回  3
    assert cache.get(4) == 4  # // 返回  4


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
