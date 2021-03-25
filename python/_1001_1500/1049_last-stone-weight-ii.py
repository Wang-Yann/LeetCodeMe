#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有一堆石头，每块石头的重量都是正整数。 
# 
#  每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下： 
# 
#  
#  如果 x == y，那么两块石头都会被完全粉碎； 
#  如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。 
#  
# 
#  最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。 
# 
#  
# 
#  示例： 
# 
#  输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= stones.length <= 30 
#  1 <= stones[i] <= 1000 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/last-stone-weight-ii/solution/shao-wei-nao-jin-zhuan-ge-wan-yong-shi-ji-bai-9778/
        分成两组　使两组和的差值最小==>查找一组　最接近sum//2 ==>背包
        """
        sum_val = sum(stones)
        capacity = sum_val // 2
        N = len(stones)
        dp = [0] * (capacity + 1)
        for i in range(N):
            cur_stone = stones[i]
            for c in range(capacity, cur_stone - 1, -1):
                dp[c] = max(dp[c], dp[c - cur_stone] + cur_stone)
        # print(dp)
        return sum_val-2*dp[capacity]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([2, 7, 4, 1, 8, 1], 1),
])
def test_solutions(args, expected):
    assert Solution().lastStoneWeightII(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
