#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 22:13:46
# @Last Modified : 2020-07-14 22:13:46
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩
# 师找到最优的预约集合（总预约时间最长），返回总的分钟数。 
# 
#  注意：本题相对原题稍作改动 
# 
#  
# 
#  示例 1： 
# 
#  输入： [1,2,3,1]
# 输出： 4
# 解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
#  
# 
#  示例 2： 
# 
#  输入： [2,7,9,3,1]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
#  
# 
#  示例 3： 
# 
#  输入： [2,1,4,5,3,1,1,3]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
#  
#  Related Topics 动态规划 
#  👍 112 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def massage(self, nums: List[int]) -> int:
        choose = no_choose = 0
        for v in nums:
            no_choose, choose = max(no_choose, choose), max(choose, no_choose + v)
        return max(no_choose, choose)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 1], 4),
    pytest.param([2, 7, 9, 3, 1], 12),
    pytest.param([2, 1, 4, 5, 3, 1, 1, 3], 12),
])
def test_solutions(args, expected):
    assert Solution().massage(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
