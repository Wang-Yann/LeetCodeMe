#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 17:10:58
# @Last Modified : 2020-07-30 17:10:58
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在组合数学中，如果一个排列中所有元素都不在原先的位置上，那么这个排列就被称为错位排列。 
# 
#  给定一个从 1 到 n 升序排列的数组，你可以计算出总共有多少个不同的错位排列吗？ 
# 
#  由于答案可能非常大，你只需要将答案对 109+7 取余输出即可。 
# 
#  
# 
#  样例 1: 
# 
#  输入: 3
# 输出: 2
# 解释: 原始的数组为 [1,2,3]。两个错位排列的数组为 [2,3,1] 和 [3,1,2]。
#  
# 
#  
# 
#  注释: 
# n 的范围是 [1, 106]。 
#  Related Topics 数学 
#  👍 14 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDerangement(self, n: int) -> int:
        """
        对于数组 [1, 2, ..., n]，我们首先考虑将 1 放置在哪个位置。根据题目的规定，1 不能放在数组的第一个位置，
        因此它有 n - 1 个位置可以放置，不妨设我们将 1 放置在了位置 x（位置从 1 开始计数，即 2 <= x <= n）。
        我们继续考虑数 x 应该放置在哪个位置，此时会有两种情况：

        我们将 x 放置在位置 1，这样我们就解决了数组 [1, 2, ..., n] 中的两个数 1 和 x，剩下的 n - 2 个数继续进行错位排列；
        我们将 x 放置在除了位置 1 的某个位置 y，可以发现，此时我们将 [2, ..., n] 这 n - 1 个数放置到位置 [1, 2, ..., n] \ x，
            其中 \ 表示从集合中去除一个元素。对于 [2, ..., n] \ x 中的数，它们不能被放置到对应的位置 [2, ..., n] \ x，
            而对于数 x，它不能被放置到位置 1，因此可以等同于对除了 1 之外的剩下 n - 1 个数继续进行错位排列。

        f(n) = (n - 1) * (f(n - 1) + f(n - 2))
        """
        if n < 2:
            return 0
        dp = [0] * (n + 1)
        dp[2] = 1
        MOD = 10 ** 9 + 7
        for i in range(3, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
            dp[i] %= MOD
        return dp[n]

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (3, 2),
    (4, 9),
    (106, 34365947)
])
def test_solutions(args, expected):
    assert Solution().findDerangement(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
