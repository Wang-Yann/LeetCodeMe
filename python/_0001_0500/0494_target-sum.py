#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选
# 择一个符号添加在前面。 
# 
#  返回可以使最终数组和为目标数 S 的所有添加符号的方法数。 
# 
#  示例 1: 
# 
#  输入: nums: [1, 1, 1, 1, 1], S: 3
# 输出: 5
# 解释: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# 一共有5种方法让最终目标和为3。
#  
# 
#  注意: 
# 
#  
#  数组非空，且长度不会超过20。 
#  初始的数组的和不会超过1000。 
#  保证返回的最终结果能被32位整数存下。 
#  
#  Related Topics 深度优先搜索 动态规划

"""
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        https://leetcode-cn.com/problems/target-sum/solution/0-1bei-bao-you-hua-jie-fa-by-sunrise-z/
        sum(a)+sum(b)=sum(nums)
        sum(a)-sum(b)=S
        a代表所有非负数组，b代表所有非正数组，
        一正一负，正的和负的绝对值为总和，正的-负的为我们的目标S
        那么可以求得sum(a) = (sum(nums)+S) /2
        即在数组nums中取子集，满足子集的和为(sum(nums)+S) /2，看看这样的条件有多少种
        转化为　0-1 背包

        二维的话
        dp[i][j] = x 表示，若只在前 i 个物品中选择，若当前背包的容量为 j，则最多有 x 种方法可以恰好装满背包
        dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]];

        """
        total = sum(nums)
        if total < S:
            return 0
        tmp = total + S
        if tmp & 0b1:
            return 0
        target = tmp // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for v in range(target, num - 1, -1):
                dp[v] += dp[v - num]
        return dp[target]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        初始版本　 超时
        优化后可以过
        """
        N = len(nums)

        @functools.lru_cache(None)
        def dfs(i, cur_sum):
            ans = 0
            if i == N:
                if cur_sum == S:
                    return 1
            else:
                ans += dfs(i + 1, cur_sum + nums[i]) + dfs(i + 1, cur_sum - nums[i])
            return ans

        return dfs(0, 0)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 1, 1, 1, 1], S=3), 5],
])
def test_solutions(kw, expected):
    assert Solution().findTargetSumWays(**kw) == expected
    assert Solution1().findTargetSumWays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
