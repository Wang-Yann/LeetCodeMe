#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。 
# 
#  每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。 
# 
#  找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：stones = [3,2,4,1], K = 2
# 输出：20
# 解释：
# 从 [3, 2, 4, 1] 开始。
# 合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
# 合并 [4, 1]，成本为 5，剩下 [5, 5]。
# 合并 [5, 5]，成本为 10，剩下 [10]。
# 总成本 20，这是可能的最小值。
#  
# 
#  示例 2： 
# 
#  输入：stones = [3,2,4,1], K = 3
# 输出：-1
# 解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
#  
# 
#  示例 3： 
# 
#  输入：stones = [3,5,1,2,6], K = 3
# 输出：25
# 解释：
# 从 [3, 5, 1, 2, 6] 开始。
# 合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
# 合并 [3, 8, 6]，成本为 17，剩下 [17]。
# 总成本 25，这是可能的最小值。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= stones.length <= 30 
#  2 <= K <= 30 
#  1 <= stones[i] <= 100 
#  
#  Related Topics 动态规划

"""
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def mergeStones(self, stones: List[int], K: int) -> int:
        """
        dp[i][j]代表 从i到j合并为最少堆的最小代价
         能合并时((j - i) % (K - 1) == 0)就合并，所以fi加上下标i到j区间合。 下标区间小于K时(j - i + 1 < K)无法合并
        
        """
        N = len(stones)
        if (N - 1) % (K - 1) != 0:
            return -1
        prefix = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix[i] = prefix[i - 1] + stones[i - 1]
        dp = [[0] * N for _ in range(N)]
        for l in range(K, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j, K - 1))
                if (l - 1) % (K - 1) == 0:
                    dp[i][j] += prefix[i + l] - prefix[i]
        # print(dp)
        return dp[0][N - 1]


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    """
    dp[i][j][k] 表示将 [i, j] 区间的石头缩小成 k 堆的最小体力花费
    GOOD
    """

    def mergeStones(self, stones, K):

        @functools.lru_cache(None)
        def dp(i, j, k):
            if i == j:
                return 0 if k == 1 else float("inf")
            else:
                if k == 1:
                    result = dp(i, j, K) + prefix[j + 1] - prefix[i]
                else:
                    result = float("inf")
                    for mid in range(i, j, K - 1):
                        result = min(result, dp(i, mid, 1) + dp(mid + 1, j, k - 1))
                return result

        N = len(stones)
        if (N - 1) % (K - 1)!=0:
            return -1
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)
        ans = dp(0, N - 1, 1)
        return ans if ans != float("inf") else 0


@pytest.mark.parametrize("kwargs,expected", [
    (dict(stones=[3, 2, 4, 1], K=2), 20),
    pytest.param(dict(stones=[3, 2, 4, 1], K=3), -1),
    pytest.param(dict(stones=[3, 5, 1, 2, 6], K=3), 25),
])
def test_solutions(kwargs, expected):
    assert Solution().mergeStones(**kwargs) == expected
    assert Solution1().mergeStones(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
