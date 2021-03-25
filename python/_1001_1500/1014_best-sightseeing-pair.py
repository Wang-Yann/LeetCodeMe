#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。 
# 
#  一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。 
# 
#  返回一对观光景点能取得的最高分。 
# 
#  
# 
#  示例： 
# 
#  输入：[8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 50000 
#  1 <= A[i] <= 1000 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        """
        对于输入中的每一个 A[j] 来说， 它的值 A[j] 和它的下标 j 都是固定的，
        所以 A[j] - j 的值也是固定的。
        因此，对于每个 A[j] 而言， 想要求 res 的最大值，也就是要求 A[i] + i （i < j） 的最大值，
        所以不妨用一个变量 pre_max 记录当前元素 A[j] 之前的 A[i] + i 的最大值，
        这样对于每个 A[j] 来说，都有 最大得分 = pre_max + A[j] - j
        """
        res = 0
        pre_max = A[0] + 0  # 初始值
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j)  # 判断能否刷新res
            pre_max = max(pre_max, A[j] + j)  # 判断能否刷新pre_max， 得到更大的A[i] + i

        return res


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res, cur = 0, 0
        for x in A:
            res = max(res, cur + x)
            cur = max(cur, x) - 1
        return res


@pytest.mark.parametrize("args,expected", [
    ([8, 1, 5, 2, 6], 11)
])
def test_solutions(args, expected):
    assert Solution().maxScoreSightseeingPair(args) == expected
    assert Solution1().maxScoreSightseeingPair(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
