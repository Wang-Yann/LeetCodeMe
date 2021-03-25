#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值
# 求平均，如果周围的单元格不足八个，则尽可能多的利用它们。 
# 
#  示例 1: 
# 
#  
# 输入:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# 输出:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
#  
# 
#  注意: 
# 
#  
#  给定矩阵中的整数范围为 [0, 255]。 
#  矩阵的长和宽的范围均为 [1, 150]。 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not M:
            return []
        m, n = len(M), len(M[0])
        ans = [[0] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1), (0, 0)]
        for i in range(m):
            for j in range(n):
                neighbors = [M[i + x][j + y] for x, y in directions
                             if 0 <= i + x <= m - 1 and 0 <= j + y <= n - 1]
                ans[i][j] = sum(neighbors) // len(neighbors)
        # print(ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]
            ,
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    ),
    (
            [[2, 2, 1],
             [2, 2, 1],
             [1, 1, 1]]
            ,
            [[2, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    ),
])
def test_solutions(args, expected):
    assert Solution().imageSmoother(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
