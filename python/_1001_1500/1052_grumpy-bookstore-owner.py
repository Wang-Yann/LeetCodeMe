#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分
# 钟结束后离开。 
# 
#  在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一
# 分钟的顾客就会不满意，不生气则他们是满意的。 
# 
#  书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。 
# 
#  请你返回这一天营业下来，最多有多少客户能够感到满意的数量。 
#  
# 
#  示例： 
# 
#  输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# 输出：16
# 解释：
# 书店老板在最后 3 分钟保持冷静。
# 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= X <= customers.length == grumpy.length <= 20000 
#  0 <= customers[i] <= 1000 
#  0 <= grumpy[i] <= 1 
#  
#  Related Topics 数组 Sliding Window

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = 0
        extra = 0
        max_extra = 0
        N = len(customers)
        for r in range(N):
            if grumpy[r] == 0:
                # // 记录未开技能时，客户的满意量
                res += customers[r]
            else:
                # // 记录区间内可补偿的最大值(老板生气时候的值)
                extra += customers[r]
            if r >= X:
                if grumpy[r - X]:
                    extra -= customers[r - X]
            max_extra = max(max_extra, extra)

        return res + max_extra


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], X=3), 16],
    [dict(customers=[9,10,4,5] , grumpy=[1,0,1,1],X= 1), 19],
])
def test_solutions(kw, expected):
    assert Solution().maxSatisfied(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
