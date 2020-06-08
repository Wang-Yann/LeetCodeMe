#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。 
# 
#  示例 1: 
# 
#  输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#  
# 
#  
# 
#  注意: 
# 
#  
#  1 <= k <= n <= 30,000。 
#  所给数据范围 [-10,000，10,000]。 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        res = total = sum(nums[:k])
        for i in range(k, length):
            total += nums[i] - nums[i - k]
            res = max(res, total)
        return res / k

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 12, -5, -6, 50, 3], k=4), 12.75],
    [dict(nums=[5], k=1), 5.0],
])
def test_solutions(kw, expected):
    res = Solution().findMaxAverage(**kw)
    assert res == pytest.approx(expected, 1e-4)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
