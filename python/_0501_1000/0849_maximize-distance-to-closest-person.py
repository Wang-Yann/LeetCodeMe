#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。 
# 
#  至少有一个空座位，且至少有一人坐在座位上。 
# 
#  亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。 
# 
#  返回他到离他最近的人的最大距离。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,0,0,0,1,0,1]
# 输出：2
# 解释：
# 如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
# 如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
# 因此，他到离他最近的人的最大距离是 2 。 
#  
# 
#  示例 2： 
# 
#  输入：[1,0,0,0]
# 输出：3
# 解释：
# 如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
# 这是可能的最大距离，所以答案是 3 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= seats.length <= 20000 
#  seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        利用前缀，中缀，后缀。 计算前缀中连续零的数量，res = max（res，zeros） 计算中间连续零的数量，
        res = max（res，（zeros + 1）/ 2） 计算后缀中连续零的数量，res = max（res，zeros）
        """
        res = i = 0
        for j in range(len(seats)):
            if seats[j]:
                res = max(res, (j - i + 1) >> 1) if i else j
                i = j + 1
        return max(res, len(seats) - i)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def maxDistToClosest(self, seats: List[int]) -> int:
        occupied = [i for i, v in enumerate(seats) if v == 1]
        length = len(seats)
        ans = max(occupied[0], 0)
        for i in range(1, len(occupied)):
            interval = occupied[i] - occupied[i - 1]
            if interval % 2:
                interval -= 1
            cur = interval >>1
            ans = max(ans, cur)
        ans = max(ans, length - 1 - occupied[-1])
        return ans


@pytest.mark.parametrize("args,expected", [
    ([1, 0, 0, 0], 3),
    ([0, 1], 1),
    ([1, 0, 0, 1], 1),
    ([1, 0, 0, 0, 1, 0, 1], 2)
])
def test_solutions(args, expected):
    assert Solution().maxDistToClosest(args) == expected
    assert Solution1().maxDistToClosest(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
