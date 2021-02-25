#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 05:49:57
# @Last Modified : 2021-02-25 05:49:57
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。 
# 
#  字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 1
# 输出：5
# 解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2
# 输出：15
# 解释：仅由元音组成的 15 个字典序字符串为
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
# 注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 33
# 输出：66045
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 50 
#  
#  Related Topics 数学 动态规划 回溯算法 
#  👍 39 👎 0


import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        dp[n][k] means the number of strings constructed by at most k different characters
        """

        @functools.lru_cache(None)
        def dp(n, k):
            if k == 1 or n == 1:
                return k
            return sum(dp(n - 1, k) for k in range(1, k + 1))

        return dp(n, 5)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=1), 5],
    [dict(n=2), 15],
    [dict(n=33), 66045],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().countVowelStrings(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
