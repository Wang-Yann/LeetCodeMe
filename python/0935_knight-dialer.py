#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 国际象棋中的骑士可以按下图所示进行移动： 
# 
#  . 
# 
#  
# 这一次，我们将 “骑士” 放在电话拨号盘的任意数字键（如上图所示）上，接下来，骑士将会跳 N-1 步。每一步必须是从一个数字键跳到另一个数字键。 
# 
#  每当它落在一个键上（包括骑士的初始位置），都会拨出键所对应的数字，总共按下 N 位数字。 
# 
#  你能用这种方式拨出多少个不同的号码？ 
# 
#  因为答案可能很大，所以输出答案模 10^9 + 7。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：1
# 输出：10
#  
# 
#  示例 2： 
# 
#  输入：2
# 输出：20
#  
# 
#  示例 3： 
# 
#  输入：3
# 输出：46
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 5000 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def knightDialer(self, N: int) -> int:
        """
        State Machine
        https://leetcode-cn.com/problems/knight-dialer/solution/4zhuang-tai-dong-tai-gui-hua-pythonjie-kong-jian-f/
        我们可以将数字分为4个状态，命名为A、B、C、D。其中A:{1,3,7,9},B:{2,8},C:{4,6},D:{0}。
        我们用f(X,n)表示：在状态X下，跳跃n步能够得到不同数字的个数。则状态转移方程为：

        f(A,n)=f(B,n-1)+f(C,n-1)
        f(B,n)=2*f(A,n-1)
        f(C,n)=2*f(A,n-1)+f(D,n-1)
        f(D,n)=2*f(C,n-1)

        """
        MOD = 10 ** 9 + 7
        if N == 1:
            return 10
        dp = [1, 1, 1, 1]
        for _ in range(N - 1):
            dp = [dp[1] + dp[2], 2 * dp[0], 2 * dp[0] + dp[3], 2 * dp[2]]
        return (4 * dp[0] + 2 * dp[1] + 2 * dp[2] + dp[3]) % MOD


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def knightDialer(self, N: int) -> int:

        MOD = 10 ** 9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [1] * 10
        for hops in range(N - 1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD


@pytest.mark.parametrize("args,expected", [
    (1, 10),
    (2, 20),
    (3, 46),
])
def test_solutions(args, expected):
    assert Solution().knightDialer(args) == expected
    assert Solution1().knightDialer(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
