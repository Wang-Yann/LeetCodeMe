#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你 n 笔订单，每笔订单都需要快递服务。 
# 
#  请你统计所有有效的 收件/配送 序列的数目，确保第 i 个物品的配送服务 delivery(i) 总是在其收件服务 pickup(i) 之后。 
# 
#  由于答案可能很大，请返回答案对 10^9 + 7 取余的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 1
# 输出：1
# 解释：只有一种序列 (P1, D1)，物品 1 的配送服务（D1）在物品 1 的收件服务（P1）后。
#  
# 
#  示例 2： 
# 
#  输入：n = 2
# 输出：6
# 解释：所有可能的序列包括：
# (P1,P2,D1,D2)，(P1,P2,D2,D1)，(P1,D1,P2,D2)，(P2,P1,D1,D2)，(P2,P1,D2,D1) 和 (P2,D2
# ,P1,D1)。
# (P1,D2,P2,D1) 是一个无效的序列，因为物品 2 的收件服务（P2）不应在物品 2 的配送服务（D2）之后。
#  
# 
#  示例 3： 
# 
#  输入：n = 3
# 输出：90
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 500 
#  
#  Related Topics 数学 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countOrders(self, n: int) -> int:
        """
        f[i]=(2i−1)*i∗f[i−1]
        于 f[i] 包含了 i 份订单，我们可以将其拆分为前 i - 1 份订单（编号为 1, 2, ..., i - 1）与 1 份额外的订单（编号为 i）。
        对于一个包含前 i - 1 份订单的固定序列，它的长度为 (i - 1) * 2，我们只需要在这个序列中加上第 i 份订单，就可以得到一条订单数量为 i 的序列

        """
        MOD = 10 ** 9 + 7
        res = 1
        for i in range(2, n + 1):
            res = res * (2*i - 1) * i % MOD
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (1, 1),
    (2, 6),
    (3, 90)
])
def test_solutions(args, expected):
    assert Solution().countOrders(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
