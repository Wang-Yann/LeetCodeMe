#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 05:55:49
# @Last Modified : 2021-02-25 05:55:49
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。 
# 
#  你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。 
# 
#  当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时： 
# 
#  
#  如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块 
#  如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块 
#  
# 如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
# 输出：4
# 解释：从建筑物 0 出发，你可以按此方案完成旅程：
# - 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
# - 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
# - 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
# - 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
# 无法越过建筑物 4 ，因为没有更多砖块或梯子。
#  
# 
#  示例 2： 
# 
#  
# 输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# 输出：7
#  
# 
#  示例 3： 
# 
#  
# 输入：heights = [14,3,19,3], bricks = 17, ladders = 0
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= heights.length <= 105 
#  1 <= heights[i] <= 106 
#  0 <= bricks <= 109 
#  0 <= ladders <= heights.length 
#  
#  Related Topics 堆 二分查找 
#  👍 40 👎 0


import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """GOOD"""
        heap = []
        N = len(heights)
        for i in range(N - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return N - 1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1), 4],
    [dict(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2), 7],
    [dict(heights=[14, 3, 19, 3], bricks=17, ladders=0), 3],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().furthestBuilding(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
