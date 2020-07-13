#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 16:24:32
# @Last Modified : 2020-07-13 16:24:32
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一个算法，算出 n 阶乘有多少个尾随零。 
# 
#  示例 1: 
# 
#  输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。 
# 
#  示例 2: 
# 
#  输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零. 
# 
#  说明: 你算法的时间复杂度应为 O(log n) 。 
#  Related Topics 数学 
#  👍 17 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (3, 0),
    (5, 1),
    (120, 28),
    (1808548329, 452137076),
])
def test_solutions(args, expected):
    assert Solution().trailingZeroes(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
