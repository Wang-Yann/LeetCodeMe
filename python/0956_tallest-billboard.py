#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。 
# 
#  你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为 1、2 和 3，则可以将它们焊接在一起形成长度为 6 的支架。 
# 
#  返回广告牌的最大可能安装高度。如果没法安装广告牌，请返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,6]
# 输出：6
# 解释：我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。
#  
# 
#  示例 2： 
# 
#  输入：[1,2,3,4,5,6]
# 输出：10
# 解释：我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。 
# 
#  示例 3： 
# 
#  输入：[1,2]
# 输出：0
# 解释：没法安装广告牌，所以返回 0。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= rods.length <= 20 
#  1 <= rods[i] <= 1000 
#  钢筋的长度总和最多为 5000 
#  
#  Related Topics 动态规划

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """
        官方题解
        对于每一根钢筋 x，我们会写下 +x，-x 或者 0。我们的目标是最终得到结果 0 并让正数之和最大。我们记所有写下的正数之和为 score
        dp[i][s] 表示当我们可以使用 rods[j] (j >= i) 时能得到的最大 score
        """

        @functools.lru_cache(None)
        def dp(i, s):
            # 边界
            if i == len(rods):
                return 0 if s == 0 else float("-inf")
            ans = max(
                dp(i + 1, s),
                dp(i + 1, s - rods[i]),
                dp(i + 1, s + rods[i]) + rods[i]
            )
            # print(i, s, ans)
            return ans

        return dp(0, 0)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    # ([1, 2, 3, 6], 6),
    ([1, 2, 3, 4, 5, 6], 10),
    # ([1, 2], 0),
])
def test_solutions(args, expected):
    assert Solution().tallestBillboard(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
