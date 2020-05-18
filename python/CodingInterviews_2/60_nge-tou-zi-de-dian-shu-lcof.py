#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。 
# 
#  
# 
#  你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 1
# 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
#  
# 
#  示例 2: 
# 
#  输入: 2
# 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0
# .05556,0.02778] 
# 
#  
# 
#  限制： 
# 
#  1 <= n <= 11 
# 

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    """ 优化DP"""

    def twoSum(self, n: int) -> List[float]:
        MAX_VALUE = 6
        dp = [0.0] * (MAX_VALUE * n + 1)
        for i in range(1, MAX_VALUE+1):
            dp[i] = 1 / MAX_VALUE
        for i in range(2, n + 1):
            for j in range(MAX_VALUE * i, i - 1, -1):
                start = max(i - 1, j - MAX_VALUE)
                # print("start",start,i - 1, j - MAX_VALUE)
                dp[j] = sum(dp[start:j]) * 1 / MAX_VALUE
        return dp[n:]


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    """ 原始二维DP
    https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/c-dong-tai-gui-hua-jie-fa-by-yizhe-shi-2/

    """

    def twoSum(self, n: int) -> List[float]:
        dp = []
        for i in range(n + 1):
            dp.append([0.0] * (6 * n + 1))
        for i in range(1, 7):
            dp[1][i] = 1 / 6
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                dp[i][j] = sum(dp[i - 1][max(1, j - 6):j]) * 1 / 6
        res = [round(i, 5) for i in dp[n] if i > 0]
        return res


class Solution2:
    """ From Book"""

    def twoSum(self, n: int) -> List[float]:
        if not n:
            return []
        MAX_VALUE = 6
        probabilities = [[0] * (MAX_VALUE * n + 1) for _ in range(2)]

        flag = 0
        for i in range(1, MAX_VALUE + 1):
            probabilities[flag][i] = 1
        for k in range(2, n + 1):
            for i in range(k):
                probabilities[1 - flag][i] = 0
            for i in range(k, MAX_VALUE * k + 1):
                probabilities[1 - flag][i] = 0
                for j in range(1, min(i, MAX_VALUE) + 1):
                    probabilities[1 - flag][i] += probabilities[flag][i - j]
            flag = 1 - flag
        res = []
        total = MAX_VALUE ** n
        for i in range(n, MAX_VALUE * n + 1):
            res.append(probabilities[flag][i] / total)
        return res


@pytest.mark.parametrize("args,expected", [
    # (1, [0.16667, 0.16667, 0.16667, 0.16667, 0.16667, 0.16667]),
    (2, [0.02778, 0.05556, 0.08333, 0.11111, 0.13889, 0.16667, 0.13889, 0.11111, 0.08333, 0.05556, 0.02778]),
])
def test_solutions(args, expected):
    def check_equal(res, expected):
        assert len(res) == len(expected)
        for v1, v2 in zip(res, expected):
            assert v1 == pytest.approx(v2, abs=1e-5)

    res = Solution().twoSum(args)
    res1 = Solution1().twoSum(args)
    res2 = Solution2().twoSum(args)
    check_equal(res, expected)
    check_equal(res1, expected)
    check_equal(res2, expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
