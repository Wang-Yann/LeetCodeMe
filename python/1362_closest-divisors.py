#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数 num，请你找出同时满足下面全部要求的两个整数： 
# 
#  
#  两数乘积等于 num + 1 或 num + 2 
#  以绝对差进行度量，两数大小最接近 
#  
# 
#  你可以按任意顺序返回这两个整数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：num = 8
# 输出：[3,3]
# 解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3 
# 。
#  
# 
#  示例 2： 
# 
#  输入：num = 123
# 输出：[5,25]
#  
# 
#  示例 3： 
# 
#  输入：num = 999
# 输出：[40,25]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num <= 10^9 
#  
#  Related Topics 数学

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def divisors(n):
            for d in reversed(range(1, int(n ** 0.5) + 1)):
                if n % d == 0:
                    return d, n // d
            return 1, n

        return list(min([divisors(num + 1), divisors(num + 2)], key=lambda x: x[1] - x[0]))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(num=8), [3, 3]],
    [dict(num=123), [5, 25]],
    [dict(num=999), [40, 25]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().closestDivisors(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
