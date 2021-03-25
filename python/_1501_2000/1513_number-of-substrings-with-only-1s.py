#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 23:32:06
# @Last Modified : 2020-07-16 23:32:06
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。 
# 
#  返回所有字符都为 1 的子字符串的数目。 
# 
#  由于答案可能很大，请你将它对 10^9 + 7 取模后返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "0110111"
# 输出：9
# 解释：共有 9 个子字符串仅由 '1' 组成
# "1" -> 5 次
# "11" -> 3 次
# "111" -> 1 次 
# 
#  示例 2： 
# 
#  输入：s = "101"
# 输出：2
# 解释：子字符串 "1" 在 s 中共出现 2 次
#  
# 
#  示例 3： 
# 
#  输入：s = "111111"
# 输出：21
# 解释：每个子字符串都仅由 '1' 组成
#  
# 
#  示例 4： 
# 
#  输入：s = "000"
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  s[i] == '0' 或 s[i] == '1' 
#  1 <= s.length <= 10^5 
#  
#  Related Topics 数学 字符串 
#  👍 2 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        return sum(len(a) * (len(a) + 1) // 2 for a in s.split("0")) % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="0110111"), 9],

    pytest.param(dict(s="101"), 2),
    pytest.param(dict(s="111111"), 21),
    pytest.param(dict(s="000"), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().numSub(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
