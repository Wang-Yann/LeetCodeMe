#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 不使用任何库函数，设计一个跳表。 
# 
#  跳表是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想
# 与链表相似。 
# 
#  例如，一个跳表包含 [30, 40, 50, 60, 70, 90]，然后增加 80、45 到跳表中，以下图的方式操作： 
# 
#  
# Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons 
# 
#  跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(
# n))，空间复杂度是 O(n)。 
# 
#  在本题中，你的设计应该要包含这些函数： 
# 
#  
#  bool search(int target) : 返回target是否存在于跳表中。 
#  void add(int num): 插入一个元素到跳表。 
#  bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。 
# 
#  
# 
#  了解更多 : https://en.wikipedia.org/wiki/Skip_list 
# 
#  注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。 
# 
#  样例: 
# 
#  Skiplist skiplist = new Skiplist();
# 
# skiplist.add(1);
# skiplist.add(2);
# skiplist.add(3);
# skiplist.search(0);   // 返回 false
# skiplist.add(4);
# skiplist.search(1);   // 返回 true
# skiplist.erase(0);    // 返回 false，0 不在跳表中
# skiplist.erase(1);    // 返回 true
# skiplist.search(1);   // 返回 false，1 已被擦除
#  
# 
#  约束条件: 
# 
#  
#  0 <= num, target <= 20000 
#  最多调用 50000 次 search, add, 以及 erase操作。 
#  
#  Related Topics 设计

"""
import math
import random

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class SkipNode:
    __slots__ = ('val', 'levels')

    def __init__(self, val, levels):
        self.val = val
        self.levels = [None] * levels


class Skiplist(object):
    """TODO TODO"""
    def __init__(self):
        self.head = SkipNode(-1, 16)

    def _iter(self, num):
        cur = self.head
        for level in range(15, -1, -1):
            while True:
                future = cur.levels[level]
                if future and future.val < num:
                    cur = future
                else:
                    break
            yield cur, level

    def search(self, target):
        for prev, level in self._iter(target):
            pass
        cur = prev.levels[0]
        return cur and cur.val == target

    def add(self, num):
        node_lvls = min(16, 1 + int(math.log2(1.0 / random.random())))
        node = SkipNode(num, node_lvls)

        for cur, level in self._iter(num):
            if level < node_lvls:
                future = cur.levels[level]
                cur.levels[level] = node
                node.levels[level] = future

    def erase(self, num):
        ans = False
        for cur, level in self._iter(num):
            future = cur.levels[level]
            if future and future.val == num:
                ans = True
                cur.levels[level] = future.levels[level]
        return ans


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# leetcode submit region end(Prohibit modification and deletion)


def testSkipList():
    skiplist = Skiplist()
    skiplist.add(1)  #
    skiplist.add(2)  #
    skiplist.add(3)  #
    assert skiplist.search(0) == False  # // 返回 false
    skiplist.add(4)  #
    assert skiplist.search(1)  # // 返回 true
    assert skiplist.erase(0) == False  # // 返回 false，0 不在跳表中
    assert skiplist.erase(1)  # // 返回 true
    assert skiplist.search(1) == False  # // 返回 false，1 已被擦除


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
