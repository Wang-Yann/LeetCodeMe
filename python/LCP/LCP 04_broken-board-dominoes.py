#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-15 23:21:43
# @Last Modified : 2020-07-15 23:21:43
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2的多米诺骨牌，你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块
# 骨牌？这些骨牌可以横着或者竖着放。 
# 
#  
# 
#  输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。 
# 
#  输出：一个整数，代表最多能在棋盘上放的骨牌数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2, m = 3, broken = [[1, 0], [1, 1]]
# 输出：2
# 解释：我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图） 
# 
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：n = 3, m = 3, broken = []
# 输出：4
# 解释：下图是其中一种可行的摆放方式
#  
# 
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n <= 8 
#  1 <= m <= 8 
#  0 <= b <= n * m 
#  
#  👍 31 👎 0


"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        """
        TODO
        将相邻格点染成不同颜色，之后求两种颜色格点构成二分图的最大匹配
        """
        nb = collections.defaultdict(list)
        broken = set(x * m + y for x, y in broken)
        for i in range(n):
            for j in range(m):
                if i * m + j in broken:
                    continue
                t = (i + j) & 1
                if i < n - 1 and (i + 1) * m + j not in broken:
                    nb[(i + t) * m + j].append((i + 1 - t) * m + j)
                if j < m - 1 and i * m + j + 1 not in broken:
                    nb[i * m + j + t].append(i * m + j + 1 - t)
        match = {}

        # print(nb)

        def find(x, v):
            for y in nb[x]:
                if y not in v:
                    v.add(y)
                    if y not in match or find(match[y], v):
                        match[y] = x
                        return True
            return False

        return sum(find(x, set()) for x in nb)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=2, m=3, broken=[[1, 0], [1, 1]]), 2],

    pytest.param(dict(n=3, m=3, broken=[]), 4),
])
def test_solutions(kwargs, expected):
    assert Solution().domino(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
