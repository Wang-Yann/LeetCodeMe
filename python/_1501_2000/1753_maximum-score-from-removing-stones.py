#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 17:32:13
# @Last Modified : 2021-02-27 17:32:13
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你正在玩一个单人游戏，面前放置着大小分别为 a、b 和 c 的 三堆 石子。 
# 
#  每回合你都要从两个 不同的非空堆 中取出一颗石子，并在得分上加 1 分。当存在 两个或更多 的空堆时，游戏停止。 
# 
#  给你三个整数 a 、b 和 c ，返回可以得到的 最大分数 。 
#  
# 
#  示例 1： 
# 
#  
# 输入：a = 2, b = 4, c = 6
# 输出：6
# 解释：石子起始状态是 (2, 4, 6) ，最优的一组操作是：
# - 从第一和第三堆取，石子状态现在是 (1, 4, 5)
# - 从第一和第三堆取，石子状态现在是 (0, 4, 4)
# - 从第二和第三堆取，石子状态现在是 (0, 3, 3)
# - 从第二和第三堆取，石子状态现在是 (0, 2, 2)
# - 从第二和第三堆取，石子状态现在是 (0, 1, 1)
# - 从第二和第三堆取，石子状态现在是 (0, 0, 0)
# 总分：6 分 。
#  
# 
#  示例 2： 
# 
#  
# 输入：a = 4, b = 4, c = 6
# 输出：7
# 解释：石子起始状态是 (4, 4, 6) ，最优的一组操作是：
# - 从第一和第二堆取，石子状态现在是 (3, 3, 6)
# - 从第一和第三堆取，石子状态现在是 (2, 3, 5)
# - 从第一和第三堆取，石子状态现在是 (1, 3, 4)
# - 从第一和第三堆取，石子状态现在是 (0, 3, 3)
# - 从第二和第三堆取，石子状态现在是 (0, 2, 2)
# - 从第二和第三堆取，石子状态现在是 (0, 1, 1)
# - 从第二和第三堆取，石子状态现在是 (0, 0, 0)
# 总分：7 分 。
#  
# 
#  示例 3： 
# 
#  
# 输入：a = 1, b = 8, c = 8
# 输出：8
# 解释：最优的一组操作是连续从第二和第三堆取 8 回合，直到将它们取空。
# 注意，由于第二和第三堆已经空了，游戏结束，不能继续从第一堆中取石子。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a, b, c <= 105 
#  
#  Related Topics 堆 数学 
#  👍 13 👎 0
  

"""

import heapq

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maximumScore(self, a: int, b: int, c: int) -> int:
        ans = 0
        heap = [-a, -b, -c]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x * y <= 0:
                continue
            ans += 1
            if x + 1 < 0:
                heapq.heappush(heap, x + 1)
            if y + 1 < 0:
                heapq.heappush(heap, y + 1)

        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted((a, b, c))
        if a + b < c:
            return a + b
        return (a + b + c) // 2


@pytest.mark.parametrize("kw,expected", [
    [dict(a=2, b=4, c=6), 6],
    [dict(a=4, b=4, c=6), 7],
    [dict(a=1, b=8, c=8), 8],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().maximumScore(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
