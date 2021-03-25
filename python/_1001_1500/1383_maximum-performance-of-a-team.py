#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 22:38:32
# @Last Modified : 2020-07-05 22:38:32
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 公司有编号为 1 到 n 的 n 个工程师，给你两个数组 speed 和 efficiency ，其中 speed[i] 和 efficiency[i] 分
# 别代表第 i 位工程师的速度和效率。请你返回由最多 k 个工程师组成的 最大团队表现值 ，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。 
# 
#  团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# 输出：60
# 解释：
# 我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 per
# formance = (10 + 5) * min(4, 7) = 60 。
#  
# 
#  示例 2： 
# 
#  输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# 输出：68
# 解释：
# 此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance = 
# (2 + 10 + 5) * min(5, 4, 7) = 68 。
#  
# 
#  示例 3： 
# 
#  输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# 输出：72
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^5 
#  speed.length == n 
#  efficiency.length == n 
#  1 <= speed[i] <= 10^5 
#  1 <= efficiency[i] <= 10^8 
#  1 <= k <= n 
#  
#  Related Topics 贪心算法 排序 
#  👍 38 👎 0

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """
        GOOD 注意领会
        采用「动一个，定一个」的策略——即我们可以枚举效率的最小值
        TODO"""
        res = sSum = 0
        min_heap = []
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(min_heap, s)
            sSum += s
            if len(min_heap) > k:
                sSum -= heapq.heappop(min_heap)
            res = max(res, sSum * e)
        return res % (10 ** 9 + 7)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2), 60),
    pytest.param(dict(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=3), 68),
    pytest.param(dict(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=4), 72),
])
def test_solutions(kwargs, expected):
    assert Solution().maxPerformance(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
