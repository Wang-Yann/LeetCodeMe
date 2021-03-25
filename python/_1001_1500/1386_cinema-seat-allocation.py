#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 
# 
#  如上图所示，电影院的观影厅中有 n 行座位，行编号从 1 到 n ，且每一行内总共有 10 个座位，列编号从 1 到 10 。 
# 
#  给你数组 reservedSeats ，包含所有已经被预约了的座位。比如说，researvedSeats[i]=[3,8] ，它表示第 3 行第 8 个座
# 位被预约了。 
# 
#  请你返回 最多能安排多少个 4 人家庭 。4 人家庭要占据 同一行内连续 的 4 个座位。隔着过道的座位（比方说 [3,3] 和 [3,4]）不是连续的座
# 位，但是如果你可以将 4 人家庭拆成过道两边各坐 2 人，这样子是允许的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# 输出：4
# 解释：上图所示是最优的安排方案，总共可以安排 4 个家庭。蓝色的叉表示被预约的座位，橙色的连续座位表示一个 4 人家庭。
#  
# 
#  示例 2： 
# 
#  输入：n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^9 
#  1 <= reservedSeats.length <= min(10*n, 10^4) 
#  reservedSeats[i].length == 2 
#  1 <= reservedSeats[i][0] <= n 
#  1 <= reservedSeats[i][1] <= 10 
#  所有 reservedSeats[i] 都是互不相同的。 
#  
#  Related Topics 贪心算法 数组

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        对于一个家庭而言，只有以下三种给他们安排座位的方法：
            安排位置 2，3，4，5；
            安排位置 4，5，6，7；
            安排位置 6，7，8，9。
        """
        # 被占用情况
        lookup = collections.defaultdict(lambda: [False]*3)
        for r, c in reservedSeats:
            if 2 <= c <= 5:
                lookup[r][0] = True
            if 4 <= c <= 7:
                lookup[r][1] = True
            if 6 <= c <= 9:
                lookup[r][2] = True
        res = 2 * n
        for a, b, c in lookup.values():
            if not a and not c:
                continue
            if not (a and b and c):
                res -= 1
                continue
            res -= 2
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]), 4],
    [dict(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]), 2],
    [dict(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]), 4],
])
def test_solutions(kw, expected):
    assert Solution().maxNumberOfFamilies(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
