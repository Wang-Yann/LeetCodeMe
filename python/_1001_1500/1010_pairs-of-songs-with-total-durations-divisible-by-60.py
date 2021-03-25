#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。 
# 
#  返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足 i < j 且有 (time[i] + tim
# e[j]) % 60 == 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整数：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60
#  
# 
#  示例 2： 
# 
#  输入：[60,60,60]
# 输出：3
# 解释：所有三对的总持续时间都是 120，可以被 60 整数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= time.length <= 60000 
#  1 <= time[i] <= 500 
#  
#  Related Topics 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0
        count = collections.Counter()
        for t in time:
            result += count[(60 - t) % 60]
            count[t % 60] += 1
        return result


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = collections.Counter()
        for v in time:
            counter[v % 60] += 1
        ans = 0
        # print(counter)
        for k, v in counter.items():
            if 0 < k < 30:
                ans += counter[60 - k] * counter[k]
        # print(ans)
        ans += counter[30] * (counter[30] - 1) // 2
        ans += counter[0] * (counter[0] - 1) // 2
        return ans


@pytest.mark.parametrize("args,expected", [
    ([30, 20, 150, 100, 40], 3),
    pytest.param([60, 60, 60], 3),
    pytest.param(
        [283, 338, 207, 325, 321, 166, 9, 303, 344, 299, 156, 443, 309, 281, 264, 353, 244, 369, 99, 97, 66, 109, 228, 164, 371, 282, 69,
         234, 122, 239, 234, 91, 304, 435, 51, 213, 357, 463, 246, 150, 111, 494, 351, 234, 145, 343, 122, 361, 53, 290, 373, 435, 302, 287,
         279, 290, 122, 154, 70, 72, 225, 209, 65, 370, 25, 253, 175, 262, 336, 250, 78, 201, 293, 374, 325, 426, 236, 106, 123, 430, 393,
         49, 154, 250, 116, 295, 9, 348, 344, 107, 393, 310, 424, 281, 292, 466, 401, 297, 13, 52, 191, 414, 302, 75, 155, 280, 114, 388,
         358, 418, 475, 429, 69, 465, 118, 259, 294, 59, 386, 256, 410, 81, 176, 282, 274, 166, 322, 315, 28, 289, 403, 283, 236, 143, 397,
         45, 420, 59, 367, 154, 19, 308, 55, 484], 176),
])
def test_solutions(args, expected):
    assert Solution().numPairsDivisibleBy60(args) == expected
    assert Solution1().numPairsDivisibleBy60(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
