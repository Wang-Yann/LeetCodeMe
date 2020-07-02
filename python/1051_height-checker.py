#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。 
# 
#  请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。 
# 
#  注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。 
# 
#  
# 
#  示例： 
# 
#  输入：heights =[1,1,4,2,1,3]
# 输出：3 
# 解释：
# 当前数组：[1,1,4,2,1,3]
# 目标数组：[1,1,1,2,3,4]
# 在下标 2 处（从 0 开始计数）出现 4 vs 1 ，所以我们必须移动这名学生。
# 在下标 4 处（从 0 开始计数）出现 1 vs 3 ，所以我们必须移动这名学生。
# 在下标 5 处（从 0 开始计数）出现 3 vs 4 ，所以我们必须移动这名学生。 
# 
#  示例 2： 
# 
#  输入：heights = [5,1,2,3,4]
# 输出：5
#  
# 
#  示例 3： 
# 
#  输入：heights = [1,2,3,4,5]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= heights.length <= 100 
#  1 <= heights[i] <= 100 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        ans = 0
        for sh, h in zip(sorted_heights, heights):
            if sh != h:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(heights=[1, 1, 4, 2, 1, 3]), 3],
    [dict(heights=[5, 1, 2, 3, 4]), 5],
    [dict(heights=[1, 2, 3, 4, 5]), 0],
])
def test_solutions(kw, expected):
    assert Solution().heightChecker(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
