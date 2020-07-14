#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 20:55:17
# @Last Modified : 2020-07-14 20:55:17
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请
# 编写代码计算叠罗汉最多能叠几个人。 
# 
#  示例： 
# 
#  输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
# 输出：6
# 解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190) 
# 
# 
#  提示： 
# 
#  
#  height.length == weight.length <= 10000 
#  
#  Related Topics 排序 二分查找 动态规划 
#  👍 37 👎 0


"""

import bisect
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        """LIS"""
        arr = sorted(zip(height, weight), key=lambda x:(x[0], -x[1]))
        dp = []
        for h, w in arr:
            pos = bisect.bisect_left(dp, w)
            if pos == len(dp):
                dp.append(w)
            else:
                dp[pos] = w
        # print(dp)
        return len(dp)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(height=[65, 70, 56, 75, 60, 68], weight=[100, 150, 90, 190, 95, 110]), 6],
    [dict(height=[1, 2, 3, 4], weight=[4, 3, 2, 1]), 1],

])
def test_solutions(kwargs, expected):
    assert Solution().bestSeqAtIndex(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
