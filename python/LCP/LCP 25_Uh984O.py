#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 22:49:57
# @Last Modified : 2021-02-22 22:49:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 小扣在秋日市集购买了一个古董键盘。由于古董键盘年久失修，键盘上只有 26 个字母 **a~z** 可以按下，且每个字母最多仅能被按 `k` 次。
# 
# 小扣随机按了 `n` 次按键，请返回小扣总共有可能按出多少种内容。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。
# 
# 
# **示例 1：**
# >输入：`k = 1, n = 1`
# > 
# >输出：`26`
# > 
# >解释：由于只能按一次按键，所有可能的字符串为 "a", "b", ... "z" 
# 
# **示例 2：**
# >输入：`k = 1, n = 2`
# > 
# >输出：`650`
# > 
# >解释：由于只能按两次按键，且每个键最多只能按一次，所有可能的字符串（按字典序排序）为 "ab", "ac", ... "zy" 
# 
# **提示：**
# - `1 <= k <= 5`
# - `1 <= n <= 26*k`
#  
# 
#  👍 19 👎 0
  

"""

import functools

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
try:
    from math import comb
except:
    from scipy.special import comb


class Solution:

    def keyboard(self, k: int, n: int) -> int:
        MOD = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(choices, cur_n):
            if cur_n == 0:
                return 1
            if choices <= 0:
                return 0
            res = 0
            for i in range(0, min(cur_n, k) + 1):
                res += int(comb(cur_n, i)) * dfs(choices - 1, cur_n - i) % MOD
            return res % MOD

        return dfs(26, n)

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(k=1, n=1), 26],
    pytest.param(dict(k=1, n=2), 650),
])
@pytest.mark.parametrize("SolutionCLS", [
    Solution,
])
def test_solutions(kwargs, expected, SolutionCLS):
    assert SolutionCLS().keyboard(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
