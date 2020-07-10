#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 15:02:18
# @Last Modified : 2020-07-10 15:02:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。 
# 
#  商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] 
# <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。 
# 
#  请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。 
# 
#  
# 
#  示例 1： 
# 
#  输入：prices = [8,4,6,2,3]
# 输出：[4,2,4,2,3]
# 解释：
# 商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
# 商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
# 商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
# 商品 3 和 4 都没有折扣。
#  
# 
#  示例 2： 
# 
#  输入：prices = [1,2,3,4,5]
# 输出：[1,2,3,4,5]
# 解释：在这个例子中，所有商品都没有折扣。
#  
# 
#  示例 3： 
# 
#  输入：prices = [10,1,1,6]
# 输出：[9,0,1,6]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 500 
#  1 <= prices[i] <= 10^3 
#  
#  Related Topics 数组 
#  👍 10 👎 0

"""
import copy
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        多思考下
       单调栈　忘记了
       递增
        """
        stk = []
        for i, p in enumerate(prices):
            # print(stk,list(map(prices.__getitem__,stk)))
            while stk and prices[stk[-1]] >= p:
                prices[stk.pop()] -= p
            stk.append(i)
        # print(stk)
        return prices


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        AC
        Success: Runtime:40 ms, faster than 94.47% of Python3 online submissions. Memory Usage:13.7 MB, less than 100.00% of Python3 online submissions.
        """
        N = len(prices)
        ans = []
        for i, price in enumerate(prices):
            delta = 0
            for j in range(i + 1, N):
                if prices[j] <= price:
                    delta = prices[j]
                    break
            ans.append(price - delta)
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(prices=[8, 4, 6, 2, 3]), [4, 2, 4, 2, 3]],
    [dict(prices=[1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]],
    [dict(prices=[10, 1, 1, 6]), [9, 0, 1, 6]],
])
def test_solutions(kw, expected):
    kw1 = copy.deepcopy(kw)
    assert Solution().finalPrices(**kw) == expected
    assert Solution1().finalPrices(**kw1) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
