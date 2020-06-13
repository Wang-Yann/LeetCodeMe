#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有一些工作：difficulty[i] 表示第i个工作的难度，profit[i]表示第i个工作的收益。 
# 
#  现在我们有一些工人。worker[i]是第i个工人的能力，即该工人只能完成难度小于等于worker[i]的工作。 
# 
#  每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。 
# 
#  举个例子，如果3个工人都尝试完成一份报酬为1的同样工作，那么总收益为 $3。如果一个工人不能完成任何工作，他的收益为 $0 。 
# 
#  我们能得到的最大收益是多少？ 
# 
#  示例： 
# 
#  输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# 输出: 100 
# 解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。 
# 
#  提示: 
# 
#  
#  1 <= difficulty.length = profit.length <= 10000 
#  1 <= worker.length <= 10000 
#  difficulty[i], profit[i], worker[i] 的范围是 [1, 10^5] 
#  
#  Related Topics 双指针

"""

import bisect
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        lookup = list(zip(difficulty, profit))
        lookup.sort()
        dp = {}
        max_profit = 0
        for d, p in lookup:
            max_profit = max(p, max_profit)
            dp[d] = max_profit
        # print(lookup)
        sorted_difficulty = [x[0] for x in lookup]
        ans = 0
        for w in worker:
            idx = bisect.bisect_left(sorted_difficulty, w)
            if idx >= len(sorted_difficulty) or sorted_difficulty[idx] > w:
                idx -= 1
            if idx < 0:
                continue
            ans += dp[sorted_difficulty[idx]]
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[4, 5, 6, 7]
    ), 100),
    (dict(
        difficulty=[85, 47, 57], profit=[24, 66, 99], worker=[40, 25, 25]
    ), 0),
    (dict(
        difficulty=[13, 37, 58], profit=[4, 90, 96], worker=[34, 73, 45]
    ), 190),
])
def test_solutions(kwargs, expected):
    assert Solution().maxProfitAssignment(**kwargs) == expected
    assert Solution1().maxProfitAssignment(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
