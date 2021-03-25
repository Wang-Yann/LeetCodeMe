#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有 A 和 B 两种类型的汤。一开始每种类型的汤有 N 毫升。有四种分配操作： 
# 
#  
#  提供 100ml 的汤A 和 0ml 的汤B。 
#  提供 75ml 的汤A 和 25ml 的汤B。 
#  提供 50ml 的汤A 和 50ml 的汤B。 
#  提供 25ml 的汤A 和 75ml 的汤B。 
#  
# 
#  当我们把汤分配给某人之后，汤就没有了。每个回合，我们将从四种概率同为0.25的操作中进行分配选择。如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两
# 种类型的汤都分配完时，停止操作。 
# 
#  注意不存在先分配100 ml汤B的操作。 
# 
#  需要返回的值： 汤A先分配完的概率 + 汤A和汤B同时分配完的概率 / 2。 
# 
#  
# 示例:
# 输入: N = 50
# 输出: 0.625
# 解释:
# 如果我们选择前两个操作，A将首先变为空。对于第三个操作，A和B会同时变为空。对于第四个操作，B将首先变为空。
# 所以A变为空的总概率加上A和B同时变为空的概率的一半是 0.25 *(1 + 1 + 0.5 + 0)= 0.625。
#  
# 
#  注释: 
# 
#  
#  0 <= N <= 10^9。 
#  
#  返回值在 10^-6 的范围将被认为是正确的。 
#  
#  
#  Related Topics 动态规划

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def soupServings(self, CNT: int) -> float:
        """
        由于四种分配操作都是 25 的倍数，因此我们可以将 N 除以 25（如果有余数，则补 1），并将分配操作变为 (4, 0)，(3, 1)，(2, 2) 和 (1, 3)。
        当 N 较小时，我们可以用动态规划来解决这个问题。设 dp(i, j) 表示汤 A 和汤 B 分别剩下 i 和 j 份时，所求的概率值。状态转移方程为：

        dp(i, j) = 1/4 * (dp(i - 4, y) + dp(i - 3, y - 1) + dp(i - 2, y - 2) + dp(i - 1, y - 3))
        边界条件为：

        dp(i, j) = 0.5   if i <= 0 and j <= 0
        dp(i, j) = 1.0   if i <= 0 and j > 0
        dp(i, j) = 0.0   if i > 0 and j <= 0
        即如果同时分配完（边界条件中的第一行），概率值为 1.0 的一半即为 0.5；如果汤 A 先分配完，概率值为 1.0；如果汤 B 先分配完，概率值为 0.0

        那么在一次分配中，汤 A 平均会少 (4 + 3 + 2 + 1) / 4 = 2.5 份，汤 B 平均会少 (0 + 1 + 2 + 3) / 4 = 1.5 份。
        因此在 N 非常大的时候，A 会有很大的概率比 B 先分配完，所有概率应该非常接近 1。事实上，当 N >= 500 * 25 时，
        所求概率已经大于 0.999999 了（可以通过上面的动态规划方法求出
        """
        CNT = (CNT + 24) // 25
        if CNT >= 500:
            return 1.0

        @functools.lru_cache(None)
        def dp(x, y):
            if x <= 0 and y <= 0:
                return 0.5
            elif x <= 0 and y > 0:
                return 1.0
            elif x > 0 and y <= 0:
                return 0.0
            else:
                return 0.25 * (dp(x - 4, y) + dp(x - 3, y - 1) + dp(x - 2, y - 2) + dp(x - 1, y - 3))

        return dp(CNT, CNT)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (50, 0.625)
])
def test_solutions(args, expected):
    assert Solution().soupServings(args) == pytest.approx(expected, 1e-4)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
