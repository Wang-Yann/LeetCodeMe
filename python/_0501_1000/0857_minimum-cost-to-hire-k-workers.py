#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有 N 名工人。 第 i 名工人的工作质量为 quality[i] ，其最低期望工资为 wage[i] 。 
# 
#  现在我们想雇佣 K 名工人组成一个工资组。在雇佣 一组 K 名工人时，我们必须按照下述规则向他们支付工资： 
# 
#  
#  对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。 
#  工资组中的每名工人至少应当得到他们的最低期望工资。 
#  
# 
#  返回组成一个满足上述条件的工资组至少需要多少钱。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入： quality = [10,20,5], wage = [70,50,30], K = 2
# 输出： 105.00000
# 解释： 我们向 0 号工人支付 70，向 2 号工人支付 35。 
# 
#  示例 2： 
# 
#  输入： quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# 输出： 30.66667
# 解释： 我们向 0 号工人支付 4，向 2 号和 3 号分别支付 13.33333。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= K <= N <= 10000，其中 N = quality.length = wage.length 
#  1 <= quality[i] <= 10000 
#  1 <= wage[i] <= 10000 
#  与正确答案误差在 10^-5 之内的答案将被视为正确的。 
#  
#  Related Topics 堆

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
import fractions

class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        """
        GOOD
        我们可以定义一个“价值”，表示工人最低期望工资与工作质量之比。例如某位工人的最低期望工资为 100，工作质量为 20，那么他的价值为 100 / 20 = 5.0
        我们需要在前 i 名工人中选择 K 个工作质量最低的。我们可以使用一个大根堆来实时维护 K 个最小值
        """
        workers = sorted((fractions.Fraction(w, q), q, w) for q, w in zip(quality, wage))
        ans = float("inf")
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q
            if len(pool) > K:
                sumq += heapq.heappop(pool)
            if len(pool) == K:
                ans = min(ans, ratio * sumq)
        return float(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        quality=[10, 20, 5], wage=[70, 50, 30], K=2
    ), 105.0),
    pytest.param(dict(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], K=3), 30.66667),
])
def test_solutions(kwargs, expected):
    assert Solution().mincostToHireWorkers(**kwargs) == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
