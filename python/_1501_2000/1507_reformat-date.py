#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-17 00:05:40
# @Last Modified : 2020-07-17 00:05:40
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0


# 给你一个字符串 date ，它的格式为 Day Month Year ，其中： 
# 
#  
#  Day 是集合 {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"} 中的一个元素。 
#  Month 是集合 {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oc
# t", "Nov", "Dec"} 中的一个元素。 
#  Year 的范围在 [1900, 2100] 之间。 
#  
# 
#  请你将字符串转变为 YYYY-MM-DD 的格式，其中： 
# 
#  
#  YYYY 表示 4 位的年份。 
#  MM 表示 2 位的月份。 
#  DD 表示 2 位的天数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：date = "20th Oct 2052"
# 输出："2052-10-20"
#  
# 
#  示例 2： 
# 
#  输入：date = "6th Jun 1933"
# 输出："1933-06-06"
#  
# 
#  示例 3： 
# 
#  输入：date = "26th May 1960"
# 输出："1960-05-26"
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定日期保证是合法的，所以不需要处理异常输入。 
#  
#  Related Topics 字符串 
#  👍 1 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def reformatDate(self, date: str) -> str:
        """AC"""
        MONTH = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        ds, ms, ys = date.split()
        return "%s-%02d-%02s" % (ys, MONTH.index(ms) + 1, ds[:-2].zfill(2))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(date="20th Oct 2052"), "2052-10-20"],
    [dict(date="6th Jun 1933"), "1933-06-06"],
    [dict(date="26th May 1960"), "1960-05-26"],

])
def test_solutions(kwargs, expected):
    assert Solution().reformatDate(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
