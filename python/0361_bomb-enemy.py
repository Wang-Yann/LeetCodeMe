#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 14:35:52
# @Last Modified : 2020-07-28 14:35:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 想象一下炸弹人游戏，在你面前有一个二维的网格来表示地图，网格中的格子分别被以下三种符号占据： 
# 
#  
#  'W' 表示一堵墙 
#  'E' 表示一个敌人 
#  '0'（数字 0）表示一个空位 
#  
# 
#  
# 
#  请你计算一个炸弹最多能炸多少敌人。 
# 
#  由于炸弹的威力不足以穿透墙体，炸弹只能炸到同一行和同一列没被墙体挡住的敌人。 
# 
#  注意：你只能把炸弹放在一个空的格子里 
# 
#  示例: 
# 
#  输入: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# 输出: 3 
# 解释: 对于如下网格
# 
# 0 E 0 0 
# E 0 W E 
# 0 E 0 0
# 
# 假如在位置 (1,1) 放置炸弹的话，可以炸到 3 个敌人
#  
#  Related Topics 动态规划 
#  👍 25 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        left = [[0 for i in range(C + 1)] for j in range(R + 1)]
        right = [[0 for i in range(C + 2)] for j in range(R + 2)]
        up = [[0 for i in range(C + 1)] for j in range(R + 1)]
        down = [[0 for i in range(C + 2)] for j in range(R + 2)]

        # left
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if grid[i - 1][j - 1] == 'E':
                    left[i][j] = left[i][j - 1] + 1
                elif grid[i - 1][j - 1] == 'W':
                    left[i][j] = 0
                else:
                    left[i][j] = left[i][j - 1]

        # right
        for i in range(1, R + 1):
            for j in range(C, 0, -1):
                if grid[i - 1][j - 1] == 'E':
                    right[i][j] = right[i][j + 1] + 1
                elif grid[i - 1][j - 1] == 'W':
                    right[i][j] = 0
                else:
                    right[i][j] = right[i][j + 1]

        # up
        for j in range(1, C + 1):
            for i in range(1, R + 1):
                if grid[i - 1][j - 1] == 'E':
                    up[i][j] = up[i - 1][j] + 1
                elif grid[i - 1][j - 1] == 'W':
                    up[i][j] = 0
                else:
                    up[i][j] = up[i - 1][j]

        # down
        for j in range(1, C + 1):
            for i in range(R, 0, -1):
                if grid[i - 1][j - 1] == 'E':
                    down[i][j] = down[i + 1][j] + 1
                elif grid[i - 1][j - 1] == 'W':
                    down[i][j] = 0
                else:
                    down[i][j] = down[i + 1][j]

        result = 0

        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if grid[i - 1][j - 1] == '0':
                    result = max(result, left[i][j] + right[i][j] + up[i][j] + down[i][j])

        return result


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def maxKilledEnemies(self, grid):
        """
        在论坛里看到了史蒂芬大神提出的另一种解法，感觉挺巧妙，就搬了过来。这种解法比较省空间，写法也比较简洁，
        需要一个 rowCnt 变量，用来记录到下一个墙之前的敌人个数。还需要一个数组 colCnt，其中 colCnt[j] 表示第j列到下一个墙之前的敌人个数。
        算法思路是遍历整个数组 grid，对于一个位置 grid[i][j]，对于水平方向，如果当前位置是开头一个或者前面一个是墙壁，
        开始从当前位置往后遍历，遍历到末尾或者墙的位置停止，计算敌人个数。对于竖直方向也是同样，如果当前位置是开头一个或者上面一个是墙壁，
        开始从当前位置向下遍历，遍历到末尾或者墙的位置停止，计算敌人个数。可能会有人有疑问，为啥 rowCnt 就可以用一个变量，
        而 colCnt 就需要用一个数组呢，为啥 colCnt 不能也用一个变量呢？原因是由遍历顺序决定的，这里是逐行遍历的，
        在每行的开头就统计了该行的敌人总数，所以再该行遍历没必要用数组，但是每次移动时就会换到不同的列，总不能没换个列就重新统计一遍吧，
        所以就在第一行时一起统计了存到数组中供后来使用。有了水平方向和竖直方向敌人的个数，
        那么如果当前位置是0，表示可以放炸弹，更新结果 res 即可
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        result, rows = 0, 0
        cols = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    rows = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            rows += 1

                if i == 0 or grid[i - 1][j] == 'W':
                    cols[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            cols[j] += 1

                if grid[i][j] == '0' and rows + cols[j] > result:
                    result = rows + cols[j]

        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(grid=[
        ["0", "E", "0", "0"],
        ["E", "0", "W", "E"],
        ["0", "E", "0", "0"]
    ]), 3],
])
def test_solutions(kw, expected):
    assert Solution().maxKilledEnemies(**kw) == expected
    assert Solution1().maxKilledEnemies(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
