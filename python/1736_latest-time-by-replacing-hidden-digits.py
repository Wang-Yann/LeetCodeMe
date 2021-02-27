#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 12:17:05
# @Last Modified : 2021-02-27 12:17:05
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。 
# 
#  有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。 
# 
#  替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：time = "2?:?0"
# 输出："23:50"
# 解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。
#  
# 
#  示例 2： 
# 
#  
# 输入：time = "0?:3?"
# 输出："09:39"
#  
# 
#  示例 3： 
# 
#  
# 输入：time = "1?:22"
# 输出："19:22"
#  
# 
#  
# 
#  提示： 
# 
#  
#  time 的格式为 hh:mm 
#  题目数据保证你可以由输入的字符串生成有效的时间 
#  
#  Related Topics 贪心算法 字符串 
#  👍 9 👎 0
  

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maximumTime(self, time: str) -> str:
        ans = ""
        hours = time[0:2]
        if hours in ("??", "2?",):
            ans += "23"
        elif hours in ("1?", "0?"):
            ans += hours[0] + "9"
        elif hours[0] == "?":
            if "4" <= hours[1] <= "9":
                ans += "1" + hours[1]
            else:
                ans += "2" + hours[1]
        else:
            ans += hours
        ans += ":"
        ans += time[3] if time[3] != "?" else "5"
        ans += time[4] if time[4] != "?" else "9"
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def maximumTime(self, time: str) -> str:
        for h in range(24)[::-1]:
            for m in range(60)[::-1]:
                s = f'{h:02d}:{m:02d}'
                if all(a == b or b == '?' for a, b in zip(s, time)):
                    return s


@pytest.mark.parametrize("kw,expected", [
    [dict(time="2?:?0"), "23:50"],
    [dict(time="0?:3?"), "09:39"],
    [dict(time="1?:22"), "19:22"],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().maximumTime(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
