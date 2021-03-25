#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 23:27:22
# @Last Modified : 2020-07-23 23:27:22
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 力扣想让一个最优秀的员工在 N 个城市间旅行来收集算法问题。 但只工作不玩耍，聪明的孩子也会变傻，所以您可以在某些特定的城市和星期休假。您的工作就是安排旅行
# 使得最大化你可以休假的天数，但是您需要遵守一些规则和限制。 
# 
#  规则和限制： 
# 
#  
#  您只能在 N 个城市之间旅行，用 0 到 N-1 的索引表示。一开始，您在索引为0的城市，并且那天是星期一。 
#  这些城市通过航班相连。这些航班用 N*N 矩阵 flights（不一定是对称的）表示，flights[i][j] 代表城市i到城市j的航空状态。如果没有城
# 市i到城市j的航班，flights[i][j] = 0；否则，flights[i][j] = 1。同时，对于所有的i，flights[i][i] = 0。 
#  您总共有 K 周（每周7天）的时间旅行。您每天最多只能乘坐一次航班，并且只能在每周的星期一上午乘坐航班。由于飞行时间很短，我们不考虑飞行时间的影响。 
#  对于每个城市，不同的星期您休假天数是不同的，给定一个 N*K 矩阵 days 代表这种限制，days[i][j] 代表您在第j个星期在城市i能休假的最长天
# 数。 
#  
# 
#  给定 flights 矩阵和 days 矩阵，您需要输出 K 周内可以休假的最长天数。 
# 
#  示例 1: 
# 
#  输入:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
# 输出: 12
# 解释: 
# Ans = 6 + 3 + 3 = 12. 
# 
# 最好的策略之一：
# 第一个星期 : 星期一从城市0飞到城市1，玩6天，工作1天。 
# （虽然你是从城市0开始，但因为是星期一，我们也可以飞到其他城市。） 
# 第二个星期 : 星期一从城市1飞到城市2，玩3天，工作4天。
# 第三个星期 : 呆在城市2，玩3天，工作4天。
#  
# 
#  
# 
#  示例 2: 
# 
#  输入:flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
# 输出: 3
# 解释: 
# Ans = 1 + 1 + 1 = 3. 
# 
# 由于没有航班可以让您飞到其他城市，你必须在城市0呆整整3个星期。 
# 对于每一个星期，你只有一天时间玩，剩下六天都要工作。 
# 所以最大休假天数为3.
#  
# 
#  
# 
#  示例 3: 
# 
#  输入:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]
# 输出: 21
# 解释:
# Ans = 7 + 7 + 7 = 21
# 
# 最好的策略之一是：
# 第一个星期 : 呆在城市0，玩7天。 
# 第二个星期 : 星期一从城市0飞到城市1，玩7天。
# 第三个星期 : 星期一从城市1飞到城市2，玩7天。
#  
# 
#  
# 
#  注意: 
# 
#  
#  N 和 K 都是正整数，在 [1, 100] 范围内。 
#  矩阵 flights 的所有值都是 [0, 1] 范围内的整数。 
#  矩阵 days 的所有值都是 [0, 7] 范围内的整数。 
#  超过休假天数您仍可以呆在那个城市，但是在额外的日子您需要 工作 ，这些日子不会算做休假日。 
#  如果您从城市A飞往城市B并在当天休假日，这个休假会被算作是城市B的休假日。 
#  我们不考虑飞行时间对计算休假日的影响。 
#  
# 
#  
#  Related Topics 动态规划 
#  👍 14 👎 0

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        """
        第 weekno  周在  cur_city 城市时，所能最大化的休假天数
        每次方法调用，遍历所有的城市（用 i 来表示）找到跟当前城市相连的城市。这时候有两个选择，
        留在当前城市或者飞到相连的城市，用 j 来表示下周所在的城市。随后，周数加 1 并进行下一次递归，根据递归结果计算休假天数。
        休假天数根据下面公式来计算： days[j][weekno] + dfs(j, weekno + 1)。
        最后，将休假天数与全局最大休假天数相比较，将全局最大休假天数更新为两者中的最大值


        """
        K = len(days[0])
        N = len(flights)

        @functools.lru_cache(None)
        def dp(cur_city, weekno):
            if weekno == K:
                return 0
            max_val = 0
            for i in range(N):
                if flights[cur_city][i] == 1 or i == cur_city:
                    val = days[i][weekno] + dp(i, weekno + 1)
                    max_val = max(max_val, val)
            return max_val

        return dp(0, 0)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(flights=[[0, 1, 1], [1, 0, 1], [1, 1, 0]], days=[[1, 3, 1], [6, 0, 3], [3, 3, 3]]), 12],

    pytest.param(dict(flights=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], days=[[1, 1, 1], [7, 7, 7], [7, 7, 7]]), 3),
    pytest.param(dict(flights=[[0, 1, 1], [1, 0, 1], [1, 1, 0]], days=[[7, 0, 0], [0, 7, 0], [0, 0, 7]]), 21),
])
def test_solutions(kwargs, expected):
    assert Solution().maxVacationDays(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
