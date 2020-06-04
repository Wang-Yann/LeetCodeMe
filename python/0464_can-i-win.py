#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。 
# 
#  如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？ 
# 
#  例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。 
# 
#  给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳
# 赢（假设两位玩家游戏时都表现最佳）？ 
# 
#  你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。 
# 
#  示例： 
# 
#  输入：
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# 输出：
# false
# 
# 解释：
# 无论第一个玩家选择哪个整数，他都会失败。
# 第一个玩家可以选择从 1 到 10 的整数。
# 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
# 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
# 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
#  
#  Related Topics 极小化极大 动态规划

"""
import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def dfs(nums, desiredTotalVal):
            hash = str(nums)
            if hash in memo:
                return memo[hash]
            if nums[-1] >= desiredTotalVal:
                return True
            for i in range(len(nums)):
                if not dfs(nums[:i] + nums[i + 1:], desiredTotalVal - nums[i]):
                    memo[hash] = True
                    return True
            memo[hash] = False
            return False

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        memo = {}
        lst = list(range(1, maxChoosableInteger + 1))
        return dfs(lst, desiredTotal)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        @functools.lru_cache(None)
        def dfs(used, desiredTotal):
            for i in range(maxChoosableInteger):
                cur = 1 << i
                if cur & used == 0:
                    if desiredTotal <= i + 1 or not dfs(cur | used, desiredTotal - i - 1):
                        return True
            return False

        return dfs(0, desiredTotal)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        maxChoosableInteger=10,
        desiredTotal=11
    ), False),
])
def test_solutions(kwargs, expected):
    assert Solution().canIWin(**kwargs) == expected
    assert Solution1().canIWin(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
