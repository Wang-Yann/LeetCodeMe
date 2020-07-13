#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 18:54:15
# @Last Modified : 2020-07-13 18:54:15
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存
# 被填满时，它应该删除最近最少使用的项目。 
# 
#  它应该支持以下操作： 获取数据 get 和 写入数据 put 。 
# 
#  获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。 
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新
# 的数据值留出空间。 
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
#  👍 19 👎 0

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class LRUCache:

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


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # // 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    assert cache.get(2) == -1  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    assert cache.get(1) == -1  # 返回 -1 (未找到)
    assert cache.get(3) == 3  # 返回  3
    assert cache.get(4) == 4  # 返回  4


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
