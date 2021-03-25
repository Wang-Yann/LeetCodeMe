#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 11:17:30
# @Last Modified : 2021-02-27 11:17:30
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有一个自行车手打算进行一场公路骑行，这条路线总共由 n + 1 个不同海拔的点组成。自行车手从海拔为 0 的点 0 开始骑行。 
# 
#  给你一个长度为 n 的整数数组 gain ，其中 gain[i] 是点 i 和点 i + 1 的 净海拔高度差（0 <= i < n）。请你返回 最高点的
# 海拔 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：gain = [-5,1,5,0,-7]
# 输出：1
# 解释：海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1 。
#  
# 
#  示例 2： 
# 
#  
# 输入：gain = [-4,-3,-2,-1,4,3,2]
# 输出：0
# 解释：海拔高度依次为 [0,-4,-7,-9,-10,-6,-3,-1] 。最高海拔为 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == gain.length 
#  1 <= n <= 100 
#  -100 <= gain[i] <= 100 
#  
#  Related Topics 数组 
#  👍 1 👎 0
  

"""

import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def largestAltitude(self, gain: List[int]) -> int:
        return max([0] + list(itertools.accumulate(gain)))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(gain=[-5, 1, 5, 0, -7]), 1],
    [dict(gain=[-4, -3, -2, -1, 4, 3, 2]), 0],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().largestAltitude(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
