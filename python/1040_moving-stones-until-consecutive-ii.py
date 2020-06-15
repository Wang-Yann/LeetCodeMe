#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个长度无限的数轴上，第 i 颗石子的位置为 stones[i]。如果一颗石子的位置最小/最大，那么该石子被称作端点石子。 
# 
#  每个回合，你可以将一颗端点石子拿起并移动到一个未占用的位置，使得该石子不再是一颗端点石子。 
# 
#  值得注意的是，如果石子像 stones = [1,2,5] 这样，你将无法移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），该
# 石子都仍然会是端点石子。 
# 
#  当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。 
# 
#  要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximu
# m_moves] 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[7,4,9]
# 输出：[1,2]
# 解释：
# 我们可以移动一次，4 -> 8，游戏结束。
# 或者，我们可以移动两次 9 -> 5，4 -> 6，游戏结束。
#  
# 
#  示例 2： 
# 
#  输入：[6,5,4,3,10]
# 输出：[2,3]
# 解释：
# 我们可以移动 3 -> 8，接着是 10 -> 7，游戏结束。
# 或者，我们可以移动 3 -> 7, 4 -> 8, 5 -> 9，游戏结束。
# 注意，我们无法进行 10 -> 2 这样的移动来结束游戏，因为这是不合要求的移动。
#  
# 
#  示例 3： 
# 
#  输入：[100,101,104,102,103]
# 输出：[0,0] 
# 
#  
# 
#  提示： 
# 
#  
#  3 <= stones.length <= 10^4 
#  1 <= stones[i] <= 10^9 
#  stones[i] 的值各不相同。 
#  
# 
#  
#  Related Topics 数组 Sliding Window

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        """
        https://leetcode-cn.com/problems/moving-stones-until-consecutive-ii/solution/jie-ti-si-lu-by-owenzzz/
        HARD
        """
        stones.sort()
        left, min_moves = 0, float("inf")
        N = len(stones)
        max_moves = max(stones[N - 1] - stones[1], stones[N - 2] - stones[0]) - (N - 2)
        for right in range(N):
            while stones[right] - stones[left] + 1 > N:  # find window size <= len(stones)
                left += 1
            if N - (right - left + 1) == 1 and stones[right] - stones[left] + 1 == N - 1:
                min_moves = min(min_moves, 2)  # case (1, 2, 3, 4), 7
            else:
                min_moves = min(min_moves, N - (right - left + 1))  # move stones not in this window
        return [min_moves, max_moves]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([7, 4, 9], [1, 2]),
    ([6, 5, 4, 3, 10], [2, 3]),
    ([100, 101, 104, 102, 103], [0, 0]),
])
def test_solutions(args, expected):
    assert Solution().numMovesStonesII(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
