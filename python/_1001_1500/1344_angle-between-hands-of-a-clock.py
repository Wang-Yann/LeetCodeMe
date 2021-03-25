#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个数 hour 和 minutes 。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：hour = 12, minutes = 30
# 输出：165
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：hour = 3, minutes = 30
# 输出；75
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：hour = 3, minutes = 15
# 输出：7.5
#  
# 
#  示例 4： 
# 
#  输入：hour = 4, minutes = 50
# 输出：155
#  
# 
#  示例 5： 
# 
#  输入：hour = 12, minutes = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hour <= 12 
#  0 <= minutes <= 59 
#  与标准答案误差在 10^-5 以内的结果都被视为正确结果。 
#  
#  Related Topics 数学

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_angle = 360.0 * hour / 12.0 + (minutes / 60.0) * 360.0 / 12.0
        m_angle = (minutes / 60.0) * 360
        delta = abs(m_angle - h_angle)
        if delta > 180:
            return 360 - delta
        else:
            return delta


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(hour=12, minutes=30), 165],
    [dict(hour=3, minutes=30), 75],
    [dict(hour=3, minutes=15), 7.5],
    [dict(hour=4, minutes=50), 155],
    [dict(hour=12, minutes=0), 0],
])
def test_solutions(kw, expected):
    assert Solution().angleClock(**kw) == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
