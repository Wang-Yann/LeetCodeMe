#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 16:59:29
# @Last Modified : 2020-07-13 16:59:29
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定N个人的出生年份和死亡年份，第i个人的出生年份为birth[i]，死亡年份为death[i]，实现一个方法以计算生存人数最多的年份。 
#  你可以假设所有人都出生于1900年至2000年（含1900和2000）之间。如果一个人在某一年的任意时期都处于生存状态，那么他们应该被纳入那一年的统计中。
# 例如，生于1908年、死于1909年的人应当被列入1908年和1909年的计数。 
#  如果有多个年份生存人数相同且均为最大值，输出其中最小的年份。 
#  示例： 
#  输入：
# birth = {1900, 1901, 1950}
# death = {1948, 1951, 2000}
# 输出： 1901
#  
#  提示： 
#  
#  0 < birth.length == death.length <= 10000 
#  birth[i] <= death[i] 
#  
#  Related Topics 数组 
#  👍 12 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        b = collections.Counter(birth)
        d = collections.Counter(death)
        ans, max_count, cur = 0, 0, 0
        for year in sorted({*b.keys(), *d.keys()}):
            cur += b[year]
            if cur > max_count:
                max_count = cur
                ans = year
            cur -= d[year]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(birth=[1900, 1901, 1950], death=[1948, 1951, 2000]), 1901],
])
def test_solutions(kw, expected):
    assert Solution().maxAliveYear(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
