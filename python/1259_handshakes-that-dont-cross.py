#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 11:08:14
# @Last Modified : 2020-08-07 11:08:14
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 偶数 个人站成一个圆，总人数为 num_people 。每个人与除自己外的一个人握手，所以总共会有 num_people / 2 次握手。 
# 
#  将握手的人之间连线，请你返回连线不会相交的握手方案数。 
# 
#  由于结果可能会很大，请你返回答案 模 10^9+7 后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：num_people = 2
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：num_people = 4
# 输出：2
# 解释：总共有两种方案，第一种方案是 [(1,2),(3,4)] ，第二种方案是 [(2,3),(4,1)] 。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：num_people = 6
# 输出：5
#  
# 
#  示例 4： 
# 
#  输入：num_people = 8
# 输出：14
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= num_people <= 1000 
#  num_people % 2 == 0 
#  
#  Related Topics 数学 动态规划 
#  👍 12 👎 0

"""
import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        """
        https://leetcode-cn.com/problems/handshakes-that-dont-cross/solution/dp-by-mike-meng-16/
        1.从1~n-1中任选一条线，将节点分割为两部分，分割两部分的排列组合之积。
        2.我们选择最后一个人作为起点，由于所有的人不能存在相交，编号为n的人选择握手的人的编号只能为1,3,5,7,...,n-1,同时将图分为两部分，
        左边有j-1个，共有dp[j-1]种握手排列组合方案，右边有n-j-1个人，则他们共有dp[n-j-1]种握手方案，
        所以总的握手组合的方案数为dp[j-1]*dp[n-j-1]

        """
        MOD = 10 ** 9 + 7
        N = num_people
        dp = [1] * (N + 1)
        for i in range(2, N + 1, 2):
            dp[i] = 0
            for j in range(1, i, 2):
                dp[i] = (dp[i] + dp[j - 1] * dp[i - j - 1]) % MOD
        return dp[N]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def numberOfWays(self, num_people: int) -> int:
        MOD = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(n):
            if n in (0, 2):
                return 1
            res = 0
            for i in range(1, n, 2):
                res += dfs(i - 1) * dfs(n - i - 1)
            return res % MOD

        return dfs(num_people)


@pytest.mark.parametrize("kw,expected", [
    [dict(num_people=2), 1],
    [dict(num_people=4), 2],
    [dict(num_people=6), 5],
    [dict(num_people=8), 14],
])
def test_solutions(kw, expected):
    assert Solution().numberOfWays(**kw) == expected
    assert Solution1().numberOfWays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
