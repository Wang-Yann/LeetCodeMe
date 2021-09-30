#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。 
# 
#  给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 开始时， 青蛙默认已站在第一个石子上，并可以
# 假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。 
# 
#  如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。 
# 
# 
#  请注意： 
# 
#  
#  石子的数量 ≥ 2 且 < 1100； 
#  每一个石子的位置序号都是一个非负整数，且其 < 231； 
#  第一个石子的位置永远是0。 
#  
# 
#  示例 1: 
# 
#  
# [0,1,3,5,6,8,12,17]
# 
# 总共有8个石子。
# 第一个石子处于序号为0的单元格的位置, 第二个石子处于序号为1的单元格的位置,
# 第三个石子在序号为3的单元格的位置， 以此定义整个数组...
# 最后一个石子处于序号为17的单元格的位置。
# 
# 返回 true。即青蛙可以成功过河，按照如下方案跳跃： 
# 跳1个单位到第2块石子, 然后跳2个单位到第3块石子, 接着 
# 跳2个单位到第4块石子, 然后跳3个单位到第6块石子, 
# 跳4个单位到第7块石子, 最后，跳5个单位到第8个石子（即最后一块石子）。
#  
# 
#  示例 2: 
# 
#  
# [0,1,2,3,4,8,9,11]
# 
# 返回 false。青蛙没有办法过河。 
# 这是因为第5和第6个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
#  
#  Related Topics 动态规划

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        for stone in stones:
            dp[stone] = set([])
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                if k - 1 > 0 and stone + k - 1 in dp:
                    dp[stone + k - 1].add(k - 1)
                if stone + k in dp:
                    dp[stone + k].add(k)
                if stone + k + 1 in dp:
                    dp[stone + k + 1].add(k + 1)
        return bool(dp[stones[-1]])


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([0, 1, 3, 5, 6, 8, 12, 17], True),
    # pytest.param([0, 1, 2, 3, 4, 8, 9, 11], False),
])
def test_solutions(args, expected):
    assert Solution().canCross(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])