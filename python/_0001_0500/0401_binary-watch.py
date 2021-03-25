#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。 
# 
#  每个 LED 代表一个 0 或 1，最低位在右侧。 
# 
#  
# 
#  例如，上面的二进制手表读取 “3:25”。 
# 
#  给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。 
# 
#  案例: 
# 
#  
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "
# 0:32"] 
# 
#  
# 
#  注意事项: 
# 
#  
#  输出的顺序没有要求。 
#  小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。 
#  分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。 
#  
#  Related Topics 位运算 回溯算法

"""
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def readBinaryWatch(self, num: int) -> List[str]:
        def bit_cnt(bits):
            assert bits >= 0
            cnt = 0
            while bits:
                bits &= bits - 1
                cnt += 1
            return cnt

        res = []
        for h in range(12):
            for m in range(60):
                if bit_cnt(h) + bit_cnt(m) == num:
                    res.append("%d:%02d" % (h, m))
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        hours = [2 ** x for x in range(4)]
        mins = [2 ** x for x in range(6)]
        HOURS, MINS = 4, 6
        if num >= 10:
            return []
        for i in range(0, num + 1):
            if i >= HOURS or num - i >= MINS:
                continue
            choose_hours = itertools.combinations(hours, i)
            choose_mins = itertools.combinations(mins, num - i)
            sum_hours = [sum(x) for x in choose_hours] or [0]
            sum_mins = [sum(x) for x in choose_mins] or [0]

            for hour in sum_hours:
                for minute in sum_mins:
                    if hour <= 11 and minute <= 59:
                        res.append("{}:{:02}".format(hour, minute))
        return res


@pytest.mark.parametrize("args,expected", [
    (1, ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]),
    (2, ['0:03', '0:05', '0:06', '0:09', '0:10', '0:12', '0:17', '0:18', '0:20', '0:24', '0:33', '0:34', '0:36', '0:40', '0:48', '10:00',
         '1:01', '1:02', '1:04', '1:08', '1:16', '1:32', '2:01', '2:02', '2:04', '2:08', '2:16', '2:32', '3:00', '4:01', '4:02', '4:04',
         '4:08', '4:16', '4:32', '5:00', '6:00', '8:01', '8:02', '8:04', '8:08', '8:16', '8:32', '9:00']
     ),
    (7, ["3:31", "3:47", "3:55", "3:59", "5:31", "5:47", "5:55", "5:59", "6:31", "6:47", "6:55", "6:59", "7:15", "7:23", "7:27", "7:29",
         "7:30", "7:39", "7:43", "7:45", "7:46", "7:51", "7:53", "7:54", "7:57", "7:58", "9:31", "9:47", "9:55", "9:59", "10:31", "10:47",
         "10:55", "10:59", "11:15", "11:23", "11:27", "11:29", "11:30", "11:39", "11:43", "11:45", "11:46", "11:51", "11:53", "11:54",
         "11:57", "11:58"])
])
def test_solutions(args, expected):
    res = Solution().readBinaryWatch(args)
    res1 = Solution().readBinaryWatch(args)
    assert sorted(res) == sorted(expected)
    assert sorted(res1) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
