#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。 
# 
#  示例 1: 
# 
#  输入: 5
# 输出: 5
# 解释: 
# 下面是带有相应二进制表示的非负整数<= 5：
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# 其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。 
# 
#  说明: 1 <= n <= 10**9
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findIntegers(self, num: int) -> int:
        """
        对应于结尾+　'0' 和 +'01'
        数字n转化为01字符串,从前向后遍历，fi表示当前i为'1'时，i位其右侧01串排列的合法方案。
       f(i)=f(i-1)+f(i-2)，此处求出i位的右侧的01串排列的合法方案，可以由i - 1时尾部加上一个'0'转移到i，可以由i - 2时尾部加上'01'转移到i。
        从高位向低位遍历，每次遇到为'1'的位时，加上fi即可，遇到连续两个'1'时，返回即可
        """
        if num < 2:
            return num + 1
        s = bin(num).replace("0b", "")[::-1]
        length = len(s)
        dp = [0] * length
        dp[0] = 1
        dp[1] = 2
        for i in range(2, length):
            dp[i] = dp[i - 1] + dp[i - 2]
        ans = 0
        # print(dp,s)
        for i in range(length - 1, -1, -1):
            if s[i] == "1":
                ans += dp[i]
                if i < length - 1 and s[i + 1] == "1":
                    return ans
        ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (5, 5),
    (100000000, 514229)
])
def test_solutions(args, expected):
    assert Solution().findIntegers(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
