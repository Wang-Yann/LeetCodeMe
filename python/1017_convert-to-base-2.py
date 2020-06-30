#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出数字 N，返回由若干 "0" 和 "1"组成的字符串，该字符串为 N 的负二进制（base -2）表示。 
# 
#  除非字符串就是 "0"，否则返回的字符串中不能含有前导零。 
# 
#  
# 
#  示例 1： 
# 
#  输入：2
# 输出："110"
# 解释：(-2) ^ 2 + (-2) ^ 1 = 2
#  
# 
#  示例 2： 
# 
#  输入：3
# 输出："111"
# 解释：(-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
#  
# 
#  示例 3： 
# 
#  输入：4
# 输出："100"
# 解释：(-2) ^ 2 = 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= N <= 10^9 
#  
#  Related Topics 数学

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def baseNeg2(self, N: int) -> str:
        res = []
        while N:
            # print(N&1,-N&1)
            # -N&1 N&1等同
            res.append(str(N & 1))  # N%-2
            N = -(N >> 1)  # N//-2
        return "".join(reversed(res)) if res else "0"


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def baseNeg2(self, N):
        BASE = -2
        result = []
        while N:
            N, r = divmod(N, BASE)
            # print(N, r)
            if r < 0:
                r -= BASE
                N += 1
            result.append(str(r))
        result.reverse()
        return "".join(result) if result else "0"


@pytest.mark.parametrize("args,expected", [
    (2, "110"),
    (3, "111"),
    (4, "100"),
])
def test_solutions(args, expected):
    assert Solution().baseNeg2(args) == expected
    assert Solution1().baseNeg2(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
