#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 08:18:28
# @Last Modified : 2021-02-22 08:18:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请你实现三个 API append，addAll 和 multAll 来实现奇妙序列。 
# 
#  请实现 Fancy 类 ： 
# 
#  
#  Fancy() 初始化一个空序列对象。 
#  void append(val) 将整数 val 添加在序列末尾。 
#  void addAll(inc) 将所有序列中的现有数值都增加 inc 。 
#  void multAll(m) 将序列中的所有现有数值都乘以整数 m 。 
#  int getIndex(idx) 得到下标为 idx 处的数值（下标从 0 开始），并将结果对 109 + 7 取余。如果下标大于等于序列的长度，请返回
#  -1 。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "appe
# nd", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# 输出：
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]
# 
# 解释：
# Fancy fancy = new Fancy();
# fancy.append(2);   // 奇妙序列：[2]
# fancy.addAll(3);   // 奇妙序列：[2+3] -> [5]
# fancy.append(7);   // 奇妙序列：[5, 7]
# fancy.multAll(2);  // 奇妙序列：[5*2, 7*2] -> [10, 14]
# fancy.getIndex(0); // 返回 10
# fancy.addAll(3);   // 奇妙序列：[10+3, 14+3] -> [13, 17]
# fancy.append(10);  // 奇妙序列：[13, 17, 10]
# fancy.multAll(2);  // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0); // 返回 26
# fancy.getIndex(1); // 返回 34
# fancy.getIndex(2); // 返回 20
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= val, inc, m <= 100 
#  0 <= idx <= 105 
#  总共最多会有 105 次对 append，addAll，multAll 和 getIndex 的调用。 
#  
#  Related Topics 设计 数学 
#  👍 23 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Fancy:
    """乘法逆元
     a^{-1} 就等于 a^{m-2} 对 m取模的结果
     将 getIndex 作为瓶颈
    """
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.A = []
        self.add = [0]
        self.mul = [1]

    def append(self, val: int) -> None:
        self.A.append(val)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])

    def addAll(self, inc: int) -> None:
        self.add[-1] += inc

    def multAll(self, m: int) -> None:
        self.add[-1] = self.add[-1] * m % self.MOD
        self.mul[-1] = self.mul[-1] * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.A):
            return -1
        m = self.mul[-1] * pow(self.mul[idx], self.MOD - 2, self.MOD)
        inc = self.add[-1] - self.add[idx] * m
        return (self.A[idx] * m + inc) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    fancy = Fancy()
    fancy.append(2)  # 奇妙序列：[2]
    fancy.addAll(3)  # 奇妙序列：[2+3] -> [5]
    fancy.append(7)  # 奇妙序列：[5, 7]
    fancy.multAll(2)  # 奇妙序列：[5*2, 7*2] -> [10, 14]
    fancy.getIndex(0)  # 返回 10
    fancy.addAll(3)  # 奇妙序列：[10+3, 14+3] -> [13, 17]
    fancy.append(10)  # 奇妙序列：[13, 17, 10]
    fancy.multAll(2)  # 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
    assert fancy.getIndex(0)  # 返回 26
    assert fancy.getIndex(1)  # 返回 34
    assert fancy.getIndex(2)  # 返回 20


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
