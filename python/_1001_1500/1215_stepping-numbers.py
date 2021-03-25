#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 16:56:47
# @Last Modified : 2020-08-05 16:56:47
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是 1，那么这个数就是一个「步进数」。 
# 
#  例如，321 是一个步进数，而 421 不是。 
# 
#  给你两个整数，low 和 high，请你找出在 [low, high] 范围内的所有步进数，并返回 排序后 的结果。 
# 
#  
# 
#  示例： 
# 
#  输入：low = 0, high = 21
# 输出：[0,1,2,3,4,5,6,7,8,9,10,12,21]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= low <= high <= 2 * 10^9 
#  
#  Related Topics 回溯算法 
#  👍 10 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        """
        AC
        """
        ans = set()

        def dfs(cur, last):
            if cur > high:
                return
            if low <= cur <= high:
                ans.add(cur)
            if last > 0:
                dfs(10 * cur + last - 1, last - 1)
            if last < 9:
                dfs(10 * cur + last + 1, last + 1)

        for i in range(10):
            dfs(i, i)
        return sorted(ans)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(low=0, high=21), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]],
    [dict(low=10, high=15), [10, 12]],
    [dict(low=7, high=121), [7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98, 101, 121]],
])
def test_solutions(kw, expected):
    assert Solution().countSteppingNumbers(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
