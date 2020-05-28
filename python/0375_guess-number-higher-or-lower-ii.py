#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们正在玩一个猜数游戏，游戏规则如下： 
# 
#  我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。 
# 
#  每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。 
# 
#  然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。 
# 
#  示例: 
# 
#  n = 10, 我选择了8.
# 
# 第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
# 第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
# 第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。
# 
# 游戏结束。8 就是我选的数字。
# 
# 你最终要支付 5 + 7 + 9 = 21 块钱。
#  
# 
#  给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。 
#  Related Topics 极小化极大 动态规划

"""
import sys

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def getMoneyAmount(self, n: int) -> int:
        """
        TODO
        https://www.jiuzhang.com/solution/guess-number-higher-or-lower-ii#tag-other-lang-python
        dp[i][j]，代表着如果我们在区间 [i , j] 内进行查找，所需要的最少 cost 来保证找到结果

        对于区间 [i, j] ，猜测 i <= k <= j 我们可能出现以下三种结果：
       1. k 就是答案，此时子问题的额外 cost = 0 ，当前位置总 cost  = k + 0;
       2. k 过大，此时我们的有效区间缩小为 [i , k - 1] 当前操作总 cost  = k + dp[i][k - 1];
       3. k 过小，此时我们的有效区间缩小为 [k + 1 , j] 当前操作总 cost  = k + dp[k + 1][j];

        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # 如果只有一个数字，那么不用猜，cost为0
        for i in range(n + 1):
            dp[i][i] = 0
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                min_cost = sys.maxsize
                for k in range(i, j):
                    min_cost = min(min_cost, k + max(dp[i][k - 1], dp[k + 1][j]))
                dp[i][j] = min_cost
        return dp[1][n]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (10, 16),
])
def test_solutions(args, expected):
    assert Solution().getMoneyAmount(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
