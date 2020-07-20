#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-20 23:22:45
# @Last Modified : 2020-07-20 23:22:45
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0


# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1]
#  。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘
# 积是18。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  
# 
#  示例 1： 
# 
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1 
# 
#  示例 2: 
# 
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 1000 
#  
# 
#  注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/ 
#  Related Topics 数学 动态规划 
#  👍 28 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        if n in (2, 3):
            return n - 1
        dp = [0, 1, 2, 3] + [0] * (n - 4 + 1)
        for i in range(4, n + 1):
            max_val = 0
            for j in range(1, i // 2 + 1):
                max_val = max(dp[j] * dp[i - j], max_val)
                dp[i] = max_val
        # print(dp)
        return dp[n] % 1000000007


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (2, 1),
    (10, 36),
])
def test_solutions(args, expected):
    assert Solution().cuttingRope(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
