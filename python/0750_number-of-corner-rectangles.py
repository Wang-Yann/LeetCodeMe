#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 14:50:49
# @Last Modified : 2020-07-31 14:50:49
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个只包含 0 和 1 的网格，找出其中角矩形的数量。 
# 
#  一个「角矩形」是由四个不同的在网格上的 1 形成的轴对称的矩形。注意只有角的位置才需要为 1。并且，4 个 1 需要是不同的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = 
# [[1, 0, 0, 1, 0],
#  [0, 0, 1, 0, 1],
#  [0, 0, 0, 1, 0],
#  [1, 0, 1, 0, 1]]
# 输出：1
# 解释：只有一个角矩形，角的位置为 grid[1][2], grid[1][4], grid[3][2], grid[3][4]。
#  
# 
#  示例 2： 
# 
#  输入：grid = 
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]
# 输出：9
# 解释：这里有 4 个 2x2 的矩形，4 个 2x3 和 3x2 的矩形和 1 个 3x3 的矩形。
#  
# 
#  示例 3： 
# 
#  输入：grid = 
# [[1, 1, 1, 1]]
# 输出：0
# 解释：矩形必须有 4 个不同的角。
#  
# 
#  
# 
#  提示： 
# 
#  
#  网格 grid 中行和列的数目范围为 [1, 200]。 
#  每个网格 grid[i][j] 中的值不是 0 就是 1 。 
#  网格中 1 的个数不会超过 6000。 
#  
# 
#  
#  Related Topics 动态规划 
#  👍 22 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        """
        转换一下思想：每增加一行，角矩形的数量增加了多少。
        算法：
        我们用 count[i, j] 来记录 row[i] = row[j] = 1 的次数。当我们处理新的一行时，对于每一对 new_row[i] = new_row[j] = 1，
        我们添加 count[i, j] 到答案中，然后 count[i, j]++

        """
        counter = collections.Counter()
        ans = 0
        for row in grid:
            for idx1, v1 in enumerate(row):
                if v1:
                    for idx2 in range(idx1 + 1, len(row)):
                        if row[idx2]:
                            ans += counter[idx1, idx2]
                            counter[idx1, idx2] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def countCornerRectangles(self, grid):

        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        # print(rows)
        result = 0
        for i in range(len(rows)):
            lookup = set(rows[i])
            for j in range(i):
                count = sum(1 for c in rows[j] if c in lookup)
                result += count * (count - 1) / 2
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(
        grid=[[1, 0, 0, 1, 0],
              [0, 0, 1, 0, 1],
              [0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1]]
    ), 1],

    [dict(
        grid=[[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]]
    ), 9],
    [dict(
        grid=[[1, 1, 1, 1]]
    ), 0, ]

])
def test_solutions(kw, expected):
    assert Solution().countCornerRectangles(**kw) == expected
    assert Solution1().countCornerRectangles(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
