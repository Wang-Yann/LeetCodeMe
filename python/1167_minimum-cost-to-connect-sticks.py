#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 13:40:20
# @Last Modified : 2020-08-05 13:40:20
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 为了装修新房，你需要加工一些长度为正整数的棒材 sticks。 
# 
#  如果要将长度分别为 X 和 Y 的两根棒材连接在一起，你需要支付 X + Y 的费用。 由于施工需要，你必须将所有棒材连接成一根。 
# 
#  返回你把所有棒材 sticks 连成一根所需要的最低费用。注意你可以任意选择棒材连接的顺序。 
# 
#  
# 
#  示例 1： 
# 
#  输入：sticks = [2,4,3]
# 输出：14
# 解释：先将 2 和 3 连接成 5，花费 5；再将 5 和 4 连接成 9；总花费为 14。
#  
# 
#  示例 2： 
# 
#  输入：sticks = [1,8,3,5]
# 输出：30
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= sticks.length <= 10^4 
#  1 <= sticks[i] <= 10^4 
#  
#  Related Topics 贪心算法 
#  👍 16 👎 0

"""
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """AC"""
        # N = len(sticks)
        # if N < 2:
        #     return 0
        heapq.heapify(sticks)
        total = 0
        while len(sticks) >= 2:
            cost1 = heapq.heappop(sticks)
            cost2 = heapq.heappop(sticks)
            cost = cost1 + cost2
            total += cost
            heapq.heappush(sticks, cost)
        return total


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(sticks=[14]), 0],
    [dict(sticks=[2, 4, 3]), 14],
    [dict(sticks=[1, 8, 3, 5]), 30],
    [dict(sticks=[3354, 4316, 3259, 4904, 4598, 474, 3166, 6322, 8080, 9009]), 151646],
])
def test_solutions(kw, expected):
    assert Solution().connectSticks(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
