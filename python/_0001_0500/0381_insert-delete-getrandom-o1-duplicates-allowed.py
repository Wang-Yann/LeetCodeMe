#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。 
# 
#  注意: 允许出现重复元素。 
# 
#  
#  insert(val)：向集合中插入元素 val。 
#  remove(val)：当 val 存在时，从集合中移除一个 val。 
#  getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。 
#  
# 
#  示例: 
# 
#  // 初始化一个空的集合。
# RandomizedCollection collection = new RandomizedCollection();
# 
# // 向集合中插入 1 。返回 true 表示集合不包含 1 。
# collection.insert(1);
# 
# // 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
# collection.insert(1);
# 
# // 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
# collection.insert(2);
# 
# // getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
# collection.getRandom();
# 
# // 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
# collection.remove(1);
# 
# // getRandom 应有相同概率返回 1 和 2 。
# collection.getRandom();
#  
#  Related Topics 设计 数组 哈希表

"""
import collections
import random

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.idx = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]:
            return False
        remove, last = self.idx[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.lst) - 1)
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    collection = RandomizedCollection()
    assert collection.insert(1)
    assert not collection.insert(1)
    assert collection.insert(2)
    assert collection.getRandom() in [1, 2]
    assert collection.remove(1)
    assert collection.getRandom() in [1, 2]


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
