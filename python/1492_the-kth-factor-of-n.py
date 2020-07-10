#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 18:04:57
# @Last Modified : 2020-07-10 18:04:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个正整数 n 和 k 。 
# 
#  如果正整数 i 满足 n % i == 0 ，那么我们就说正整数 i 是整数 n 的因子。 
# 
#  考虑整数 n 的所有因子，将它们 升序排列 。请你返回第 k 个因子。如果 n 的因子数少于 k ，请你返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 12, k = 3
# 输出：3
# 解释：因子列表包括 [1, 2, 3, 4, 6, 12]，第 3 个因子是 3 。
#  
# 
#  示例 2： 
# 
#  输入：n = 7, k = 2
# 输出：7
# 解释：因子列表包括 [1, 7] ，第 2 个因子是 7 。
#  
# 
#  示例 3： 
# 
#  输入：n = 4, k = 4
# 输出：-1
# 解释：因子列表包括 [1, 2, 4] ，只有 3 个因子，所以我们应该返回 -1 。
#  
# 
#  示例 4： 
# 
#  输入：n = 1, k = 1
# 输出：1
# 解释：因子列表包括 [1] ，第 1 个因子为 1 。
#  
# 
#  示例 5： 
# 
#  输入：n = 1000, k = 3
# 输出：4
# 解释：因子列表包括 [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000] 。
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= n <= 1000 
#  
#  Related Topics 数学 
#  👍 1 👎 0

"""

import math

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """AC"""
        factors = {1, n}
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        sorted_factors = sorted(factors)
        if k <= len(sorted_factors):
            return sorted_factors[k - 1]
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=12, k=3), 3],
    [dict(n=7, k=2), 7],
    [dict(n=4, k=4), -1],
    [dict(n=1, k=1), 1],
    [dict(n=1000, k=3), 4],
])
def test_solutions(kw, expected):
    assert Solution().kthFactor(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
