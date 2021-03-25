#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 19:34:14
# @Last Modified : 2021-02-27 19:34:14
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s ，返回 s 中 同构子字符串 的数目。由于答案可能很大，只需返回对 109 + 7 取余 后的结果。 
# 
#  同构字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同构字符串。 
# 
#  子字符串 是字符串中的一个连续字符序列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abbcccaa"
# 输出：13
# 解释：同构子字符串如下所列：
# "a"   出现 3 次。
# "aa"  出现 1 次。
# "b"   出现 2 次。
# "bb"  出现 1 次。
# "c"   出现 3 次。
# "cc"  出现 2 次。
# "ccc" 出现 1 次。
# 3 + 1 + 2 + 1 + 3 + 2 + 1 = 13 
# 
#  示例 2： 
# 
#  输入：s = "xy"
# 输出：2
# 解释：同构子字符串是 "x" 和 "y" 。 
# 
#  示例 3： 
# 
#  输入：s = "zzzzz"
# 输出：15
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 105 
#  s 由小写字符串组成 
#  
#  Related Topics 贪心算法 字符串 
#  👍 7 👎 0
  

"""

import itertools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def countHomogenous(self, s: str) -> int:
        """AC"""
        ans = 0
        for char, grp in itertools.groupby(s):
            cnt = len(list(grp))
            ans += cnt * (cnt + 1) // 2
        MOD = 10 ** 9 + 7
        return ans % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="abbcccaa"), 13],
    [dict(s="xy"), 2],
    [dict(s="zzzzz"), 15],
    [dict(s="a" + "z" * (10 ** 5)), 49966],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().countHomogenous(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
