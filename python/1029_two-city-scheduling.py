#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。 
# 
#  返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。 
# 
#  
# 
#  示例： 
# 
#  输入：[[10,20],[30,200],[400,50],[30,20]]
# 输出：110
# 解释：
# 第一个人去 A 市，费用为 10。
# 第二个人去 A 市，费用为 30。
# 第三个人去 B 市，费用为 50。
# 第四个人去 B 市，费用为 20。
# 
# 最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= costs.length <= 100 
#  costs.length 为偶数 
#  1 <= costs[i][0], costs[i][1] <= 1000 
#  
#  Related Topics 贪心算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """不简单
        公司首先将这 2N 个人全都安排飞往 B 市，再选出 N 个人改变它们的行程，让他们飞往 A 市。
        如果选择改变一个人的行程，那么公司将会额外付出 price_A - price_B 的费用，这个费用可正可负
         最优的方案是，选出 price_A - price_B 最小的 NN 个人，让他们飞往 A 市，其余人飞往 B 市
        """
        N = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])
        total = 0
        for i in range(N):
            total += costs[i][0] + costs[i + N][1]
        return total


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[10, 20], [30, 200], [400, 50], [30, 20]], 110)
])
def test_solutions(args, expected):
    assert Solution().twoCitySchedCost(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
