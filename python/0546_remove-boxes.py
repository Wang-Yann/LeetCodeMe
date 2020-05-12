#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。 
# 你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分
# 。 
# 当你将所有盒子都去掉之后，求你能获得的最大积分和。 
# 
#  示例 1： 
# 输入: 
# 
#  
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
#  
# 
#  输出: 
# 
#  
# 23
#  
# 
#  解释: 
# 
#  
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
# ----> [1, 3, 3, 3, 1] (1*1=1 分) 
# ----> [1, 1] (3*3=9 分) 
# ----> [] (2*2=4 分)
#  
# 
#  
# 
#  提示：盒子的总数 n 不会超过 100。 
#  Related Topics 深度优先搜索 动态规划

"""
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    元素  dp[l][r][k] ,l 表示起始下标，r 表示结束下表，k 表示与第 r 个元素相似的元素个数，可以在最后一起合并并得到最终的分数存入 dp[l][r][k]


    https://leetcode-cn.com/problems/remove-boxes/solution/yi-chu-he-zi-by-leetcode/
    """

    def removeBoxes(self, boxes: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(l, r, k):
            if l > r:
                return 0
            while l < r and boxes[l + 1] == boxes[l]:
                l += 1
                k += 1
            res = dfs(l + 1, r, 0) + (k + 1) ** 2
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    res = max(res, dfs(l + 1, i - 1, 0) + dfs(i, r, k + 1))
            return res

        length = len(boxes)
        # lookup = [ [  [0]*length for _ in range(length)  ] for _ in range(length)]
        return dfs(0, length - 1, 0)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([1, 3, 2, 2, 2, 3, 4, 3, 1], 23),
])
def test_solutions(args, expected):
    assert Solution().removeBoxes(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
