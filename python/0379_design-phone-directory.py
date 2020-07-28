#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 16:29:17
# @Last Modified : 2020-07-28 16:29:17
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一个电话目录管理系统，让它支持以下功能： 
# 
#  
#  get: 分配给用户一个未被使用的电话号码，获取失败请返回 -1 
#  check: 检查指定的电话号码是否被使用 
#  release: 释放掉一个电话号码，使其能够重新被分配 
#  
# 
#  
# 
#  示例： 
# 
#  // 初始化电话目录，包括 3 个电话号码：0，1 和 2。
# PhoneDirectory directory = new PhoneDirectory(3);
# 
# // 可以返回任意未分配的号码，这里我们假设它返回 0。
# directory.get();
# 
# // 假设，函数返回 1。
# directory.get();
# 
# // 号码 2 未分配，所以返回为 true。
# directory.check(2);
# 
# // 返回 2，分配后，只剩一个号码未被分配。
# directory.get();
# 
# // 此时，号码 2 已经被分配，所以返回 false。
# directory.check(2);
# 
# // 释放号码 2，将该号码变回未分配状态。
# directory.release(2);
# 
# // 号码 2 现在是未分配状态，所以返回 true。
# directory.check(2);
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= maxNumbers <= 10^4 
#  0 <= number < maxNumbers 
#  调用方法的总数处于区间 [0 - 20000] 之内 
#  
#  Related Topics 设计 链表 
#  👍 14 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class PhoneDirectory:
    """AAAC"""

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.pool_size = maxNumbers
        self.released_pool = set()
        self.cur_num = 0

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.released_pool:
            return self.released_pool.pop()
        if self.cur_num < self.pool_size:
            self.cur_num += 1
            return self.cur_num - 1
        return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return self.cur_num <= number < self.pool_size or number in self.released_pool

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number < self.cur_num and number not in self.released_pool:
            self.released_pool.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    #  // 初始化电话目录，包括 3 个电话号码：0，1 和 2。
    directory = PhoneDirectory(3)
    #
    # // 可以返回任意未分配的号码，这里我们假设它返回 0。
    assert directory.get() == 0
    #
    # // 假设，函数返回 1。
    assert directory.get() == 1
    #
    # // 号码 2 未分配，所以返回为 true。
    assert directory.check(2)
    #
    # // 返回 2，分配后，只剩一个号码未被分配。
    assert directory.get() == 2
    #
    # // 此时，号码 2 已经被分配，所以返回 false。
    assert directory.check(2) == False
    #
    # // 释放号码 2，将该号码变回未分配状态。
    directory.release(2)
    #
    # // 号码 2 现在是未分配状态，所以返回 true。
    assert directory.check(2)


def test_solution1():
    #  // 初始化电话目录，包括 3 个电话号码：0，1 和 2。
    directory = PhoneDirectory(1)
    assert directory.check(0)
    assert directory.get() == 0
    assert directory.check(0) == False
    assert directory.get() == -1


# input:["PhoneDirectory","check","get","check","get"] [[1],[0],[],[0],[]] Output:[null,true,0,false,1] Expected:[null,true,0,false,-1]

if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
