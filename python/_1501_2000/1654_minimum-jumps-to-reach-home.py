#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 08:35:54
# @Last Modified : 2021-02-25 08:35:54
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。 
# 
#  跳蚤跳跃的规则如下： 
# 
#  
#  它可以 往前 跳恰好 a 个位置（即往右跳）。 
#  它可以 往后 跳恰好 b 个位置（即往左跳）。 
#  它不能 连续 往后跳 2 次。 
#  它不能跳到任何 forbidden 数组中的位置。 
#  
# 
#  跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。 
# 
#  给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃
# 次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# 输出：3
# 解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
#  
# 
#  示例 2： 
# 
#  
# 输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# 输出：-1
#  
# 
#  示例 3： 
# 
#  
# 输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# 输出：2
# 解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= forbidden.length <= 1000 
#  1 <= a, b, forbidden[i] <= 2000 
#  0 <= x <= 2000 
#  forbidden 中所有位置互不相同。 
#  位置 x 不在 forbidden 中。 
#  
#  Related Topics 广度优先搜索 动态规划 
#  👍 16 👎 0


import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        dq = collections.deque()
        dq.append((0, 0, False))
        while dq:
            cur, steps, used = dq.popleft()
            if cur == x:
                return steps
            if cur + a < 6000 and cur + a not in forbidden:
                # 6000是往右探索的最大值，x最大为2000
                forbidden.add(cur + a)
                dq.append((cur + a, steps + 1, False))
            if not used and cur - b > 0 and cur - b not in forbidden:
                # forbidden.add(cur-b)
                # 这里不能forbidden，因为后退回cur-b处时，无法覆盖前进到cur-b再后退到cur-2b的情况。
                dq.append((cur - b, steps + 1, True))
        return -1


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """
        Me
        """
        forbidden_set = set(forbidden)
        dq = collections.deque([(0, 1)])
        dest = x
        step = 0
        LIMIT = 2000 + a + b
        while dq:
            for _ in range(len(dq)):
                pos, d = dq.popleft()
                if pos == dest:
                    return step
                if pos + a not in forbidden_set and pos + a < LIMIT:
                    dq.append((pos + a, 1))
                    forbidden_set.add(pos + a)
                if d != -1 and pos - b > 0 and pos - b not in forbidden_set:
                    dq.append((pos - b, -1))
            step += 1
        return -1


@pytest.mark.parametrize("kw,expected", [
    [dict(forbidden=[14, 4, 18, 1, 15], a=3, b=15, x=9), 3],
    [dict(forbidden=[8, 3, 16, 6, 12, 20], a=15, b=13, x=11), -1],
    [dict(forbidden=[1, 6, 2, 14, 5, 17, 4], a=16, b=9, x=7), 2],
    [dict(forbidden=[18, 13, 3, 9, 8, 14], a=3, b=8, x=6), -1],
    [dict(forbidden=[162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36,
                     103, 149, 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176,
                     16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98], a=29, b=98, x=80), 121],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().minimumJumps(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
