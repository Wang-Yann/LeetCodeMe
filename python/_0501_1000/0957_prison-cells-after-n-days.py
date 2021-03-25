#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 8 间牢房排成一排，每间牢房不是有人住就是空着。 
# 
#  每天，无论牢房是被占用或空置，都会根据以下规则进行更改： 
# 
#  
#  如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。 
#  否则，它就会被空置。 
#  
# 
#  （请注意，由于监狱中的牢房排成一行，所以行中的第一个和最后一个房间无法有两个相邻的房间。） 
# 
#  我们用以下方式描述监狱的当前状态：如果第 i 间牢房被占用，则 cell[i]==1，否则 cell[i]==0。 
# 
#  根据监狱的初始状态，在 N 天后返回监狱的状况（和上述 N 种变化）。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：cells = [0,1,0,1,1,0,0,1], N = 7
# 输出：[0,0,1,1,0,0,0,0]
# 解释：
# 下表概述了监狱每天的状况：
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
# 
#  
# 
#  示例 2： 
# 
#  输入：cells = [1,0,0,1,0,0,1,0], N = 1000000000
# 输出：[0,0,1,1,1,1,1,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  cells.length == 8 
#  cells[i] 的值为 0 或 1 
#  1 <= N <= 10^9 
#  
#  Related Topics 哈希表

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """
        14 是测出来的一周期
        """
        N = N - max(N - 1, 0) // 14 * 14
        for _ in range(N):
            cells = tuple(1 if 0 < i < 8 - 1 and cells[i - 1] == cells[i + 1] else 0 for i in range(8))
            #     cells = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1, 7)] + [0]
            # print(cells)
        return list(cells)


# leetcode submit region end(Prohibit modification and deletion)

def test_N():
    for N in range(44):
        N1 = N - max(N - 1, 0) // 14 * 14
        N2 = N % 14
        assert N1==N2


@pytest.mark.parametrize("kw,expected", [
    [dict(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=7), [0, 0, 1, 1, 0, 0, 0, 0]],
    [dict(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=14), [0, 0, 0, 0, 1, 1, 0, 0]],
    [dict(cells=[1, 0, 0, 1, 0, 0, 0, 1], N=14), [0, 1, 1, 0, 1, 1, 1, 0]],
    [dict(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=17), [0, 1, 1, 0, 0, 1, 0, 0]],
    [dict(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000), [0, 0, 1, 1, 1, 1, 1, 0]],
    [dict(cells=[1, 0, 0, 1, 0, 0, 0, 1], N=826), [0, 1, 1, 0, 1, 1, 1, 0]],
])
def test_solutions(kw, expected):
    assert Solution().prisonAfterNDays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
