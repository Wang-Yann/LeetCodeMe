#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请你编写一个程序来计算两个日期之间隔了多少天。 
# 
#  日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。 
# 
#  
# 
#  示例 1： 
# 
#  输入：date1 = "2019-06-29", date2 = "2019-06-30"
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：date1 = "2020-01-15", date2 = "2019-12-31"
# 输出：15
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定的日期是 1971 年到 2100 年之间的有效日期。 
#  
# 

"""
import datetime

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        delta = datetime.datetime.strptime(date1, "%Y-%m-%d") - datetime.datetime.strptime(date2, "%Y-%m-%d")
        return abs(delta.days)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(date1="2019-06-29", date2="2019-06-30"), 1],
    [dict(date1="2020-01-15", date2="2019-12-31"), 15],
])
def test_solutions(kw, expected):
    assert Solution().daysBetweenDates(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
