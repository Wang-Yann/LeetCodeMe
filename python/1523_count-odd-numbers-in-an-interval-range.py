#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-08 00:09:34
# @Last Modified : 2020-08-08 00:09:34
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：low = 3, high = 7
# 输出：3
# 解释：3 到 7 之间奇数数字为 [3,5,7] 。 
# 
#  示例 2： 
# 
#  输入：low = 8, high = 10
# 输出：1
# 解释：8 到 10 之间奇数数字为 [9] 。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= low <= high <= 10^9 
#  
#  Related Topics 数学 
#  👍 3 👎 0
	 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        if low % 2 == 1:
            low += 1
            ans += 1
        if high % 2 == 1:
            high -= 1
            ans += 1
        ans += (high - low) // 2
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def countOdds(self, low: int, high: int) -> int:
        """
        高位的奇数个数-低位奇数个数

        """

        return (high >> 1) + high % 2 - (low >> 1)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(low=3, high=7), 3],

    pytest.param(dict(low=8, high=10), 1),
    pytest.param(dict(low=8, high=12), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().countOdds(**kwargs) == expected
    assert Solution1().countOdds(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
