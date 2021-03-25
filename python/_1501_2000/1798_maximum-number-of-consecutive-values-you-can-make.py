#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-22 02:40:38
# @Last Modified : 2021-03-22 02:40:38
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个长度为 n 的整数数组 coins ，它代表你拥有的 n 个硬币。第 i 个硬币的值为 coins[i] 。如果你从这些硬币中选出一部分硬币，它们的
# 和为 x ，那么称，你可以 构造 出 x 。 
# 
#  请返回从 0 开始（包括 0 ），你最多能 构造 出多少个连续整数。 
# 
#  你可能有多个相同值的硬币。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1,3]
# 输出：2
# 解释：你可以得到以下这些值：
# - 0：什么都不取 []
# - 1：取 [1]
# 从 0 开始，你可以构造出 2 个连续整数。 
# 
#  示例 2： 
# 
#  
# 输入：coins = [1,1,1,4]
# 输出：8
# 解释：你可以得到以下这些值：
# - 0：什么都不取 []
# - 1：取 [1]
# - 2：取 [1,1]
# - 3：取 [1,1,1]
# - 4：取 [4]
# - 5：取 [4,1]
# - 6：取 [4,1,1]
# - 7：取 [4,1,1,1]
# 从 0 开始，你可以构造出 8 个连续整数。 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,4,10,3,1]
# 输出：20 
# 
#  
# 
#  提示： 
# 
#  
#  coins.length == n 
#  1 <= n <= 4 * 104 
#  1 <= coins[i] <= 4 * 104 
#  
#  Related Topics 贪心算法 
#  👍 11 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        ans = 1
        for c in sorted(coins):
            if c > ans:
                break
            ans += c
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(coins=[1, 3]), 2],
    [dict(coins=[1, 1, 1, 4]), 8],
    [dict(coins=[1, 4, 10, 3, 1]), 20],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().getMaximumConsecutive(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
