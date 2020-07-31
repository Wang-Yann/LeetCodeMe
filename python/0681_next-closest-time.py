#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 11:07:04
# @Last Modified : 2020-07-31 11:07:04
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个形如 “HH:MM” 表示的时刻，利用当前出现过的数字构造下一个距离当前时间最近的时刻。每个出现数字都可以被无限次使用。 
# 
#  你可以认为给定的字符串一定是合法的。例如，“01:34” 和 “12:09” 是合法的，“1:34” 和 “12:9” 是不合法的。 
# 
#  
# 
#  样例 1: 
# 
#  输入: "19:34"
# 输出: "19:39"
# 解释: 利用数字 1, 9, 3, 4 构造出来的最近时刻是 19:39，是 5 分钟之后。结果不是 19:33 因为这个时刻是 23 小时 59 分钟之后
# 。
#  
# 
#  
# 
#  样例 2: 
# 
#  输入: "23:59"
# 输出: "22:22"
# 解释: 利用数字 2, 3, 5, 9 构造出来的最近时刻是 22:22。 答案一定是第二天的某一时刻，所以选择可构造的最小时刻。
#  
# 
#  
#  Related Topics 字符串 
#  👍 24 👎 0

"""
import datetime

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextClosestTime(self, time: str) -> str:
        dt = datetime.datetime.strptime(time, '%H:%M')
        for i in range(1, 60 * 60 * 24 + 1):
            s_inc = (dt + datetime.timedelta(minutes=i)).strftime("%H:%M")
            if all(char in time for char in s_inc):
                return s_inc


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h, m = time.split(":")
        curr = int(h) * 60 + int(m)
        result = None
        for i in range(curr + 1, curr + 1441):
            t = i % 1440
            h, m = t // 60, t % 60
            result = "%02d:%02d" % (h, m)
            if set(result) <= set(time):
                break
        return result


@pytest.mark.parametrize("args,expected", [
    ("19:34", "19:39"),
    ("23:59", "22:22"),
])
def test_solutions(args, expected):
    assert Solution().nextClosestTime(args) == expected
    assert Solution1().nextClosestTime(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
