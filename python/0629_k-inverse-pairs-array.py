#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。 
# 
#  逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。 
# 
#  由于答案可能很大，只需要返回 答案 mod 109 + 7 的值。 
# 
#  示例 1: 
# 
#  
# 输入: n = 3, k = 0
# 输出: 1
# 解释: 
# 只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
#  
# 
#  示例 2: 
# 
#  
# 输入: n = 3, k = 1
# 输出: 2
# 解释: 
# 数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
#  
# 
#  说明: 
# 
#  
#  n 的范围是 [1, 1000] 并且 k 的范围是 [0, 1000]。 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        我们用 f(i, j) 表示数字 [1 .. i] 的排列中恰好包含 j 个逆序对的个数。在状态转移时，我们考虑数 i 放置的位置与逆序对个数的关系。
        我们在数字 [1 .. i - 1] 组成的排列中放入 i 时，有 i 种放置方法：如果将 i 放在最后，则逆序对数量不变；
        如果将 i 放在倒数第二个，则逆序对数量增加 1；如果将 i 放在第一个，则逆序对数量增加 i - 1。
        这是因为 i 是 [1 .. i] 中的最大值，因此将它放置在 [1 .. i - 1] 的排列中的任意一个位置，
        它都会与在它之后的那些数形成逆序对。如果它后面有 k 个数，则会形成 k 个逆序对

        f(i, j) = f(i - 1, j) + f(i - 1, j - 1) + ... + f(i - 1, j - i + 1)
        优化为以下:
        ==> f(i, j) = f(i, j - 1) + f(i - 1, j) - f(i - 1, j - i)
        https://leetcode-cn.com/problems/k-inverse-pairs-array/solution/kge-ni-xu-dui-shu-zu-by-leetcode/
        """
        MOD = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(min(k, i * (i - 1) // 2) + 1):
                if i == 1 and j == 0:
                    dp[i][j] = 1
                    break
                elif j == 0:
                    dp[i][j] = 1
                else:
                    if j - i >= 0:
                        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] + MOD - dp[i - 1][j - i]) % MOD
                    else:
                        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD
        return dp[n][k]


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("kw,expected", [
    [dict(n=3, k=0), 1],
    [dict(n=3, k=1), 2],
])
def test_solutions(kw, expected):
    assert Solution().kInversePairs(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
