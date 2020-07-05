#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 21:39:26
# @Last Modified : 2020-07-05 21:39:26
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 target 。一开始，你有一个数组 A ，它的所有元素均为 1 ，你可以执行以下操作： 
# 
#  
#  令 x 为你数组里所有元素的和 
#  选择满足 0 <= i < target.size 的任意下标 i ，并让 A 数组里下标为 i 处的值为 x 。 
#  你可以重复该过程任意次 
#  
# 
#  如果能从 A 开始构造出目标数组 target ，请你返回 True ，否则返回 False 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = [9,3,5]
# 输出：true
# 解释：从 [1, 1, 1] 开始
# [1, 1, 1], 和为 3 ，选择下标 1
# [1, 3, 1], 和为 5， 选择下标 2
# [1, 3, 5], 和为 9， 选择下标 0
# [9, 3, 5] 完成
#  
# 
#  示例 2： 
# 
#  输入：target = [1,1,1,2]
# 输出：false
# 解释：不可能从 [1,1,1,1] 出发构造目标数组。
#  
# 
#  示例 3： 
# 
#  输入：target = [8,5]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  N == target.length 
#  1 <= target.length <= 5 * 10^4 
#  1 <= target[i] <= 10^9 
#  
#  Related Topics 贪心算法 
#  👍 42 👎 0

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isPossible(self, target: List[int]) -> bool:
        # (1) x + remain = y
        # (2) y + remain = total
        # (1) - (2) => x - y = y - total
        #           => x = 2*y - total
        total = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)
        while total != len(target):
            y = -heapq.heappop(max_heap)
            remain = total - y
            x = y - remain
            if x <= 0 or remain == 0:
                return False
            if x > remain:  # for case [1, 1000000000]
                x = x % remain + remain
            heapq.heappush(max_heap, -x)
            total = x + remain
        return True


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        A = [-a for a in target]
        heapq.heapify(A)
        while True:
            # print(A)
            a = -heapq.heappop(A)
            total -= a
            if a == 1 or total == 1:
                return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(A, -a)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        target=[9, 3, 5]
    ), True),
    pytest.param(dict(target=[8, 5]), True),
    pytest.param(dict(target=[1, 1000000000]), True),
    pytest.param(dict(target=[1, 1, 1, 2]), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isPossible(**kwargs) == expected
    assert Solution1().isPossible(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
