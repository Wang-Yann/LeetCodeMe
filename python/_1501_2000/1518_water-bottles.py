#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-08 16:37:47
# @Last Modified : 2020-08-08 16:37:47
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。 
# 
#  如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。 
# 
#  请你计算 最多 能喝到多少瓶酒。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：numBottles = 9, numExchange = 3
# 输出：13
# 解释：你可以用 3 个空酒瓶兑换 1 瓶酒。
# 所以最多能喝到 9 + 3 + 1 = 13 瓶酒。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：numBottles = 15, numExchange = 4
# 输出：19
# 解释：你可以用 4 个空酒瓶兑换 1 瓶酒。
# 所以最多能喝到 15 + 3 + 1 = 19 瓶酒。
#  
# 
#  示例 3： 
# 
#  输入：numBottles = 5, numExchange = 5
# 输出：6
#  
# 
#  示例 4： 
# 
#  输入：numBottles = 2, numExchange = 3
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= numBottles <= 100 
#  2 <= numExchange <= 100 
#  
#  Related Topics 贪心算法 
#  👍 13 👎 0
	 

"""

import pytest, traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode, ListNode
from sample_datas import BIG_CASE


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        cur_bottles = numBottles
        while cur_bottles >= numExchange:
            n, r = divmod(cur_bottles, numExchange)
            cur_bottles = n + r
            ans += n
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(numBottles=9, numExchange=3), 13],

    pytest.param(dict(numBottles=15, numExchange=4), 19),
    pytest.param(dict(numBottles=5, numExchange=5), 6),
    pytest.param(dict(numBottles=2, numExchange=3), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().numWaterBottles(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
