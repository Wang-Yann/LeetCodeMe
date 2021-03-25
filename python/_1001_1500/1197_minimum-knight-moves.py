#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 15:58:37
# @Last Modified : 2020-08-05 15:58:37
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一个坐标可以从 -infinity 延伸到 +infinity 的 无限大的 棋盘上，你的 骑士 驻扎在坐标为 [0, 0] 的方格里。 
# 
#  骑士的走法和中国象棋中的马相似，走 “日” 字：即先向左（或右）走 1 格，再向上（或下）走 2 格；或先向左（或右）走 2 格，再向上（或下）走 1 格
# 。 
# 
#  每次移动，他都可以按图示八个方向之一前进。 
# 
#  
# 
#  现在，骑士需要前去征服坐标为 [x, y] 的部落，请你为他规划路线。 
# 
#  最后返回所需的最小移动次数即可。本题确保答案是一定存在的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：x = 2, y = 1
# 输出：1
# 解释：[0, 0] → [2, 1]
#  
# 
#  示例 2： 
# 
#  输入：x = 5, y = 5
# 输出：4
# 解释：[0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  |x| + |y| <= 300 
#  
#  Related Topics 广度优先搜索 
#  👍 24 👎 0

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """AC"""
        source = (0, 0)
        seen = {source}
        dq = collections.deque([source])
        level = 0
        while dq:
            l = len(dq)
            for _ in range(l):
                i, j = dq.popleft()
                if i == x and j == y:
                    return level
                for dx, dy in [(-1, -2), (-2, -1), (-1, 2), (2, -1), (1, -2), (-2, 1), (1, 2), (2, 1)]:
                    nx, ny = i + dx, j + dy
                    if (nx, ny) not in seen:
                        dq.append((nx, ny))
                        seen.add((nx, ny))
            level += 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(x=2, y=1), 1],
    [dict(x=5, y=5), 4],
])
def test_solutions(kw, expected):
    assert Solution().minKnightMoves(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
