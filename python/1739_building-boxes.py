#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 08:51:25
# @Last Modified : 2021-02-23 08:51:25
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有一个立方体房间，其长度、宽度和高度都等于 n 个单位。请你在房间里放置 n 个盒子，每个盒子都是一个单位边长的立方体。放置规则如下： 
# 
#  
#  你可以把盒子放在地板上的任何地方。 
#  如果盒子 x 需要放置在盒子 y 的顶部，那么盒子 y 竖直的四个侧面都 必须 与另一个盒子或墙相邻。 
#  
# 
#  给你一个整数 n ，返回接触地面的盒子的 最少 可能数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：n = 3
# 输出：3
# 解释：上图是 3 个盒子的摆放位置。
# 这些盒子放在房间的一角，对应左侧位置。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：n = 4
# 输出：3
# 解释：上图是 3 个盒子的摆放位置。
# 这些盒子放在房间的一角，对应左侧位置。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：n = 10
# 输出：6
# 解释：上图是 10 个盒子的摆放位置。
# 这些盒子放在房间的一角，对应后方位置。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 109 
#  
#  Related Topics 数学 二分查找 
#  👍 14 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumBoxes(self, n: int) -> int:
        # 模拟放方块的过程
        """
        https://leetcode.com/problems/building-boxes/discuss/1032016/C%2B%2B-Python-3-variables-solution-with-drawing-explanation
        """
        nextOutBound = curLevelTotalBox = total = 0
        while total < n:
            nextOutBound += 1
            curLevelTotalBox += nextOutBound
            total += curLevelTotalBox
            # print(edge,bottom,total)
        if total == n:
            return curLevelTotalBox
        total -= curLevelTotalBox
        curLevelTotalBox -= nextOutBound
        nextOutBound = 0
        while total < n:
            nextOutBound += 1
            total += nextOutBound
        return curLevelTotalBox + nextOutBound


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=3), 3],
    [dict(n=4), 3],
    [dict(n=10), 6],
])
def test_solutions(kw, expected):
    assert Solution().minimumBoxes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
