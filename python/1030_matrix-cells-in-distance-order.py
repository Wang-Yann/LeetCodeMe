#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。 
# 
#  另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。 
# 
#  返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈
# 顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。） 
# 
#  
# 
#  示例 1： 
# 
#  输入：R = 1, C = 2, r0 = 0, c0 = 0
# 输出：[[0,0],[0,1]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1]
#  
# 
#  示例 2： 
# 
#  输入：R = 2, C = 2, r0 = 0, c0 = 1
# 输出：[[0,1],[0,0],[1,1],[1,0]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
# [[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
#  
# 
#  示例 3： 
# 
#  输入：R = 2, C = 3, r0 = 1, c0 = 2
# 输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
# 其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= R <= 100 
#  1 <= C <= 100 
#  0 <= r0 < R 
#  0 <= c0 < C 
#  
#  Related Topics 排序

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        data = [[x, y] for x in range(R) for y in range(C)]
        data.sort(key=lambda p: abs(p[0] - r0) + abs(p[1] - c0))
        return data


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(R=1, C=2, r0=0, c0=0), [[0, 0], [0, 1]]],
    [dict(R=2, C=2, r0=0, c0=1), [[0, 1], [0, 0], [1, 1], [1, 0]]],
    [dict(R=2, C=3, r0=1, c0=2), [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]],
    [dict(R=3, C=5, r0=2, c0=3),
     [[2, 3], [1, 3], [2, 2], [2, 4], [0, 3],
      [1, 2], [1, 4], [2, 1], [0, 2], [0, 4],
      [1, 1], [2, 0], [0, 1], [1, 0], [0, 0]]],
])
def test_solutions(kw, expected):
    assert Solution().allCellsDistOrder(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
