#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数 n 。请你先求出从 1 到 n 的每个整数 10 进制表示下的数位和（每一位上的数字相加），然后把数位和相等的数字放到同一个组中。 
# 
#  请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 13
# 输出：4
# 解释：总共有 9 个组，将 1 到 13 按数位求和后这些组分别是：
# [1,10]，[2,11]，[3,12]，[4,13]，[5]，[6]，[7]，[8]，[9]。总共有 4 个组拥有的数字并列最多。
#  
# 
#  示例 2： 
# 
#  输入：n = 2
# 输出：2
# 解释：总共有 2 个大小为 1 的组 [1]，[2]。
#  
# 
#  示例 3： 
# 
#  输入：n = 15
# 输出：6
#  
# 
#  示例 4： 
# 
#  输入：n = 24
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^4 
#  
#  Related Topics 数组

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = collections.Counter([sum(map(int, str(x))) for x in range(1, n + 1)])
        cnts = list(counter.values())
        return cnts.count(max(cnts))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=13), 4],
    [dict(n=2), 2],
    [dict(n=15), 6],
    [dict(n=24), 5],
])
def test_solutions(kw, expected):
    assert Solution().countLargestGroup(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
