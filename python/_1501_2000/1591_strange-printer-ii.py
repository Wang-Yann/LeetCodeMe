#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 05:51:09
# @Last Modified : 2021-02-22 05:51:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个奇怪的打印机，它有如下两个特殊的打印规则： 
# 
#  
#  每一次操作时，打印机会用同一种颜色打印一个矩形的形状，每次打印会覆盖矩形对应格子里原本的颜色。 
#  一旦矩形根据上面的规则使用了一种颜色，那么 相同的颜色不能再被使用 。 
#  
# 
#  给你一个初始没有颜色的 m x n 的矩形 targetGrid ，其中 targetGrid[row][col] 是位置 (row, col) 的颜色。
#  
# 
#  如果你能按照上述规则打印出矩形 targetGrid ，请你返回 true ，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
# 输出：true
#  
# 
#  示例 3： 
# 
#  输入：targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
# 输出：false
# 解释：没有办法得到 targetGrid ，因为每一轮操作使用的颜色互不相同。 
# 
#  示例 4： 
# 
#  输入：targetGrid = [[1,1,1],[3,1,3]]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == targetGrid.length 
#  n == targetGrid[i].length 
#  1 <= m, n <= 60 
#  1 <= targetGrid[row][col] <= 60 
#  
#  Related Topics 贪心算法 
#  👍 13 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        """
        拓扑排序也可
        For each color, find its index of left most, top most, right most, bottom most point.
        Then we need to paint this color from [top, left] to [bottom, right].

        If in the rectangle, all the colors are either the same or 0,
        we mark all of them to 0.

        If we can mark the whole grid to 0, it means the target if printable.
        """
        R, C = len(targetGrid), len(targetGrid[0])
        pos = [[R, C, 0, 0] for i in range(61)]
        colors = set()
        for i in range(R):
            for j in range(C):
                c = targetGrid[i][j]
                colors.add(c)
                pos[c][0] = min(pos[c][0], i)
                pos[c][1] = min(pos[c][1], j)
                pos[c][2] = max(pos[c][2], i)
                pos[c][3] = max(pos[c][3], j)

        def test(color):
            for i in range(pos[color][0], pos[color][2] + 1):
                for j in range(pos[color][1], pos[color][3] + 1):
                    if targetGrid[i][j] > 0 and targetGrid[i][j] != color:
                        return False
            for i in range(pos[color][0], pos[color][2] + 1):
                for j in range(pos[color][1], pos[color][3] + 1):
                    targetGrid[i][j] = 0
            return True

        while colors:
            colors2 = set()
            for c in colors:
                if not test(c):
                    colors2.add(c)
            if len(colors2) == len(colors):
                return False
            colors = colors2
        return True


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(targetGrid=[[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]), True],
    [dict(targetGrid=[[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]]), True],
    [dict(targetGrid=[[1, 2, 1], [2, 1, 2], [1, 2, 1]]), False],
    [dict(targetGrid=[[1, 1, 1], [3, 1, 3]]), False],
])
def test_solutions(kw, expected):
    assert Solution().isPrintable(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
