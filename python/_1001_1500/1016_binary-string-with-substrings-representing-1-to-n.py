#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二进制字符串 S（一个仅由若干 '0' 和 '1' 构成的字符串）和一个正整数 N，如果对于从 1 到 N 的每个整数 X，其二进制表示都是 S 的
# 子串，就返回 true，否则返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  输入：S = "0110", N = 3
# 输出：true
#  
# 
#  示例 2： 
# 
#  输入：S = "0110", N = 4
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 1000 
#  1 <= N <= 10^9 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for v in range(N, max(N // 2 - 1,1), -1):
            v_char = bin(v)[2:]
            if v_char not in S:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(S="1", N=1), True],
    [dict(S="0110", N=3), True],
    [dict(S="0110", N=4), False],
])
def test_solutions(kw, expected):
    assert Solution().queryString(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
