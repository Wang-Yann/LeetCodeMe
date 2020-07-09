#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-09 23:50:20
# @Last Modified : 2020-07-09 23:50:20
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于 n 的 最简 分数 。分数可以以 任意 顺序返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：["1/2"]
# 解释："1/2" 是唯一一个分母小于等于 2 的最简分数。 
# 
#  示例 2： 
# 
#  输入：n = 3
# 输出：["1/2","1/3","2/3"]
#  
# 
#  示例 3： 
# 
#  输入：n = 4
# 输出：["1/2","1/3","1/4","2/3","3/4"]
# 解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。 
# 
#  示例 4： 
# 
#  输入：n = 1
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 100 
#  
#  Related Topics 数学 
#  👍 3 👎 0


"""

import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    AC
    解答成功: 执行耗时:108 ms,击败了86.12% 的Python3用户 内存消耗:14.1 MB,击败了100.00% 的Python3用户
    """

    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for divisor in range(2, n + 1):
            for numerator in range(1, divisor):
                if math.gcd(divisor, numerator) == 1:
                    ans.append("%d/%d" % (numerator, divisor))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=2), ["1/2"]],
    [dict(n=3), ["1/2", "1/3", "2/3"]],
    [dict(n=4), ["1/2", "1/3", "1/4", "2/3", "3/4"]],
    pytest.param(dict(n=1), []),
])
def test_solutions(kwargs, expected):
    assert sorted(Solution().simplifiedFractions(**kwargs)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
