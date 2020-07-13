#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 09:37:20
# @Last Modified : 2020-04-23 09:37:20
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import pytest


class Solution:
    def waysToChangeMe(self, n: int) -> int:
        """超出时间限制"""
        choices = [25, 10, 5, 1]
        choices_cnt = 4
        ans = 0

        def dfs(first, total):
            nonlocal ans
            if total == n:
                ans += 1
                return
            elif total > n:
                return
            else:
                for i in range(first, choices_cnt):
                    dfs(i, total + choices[i])

        dfs(0, 0)
        # print(ans)
        return ans % 1000000007

    def waysToChange(self, n: int) -> int:
        """
         v -> volume | c->cost
            完全背包问题　TODO
            数学法也可以
            f(i,v)=f(i−1,v)+f(i,v−ci)
            我们用 f(i, v) 来表示前 i 种物品构成面值为 v 的方案数量
            见`背包九讲`
​
        """
        choices = [25, 10, 5, 1]
        dp = [1] + [0] * n
        for cost in choices:
            for v_idx in range(cost, n + 1):
                dp[v_idx] += dp[v_idx - cost]

        return dp[n] % 1000000007


@pytest.mark.parametrize("args,expected", [
    (5, 2),
    (10, 4),
    (23, 9),
    (852, 88537),
])
def test_solutions(args, expected):
    assert Solution().waysToChange(args) == expected
    # assert Solution().waysToChangeMe(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
