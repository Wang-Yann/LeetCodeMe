#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-26 21:36:27
# @Last Modified : 2020-07-26 21:36:27
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 花园里有 N 个花盆，每个花盆里都有一朵花。这 N 朵花会在 N 天内依次开放，每天有且仅有一朵花会开放并且会一直盛开下去。 
# 
#  给定一个数组 flowers 包含从 1 到 N 的数字，每个数字表示在那一天开放的花所在的花盆编号。 
# 
#  例如， flowers[i] = x 表示在第 i+1 天盛开的花在第 x 个花盆中，i 和 x 都在 1 到 N 的范围内。 
# 
#  给你一个整数 k，请你输出在哪一天恰好有两朵盛开的花，他们中间间隔了 k 朵花并且都没有开放。 
# 
#  如果不存在，输出 -1。 
# 
#  
# 
#  样例 1: 
# 
#  输入: 
# flowers: [1,3,2]
# k: 1
# 输出: 2
# 解释: 在第二天，第一朵和第三朵花都盛开了。
#  
# 
#  
# 
#  样例 2: 
# 
#  输入: 
# flowers: [1,2,3]
# k: 1
# 输出: -1
#  
# 
#  
# 
#  注释 : 
# 
#  
#  给定的数组范围是 [1, 20000]。 
#  
# 
#  
#  Related Topics Ordered Map 
#  👍 24 👎 0

"""

import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        """
        贪心
        滑动窗口
        TODO

        """
        N = len(bulbs)
        days = [0] * N
        for day, pos in enumerate(bulbs):
            days[pos - 1] = day
        result = math.inf
        left, right = 0, K + 1
        i = 0
        while right < N:
            if days[i] < days[left] or days[i] <= days[right]:  # 当i位置的花开放时间较早
                if i == right:  # i移动到right，说明当前区间中没有花的开放时间早于左右端点
                    result = min(result, max(days[left], days[right]))  # 左右两端点选择较晚开放的，然后再选择每次更新最下答案
                left, right = i, K + 1 + i  # 更新区间端点
            i += 1
        return result + 1 if result != math.inf else -1


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    """
      滑动窗口
    """

    def kEmptySlots(self, bulbs, K):
        days = [0] * len(bulbs)
        for day, position in enumerate(bulbs, 1):
            days[position - 1] = day

        ans = float('inf')
        left, right = 0, K + 1
        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + K + 1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right + K + 1

        return ans if ans < float('inf') else -1


@pytest.mark.parametrize("kwargs,expected", [
    [dict(bulbs=[1, 3, 2], K=1), 2],
    pytest.param(dict(bulbs=[1, 2, 3], K=1), -1),
])
def test_solutions(kwargs, expected):
    assert Solution().kEmptySlots(**kwargs) == expected
    assert Solution1().kEmptySlots(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
