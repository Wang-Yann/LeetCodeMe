#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 17:28:47
# @Last Modified : 2020-07-21 17:28:47
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计并实现一个 TwoSum 的类，使该类需要支持 add 和 find 的操作。 
# 
#  add 操作 - 对内部数据结构增加一个数。 
# find 操作 - 寻找内部数据结构中是否存在一对整数，使得两数之和与给定的数相等。 
# 
#  示例 1: 
# 
#  add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
#  
# 
#  示例 2: 
# 
#  add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false 
#  Related Topics 设计 哈希表 
#  👍 21 👎 0

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class TwoSum:

    def __init__(self):
        """
        initialize your data structure here
        """
        self.lookup = collections.defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.lookup[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.lookup:
            num = value - key
            if num in self.lookup and (num != key or self.lookup[key] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    sol = TwoSum()
    sol.add(1)
    sol.add(3)
    sol.add(5)
    assert sol.find(4)
    assert not sol.find(7)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
