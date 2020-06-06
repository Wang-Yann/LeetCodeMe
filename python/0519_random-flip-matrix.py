#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 题中给出一个 n_rows 行 n_cols 列的二维矩阵，且所有值被初始化为 0。要求编写一个 flip 函数，均匀随机的将矩阵中的 0 变为 1，并返回
# 该值的位置下标 [row_id,col_id]；同样编写一个 reset 函数，将所有的值都重新置为 0。尽量最少调用随机函数 Math.random()，并且
# 优化时间和空间复杂度。 
# 
#  注意: 
# 
#  
#  1 <= n_rows, n_cols <= 10000 
#  0 <= row.id < n_rows 并且 0 <= col.id < n_cols 
#  当矩阵中没有值为 0 时，不可以调用 flip 函数 
#  调用 flip 和 reset 函数的次数加起来不会超过 1000 次 
#  
# 
#  示例 1： 
# 
#  输入: 
# ["Solution","flip","flip","flip","flip"]
# [[2,3],[],[],[],[]]
# 输出: [null,[0,1],[1,2],[1,0],[1,1]]
#  
# 
#  示例 2： 
# 
#  输入: 
# ["Solution","flip","flip","reset","flip"]
# [[1,2],[],[],[],[]]
# 输出: [null,[0,0],[0,1],null,[0,0]] 
# 
#  输入语法解释： 
# 
#  输入包含两个列表：被调用的子程序和他们的参数。Solution 的构造函数有两个参数，分别为 n_rows 和 n_cols。flip 和 reset 没
# 有参数，参数总会以列表形式给出，哪怕该列表为空 
#  Related Topics Random

"""
import random
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    https://blog.csdn.net/fuxuemingzhu/article/details/83188258
    Fisher–Yates shuffle 洗牌算法
    """

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n = n_rows * n_cols
        self.lookup = {}

    def flip(self) -> List[int]:
        self.n -= 1
        target = random.randint(0, self.n)
        x = self.lookup.get(target, target)
        self.lookup[target] = self.lookup.get(self.n, self.n)
        return list(divmod(x, self.n_cols))

    def reset(self) -> None:
        self.n = self.n_rows * self.n_cols
        self.lookup = {}


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    sol = Solution(2, 3)
    assert sol.flip()
    assert sol.flip()
    assert sol.flip()


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
