#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 23:38:06
# @Last Modified : 2021-02-25 23:38:06
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数 n ，请你将 1 到 n 的二进制表示连接起来，并返回连接结果对应的 十进制 数字对 109 + 7 取余的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 1
# 输出：1
# 解释：二进制的 "1" 对应着十进制的 1 。
#  
# 
#  示例 2： 
# 
#  输入：n = 3
# 输出：27
# 解释：二进制下，1，2 和 3 分别对应 "1" ，"10" 和 "11" 。
# 将它们依次连接，我们得到 "11011" ，对应着十进制的 27 。
#  
# 
#  示例 3： 
# 
#  输入：n = 12
# 输出：505379714
# 解释：连接结果为 "1101110010111011110001001101010111100" 。
# 对应的十进制数字为 118505380540 。
# 对 109 + 7 取余后，结果为 505379714 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 105 
#  
#  Related Topics 数学 
#  👍 20 👎 0
  

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        ans = shift = 0
        for i in range(1, n + 1):
            # ans 表示答案，shift 表示 len_{2}(i)
            if (i & (i - 1)) == 0:
                shift += 1
            ans = ((ans << shift) + i) % MOD
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def concatenatedBinary(self, n):
        ans, M = 0, 10 ** 9 + 7
        for x in range(1, n + 1):
            ans = (ans * (1 << (len(bin(x)) - 2)) + x) % M
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(n=1), 1],
    [dict(n=3), 27],
    [dict(n=12), 505379714],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().concatenatedBinary(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
