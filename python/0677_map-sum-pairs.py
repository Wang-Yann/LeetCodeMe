#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 实现一个 MapSum 类里的两个方法，insert 和 sum。 
# 
#  对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。 
# 
#  对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。 
# 
#  示例 1: 
# 
#  输入: insert("apple", 3), 输出: Null
# 输入: sum("ap"), 输出: 3
# 输入: insert("app", 2), 输出: Null
# 输入: sum("ap"), 输出: 5
#  
#  Related Topics 字典树

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class MapSum:
    """
    前缀字典树
    插入时
    每个前缀将更改为 delta = val - map[key]
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        trie = lambda: collections.defaultdict(trie)
        self.root = trie()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for char in key:
            cur = cur[char]
        delta = val
        if "_end" in cur:
            delta -= cur["_end"]
        cur = self.root
        for char in key:
            cur = cur[char]
            if "_count" in cur:
                cur["_count"] += delta
            else:
                cur["_count"] = delta
        cur["_end"] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur:
                return 0
            cur = cur[char]
        return cur["_count"]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# leetcode submit region end(Prohibit modification and deletion)

def test_solutions():
    obj = MapSum()
    obj.insert("apple", 3)
    print(obj.root)
    assert obj.sum("ap") == 3
    obj.insert("app", 2)
    # print(obj.root)
    assert obj.sum("ap") == 5
    assert obj.sum("xx") == 0


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
