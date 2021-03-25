#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-26 23:52:11
# @Last Modified : 2020-07-26 23:52:11
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 假设我们在一条水平数轴上，列表 stations 来表示各个加油站的位置，加油站分别在 stations[0], stations[1], ..., sta
# tions[N-1] 的位置上，其中 N = stations.length。 
# 
#  现在我们希望增加 K 个新的加油站，使得相邻两个加油站的距离 D 尽可能的最小，请你返回 D 可能的最小值。 
# 
#  示例： 
# 
#  输入：stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# 输出：0.500000
#  
# 
#  注： 
# 
#  
#  stations.length 是在范围 [10, 2000] 内的整数 
#  stations[i] 是在范围 [0, 10^8] 内的整数 
#  K 是在范围 [1, 10^6] 内的整数 
#  在 10^-6 以内的正确值会被视为正确的答案 
#  
#  Related Topics 二分查找 
#  👍 14 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        """
        二分
        GOOD
        """

        def possible(D):
            sum_val = sum(
                int((stations[i + 1] - stations[i]) / D)
                for i in range(N - 1)
            )
            return sum_val <= K

        N = len(stations)
        lo, hi = 0, 10 ** 8
        while hi - lo > 1e-6:
            mid = (lo + hi) / 2.0
            if possible(mid):
                hi = mid
            else:
                lo = mid
        return lo


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(stations=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K=9), 0.5000000],

])
def test_solutions(kwargs, expected):
    assert Solution().minmaxGasDist(**kwargs) == pytest.approx(expected, 1e-6)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
