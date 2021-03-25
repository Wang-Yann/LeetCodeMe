#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 16:47:01
# @Last Modified : 2020-07-23 16:47:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一群朋友在度假期间会相互借钱。比如说，小爱同学支付了小新同学的午餐共计 10 美元。如果小明同学支付了小爱同学的出租车钱共计 5 美元。我们可以用一个三元组
#  (x, y, z) 表示一次交易，表示 x 借给 y 共计 z 美元。用 0, 1, 2 表示小爱同学、小新同学和小明同学（0, 1, 2 为人的标号），上述
# 交易可以表示为 [[0, 1, 10], [2, 0, 5]]。 
# 
#  给定一群人之间的交易信息列表，计算能够还清所有债务的最小次数。 
# 
#  注意： 
# 
#  
#  一次交易会以三元组 (x, y, z) 表示，并有 x ≠ y 且 z > 0。 
#  人的标号可能不是按顺序的，例如标号可能为 0, 1, 2 也可能为 0, 2, 6。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：
# [[0,1,10], [2,0,5]]
# 
# 输出：
# 2
# 
# 解释：
# 人 #0 给人 #1 共计 10 美元。
# 人 #2 给人 #0 共计 5 美元。
# 
# 需要两次交易。一种方式是人 #1 分别给人 #0 和人 #2 各 5 美元。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
# 
# 输出：
# 1
# 
# 解释：
# 人 #0 给人 #1 共计 10 美元。Person #0 gave person #1 $10.
# 人 #1 给人 #0 共计 1 美元。Person #1 gave person #0 $1.
# 人 #1 给人 #2 共计 5 美元。Person #1 gave person #2 $5.
# 人 #2 给人 #0 共计 5 美元。Person #2 gave person #0 $5.
# 
# 因此，人 #1 需要给人 #0 共计 4 美元，所有的债务即可还清。
#  
# 
#  
#  👍 29 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        三角债务
        链接：https://leetcode-cn.com/problems/optimal-account-balancing/solution/bao-li-hui-su-by-powcai/

        一个人如果借出去和还出去钱相等，说明可以退出这个系统，比如你借小明2元，小红欠你2元，虽然是两个过程，
        但是你在这个系统，没有导致自己的收入变多或者变少，上帝会帮你平衡这一切，你的退出不好影响系统。
        所以，我们可以计算出每个账号上有多少钱，正负表示自己拥有的财产。
        本身就是NP难问题，暴力回溯解决问

        """
        person = collections.defaultdict(int)
        for x, y, z in transactions:
            person[x] -= z
            person[y] += z
        # 账号
        accounts = list(person.values())
        # print(accounts)

        self.res = 0x7fffffff

        def dfs(cur_i, cnt):
            # 全局变量退出递归
            if cnt >= self.res:
                return
            # 账号为0不考虑
            while cur_i < len(accounts) and accounts[cur_i] == 0:
                cur_i += 1
            # 遍历完
            if cur_i == len(accounts):
                self.res = min(self.res, cnt)
                return
            for j in range(cur_i + 1, len(accounts)):
                if accounts[cur_i] * accounts[j] < 0:
                    accounts[j] += accounts[cur_i]
                    dfs(cur_i + 1, cnt + 1)
                    accounts[j] -= accounts[cur_i]

        dfs(0, 0)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def minTransfers(self, transactions):
        """九章"""
        debt = {}
        account = []
        len = 0
        for t in transactions:
            debt[t[0]] = debt.get(t[0], 0) - t[2]
            debt[t[1]] = debt.get(t[1], 0) + t[2]
        for v in debt.values():
            if v != 0:
                account.append(v)
                len = len + 1
        if len == 0:
            return 0

        dp = [0x7fffffff for x in range(0, 1 << len)]

        for i in range(1, 1 << len):
            sum = 0
            count = 0
            for j in range(0, len):
                if ((1 << j) & i) != 0:
                    sum = sum + account[j]
                    count = count + 1
            if sum == 0:
                dp[i] = count - 1
                for j in range(1, i):
                    if (i & j) == j and dp[j] + dp[i - j] < dp[i]:
                        dp[i] = dp[j] + dp[i - j]
        return dp[(1 << len) - 1]


@pytest.mark.parametrize("args,expected", [
    ([[0, 1, 10], [2, 0, 5]], 2),
    ([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]], 1),
])
def test_solutions(args, expected):
    assert Solution().minTransfers(args) == expected
    assert Solution1().minTransfers(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
