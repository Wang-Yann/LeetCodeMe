#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 00:01:23
# @Last Modified : 2020-07-06 00:01:23
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 桌面上有 2n 个颜色不完全相同的球，球上的颜色共有 k 种。给你一个大小为 k 的整数数组 balls ，其中 balls[i] 是颜色为 i 的球的数量
# 。 
# 
#  所有的球都已经 随机打乱顺序 ，前 n 个球放入第一个盒子，后 n 个球放入另一个盒子（请认真阅读示例 2 的解释部分）。 
# 
#  注意：这两个盒子是不同的。例如，两个球颜色分别为 a 和 b，盒子分别为 [] 和 ()，那么 [a] (b) 和 [b] (a) 这两种分配方式是不同的
# （请认真阅读示例 1 的解释部分）。 
# 
#  请计算「两个盒子中球的颜色数相同」的情况的概率。 
# 
#  
# 
#  示例 1： 
# 
#  输入：balls = [1,1]
# 输出：1.00000
# 解释：球平均分配的方式只有两种：
# - 颜色为 1 的球放入第一个盒子，颜色为 2 的球放入第二个盒子
# - 颜色为 2 的球放入第一个盒子，颜色为 1 的球放入第二个盒子
# 这两种分配，两个盒子中球的颜色数都相同。所以概率为 2/2 = 1 。
#  
# 
#  示例 2： 
# 
#  输入：balls = [2,1,1]
# 输出：0.66667
# 解释：球的列表为 [1, 1, 2, 3]
# 随机打乱，得到 12 种等概率的不同打乱方案，每种方案概率为 1/12 ：
# [1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], 
# [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
# 然后，我们将前两个球放入第一个盒子，后两个球放入第二个盒子。
# 这 12 种可能的随机打乱方式中的 8 种满足「两个盒子中球的颜色数相同」。
# 概率 = 8/12 = 0.66667
#  
# 
#  示例 3： 
# 
#  输入：balls = [1,2,1,2]
# 输出：0.60000
# 解释：球的列表为 [1, 2, 2, 3, 4, 4]。要想显示所有 180 种随机打乱方案是很难的，但只检查「两个盒子中球的颜色数相同」的 108 种情况
# 是比较容易的。
# 概率 = 108 / 180 = 0.6 。
#  
# 
#  示例 4： 
# 
#  输入：balls = [3,2,1]
# 输出：0.30000
# 解释：球的列表为 [1, 1, 1, 2, 2, 3]。要想显示所有 60 种随机打乱方案是很难的，但只检查「两个盒子中球的颜色数相同」的 18 种情况是比
# 较容易的。
# 概率 = 18 / 60 = 0.3 。
#  
# 
#  示例 5： 
# 
#  输入：balls = [6,6,6,6,6,6]
# 输出：0.90327
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= balls.length <= 8 
#  1 <= balls[i] <= 6 
#  sum(balls) 是偶数 
#  答案与真实值误差在 10^-5 以内，则被视为正确答案 
#  
#  Related Topics 数学 回溯算法 
#  👍 20 👎 0

"""
import itertools
import math
from collections import Counter
from typing import List

import pytest
# leetcode submit region begin(Prohibit modification and deletion)
# from scipy.interpolate.interpolate import prod
from sympy import prod


class Solution:
    """
    暴力法
       https://leetcode-cn.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/solution/zhuan-ge-guo-ji-ban-ben-de-bao-li-jie-fa-you-mei-d/
       """

    def multinomial(self, n):
        return math.factorial(sum(n)) / prod([math.factorial(i) for i in n])

    def getProbability(self, balls):
        # print(self.multinomial([1, 2, 3]))
        k, n, Q = len(balls), sum(balls) // 2, 0
        arrays = [range(0, i + 1) for i in balls]
        t = list(itertools.product(*arrays))
        for i in range(len(t)):
            if sum(t[i]) == n and t[i].count(0) == t[-i - 1].count(0):
                Q += self.multinomial(t[i]) * self.multinomial(t[-i - 1])

        return Q / self.multinomial(list(balls))


# leetcode submit region end(Prohibit modification and deletion)

class Solution2:
    """Hard No should in Interview"""

    def getProbability(self, balls: List[int]) -> float:
        from scipy.special import comb  # help to calculate combination numbers

        sm = sum(balls)
        number_of_combinations = comb(sm, sm // 2)  #

        def number_of_ways_to_pick(n):
            # there are n balls of color-a, we want to pick some number of them and put them into boxA, and others into boxB
            d = Counter()
            # key: number of balls put into boxA, value: number of such combinations
            for i in range(n + 1):
                d[i] = comb(n, i)
            return d

        status = Counter()
        status[(0, 0)] = 1
        # key: number difference, color difference; value: number of such combinations
        for n in balls:
            combs = number_of_ways_to_pick(n)
            new_s = Counter()
            for k in status:
                d_n, d_c = k
                for n_a in combs:
                    if n_a == 0:
                        new_s[(d_n - n, d_c - 1)] += status[k] * combs[n_a]
                    elif n_a == n:
                        new_s[(d_n + n, d_c + 1)] += status[k] * combs[n_a]
                    else:
                        new_s[(d_n + 2 * n_a - n, d_c)] += status[k] * combs[n_a]
            status = new_s

        return status[(0, 0)] / number_of_combinations


@pytest.mark.parametrize("kwargs,expected", [
    (dict(balls=[1, 1]), 1.0),
    (dict(balls=[2, 1, 1]), 0.66667),
    (dict(balls=[1, 2, 1, 2]), 0.60),
    (dict(balls=[3, 2, 1]), 0.30),
    pytest.param(dict(balls=[6, 6, 6, 6, 6, 6]), 0.90327),
    pytest.param(dict(balls=[6, 6, 6, 6, 6, 6, 6, 6]), 0.85571),
])
def test_solutions(kwargs, expected):
    assert Solution().getProbability(**kwargs) == pytest.approx(expected, 1e-5)
    assert Solution2().getProbability(**kwargs) == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
