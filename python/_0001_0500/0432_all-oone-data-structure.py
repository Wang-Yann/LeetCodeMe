#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 请你实现一个数据结构支持以下操作： 
# 
#  
#  Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。 
#  Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否则使一个存在的 key 值减一。如果这个 key 不存在，这个函数不做任
# 何事情。key 保证不为空字符串。 
#  GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串"" 。 
#  GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串""。 
#  
# 
#  
# 
#  挑战： 
# 
#  你能够以 O(1) 的时间复杂度实现所有操作吗？ 
#  Related Topics 设计

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Node(object):
    """
    double linked list node
    """

    def __init__(self, value, keys):
        self.value = value
        self.keys = keys
        self.prev = None
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = Node(0, set())
        self.tail = Node(0, set())
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, pos, node):
        node.prev, node.next = pos.prev, pos
        pos.prev.next, pos.prev = node, node
        return node

    def erase(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        del node

    def empty(self):
        return self.head.next is self.tail

    def begin(self):
        return self.head.next

    def end(self):
        return self.tail

    def front(self):
        return self.head.next

    def back(self):
        return self.tail.prev


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_of_keys = {}
        self.buckets = LinkedList()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.bucket_of_keys:
            self.bucket_of_keys[key] = self.buckets.insert(self.buckets.begin(), Node(0, {key}))
        bucket, next_bucket = self.bucket_of_keys[key], self.bucket_of_keys[key].next
        if next_bucket is self.buckets.end() or next_bucket.value > bucket.value + 1:
            next_bucket = self.buckets.insert(next_bucket, Node(bucket.value + 1, set()))
        next_bucket.keys.add(key)
        self.bucket_of_keys[key] = next_bucket

        bucket.keys.remove(key)
        if not bucket.keys:
            self.buckets.erase(bucket)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.bucket_of_keys:
            return
        bucket, prev_bucket = self.bucket_of_keys[key], self.bucket_of_keys[key].prev
        self.bucket_of_keys.pop(key, None)
        if bucket.value > 1:
            if bucket is self.buckets.begin() or prev_bucket.value < bucket.value - 1:
                prev_bucket = self.buckets.insert(bucket, Node(bucket.value - 1, set()))
            prev_bucket.keys.add(key)
            self.bucket_of_keys[key] = prev_bucket
        bucket.keys.remove(key)
        if not bucket.keys:
            self.buckets.erase(bucket)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.buckets.empty():
            return ""
        return iter(self.buckets.back().keys).__next__()

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.buckets.empty():
            return ""
        return iter(self.buckets.front().keys).__next__()


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# leetcode submit region end(Prohibit modification and deletion)

def test_solutions():
    obj = AllOne()
    obj.inc("hello")
    assert obj.getMaxKey() == "hello"
    assert obj.getMinKey() == "hello"


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
