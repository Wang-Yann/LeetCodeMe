#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 
# 
#  二指输入法定制键盘在 XY 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处，例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1
# )，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。 
# 
#  给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。坐标 (x1,y1) 和 (x2,y2) 之间的
# 距离是 |x1 - x2| + |y1 - y2|。 
# 
#  注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。 
# 
#  
# 
#  示例 1： 
# 
#  输入：word = "CAKE"
# 输出：3
# 解释： 
# 使用两根手指输入 "CAKE" 的最佳方案之一是： 
# 手指 1 在字母 'C' 上 -> 移动距离 = 0 
# 手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2 
# 手指 2 在字母 'K' 上 -> 移动距离 = 0 
# 手指 2 在字母 'E' 上 -> 移动距离 = 从字母 'K' 到字母 'E' 的距离  = 1 
# 总距离 = 3
#  
# 
#  示例 2： 
# 
#  输入：word = "HAPPY"
# 输出：6
# 解释： 
# 使用两根手指输入 "HAPPY" 的最佳方案之一是：
# 手指 1 在字母 'H' 上 -> 移动距离 = 0
# 手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'H' 到字母 'A' 的距离 = 2
# 手指 2 在字母 'P' 上 -> 移动距离 = 0
# 手指 2 在字母 'P' 上 -> 移动距离 = 从字母 'P' 到字母 'P' 的距离 = 0
# 手指 1 在字母 'Y' 上 -> 移动距离 = 从字母 'A' 到字母 'Y' 的距离 = 4
# 总距离 = 6
#  
# 
#  示例 3： 
# 
#  输入：word = "NEW"
# 输出：3
#  
# 
#  示例 4： 
# 
#  输入：word = "YEAR"
# 输出：7
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= word.length <= 300 
#  每个 word[i] 都是一个大写英文字母。 
#  
#  Related Topics 动态规划

"""
import string

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minimumDistance(self, word: str) -> int:
        """
        HARD
        """
        INT_MAX = 0x7fffffff

        def distance(a, b):
            if -1 in [a, b]:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        dp = {(-1, -1):0}
        for char in word:
            c = ord(char) - ord("A")
            new_dp = {}
            for l, r in dp:
                new_dp[c, r] = min(new_dp.get((c, r), INT_MAX), dp[l, r] + distance(l, c))
                new_dp[l, c] = min(new_dp.get((l, c), INT_MAX), dp[l, r] + distance(r, c))
            dp = new_dp
        return min(dp.values())


# leetcode submit region end(Prohibit modification and deletion)




@pytest.mark.parametrize("kwargs,expected", [
    (dict(word="CAKE"), 3),
    pytest.param(dict(word="HAPPY"), 6),
    pytest.param(dict(word="NEW"), 3),
    pytest.param(dict(word="YEAR"), 7),
])
def test_solutions(kwargs, expected):
    assert Solution().minimumDistance(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
