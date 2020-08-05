#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 15:48:02
# @Last Modified : 2020-08-05 15:48:02
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 楼下水果店正在促销，你打算买些苹果，arr[i] 表示第 i 个苹果的单位重量。 
# 
#  你有一个购物袋，最多可以装 5000 单位重量的东西，算一算，最多可以往购物袋里装入多少苹果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [100,200,150,1000]
# 输出：4
# 解释：所有 4 个苹果都可以装进去，因为它们的重量之和为 1450。
#  
# 
#  示例 2： 
# 
#  输入：arr = [900,950,800,1000,700,800]
# 输出：5
# 解释：6 个苹果的总重量超过了 5000，所以我们只能从中任选 5 个。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^3 
#  1 <= arr[i] <= 10^3 
#  
#  Related Topics 贪心算法 
#  👍 3 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        ans = 0
        cur_weight = 0
        for w in arr:
            cur_weight += w
            if cur_weight > 5000:
                break
            ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[100, 200, 150, 1000]), 4],
    [dict(arr=[900, 950, 800, 1000, 700, 800]), 5],
])
def test_solutions(kw, expected):
    assert Solution().maxNumberOfApples(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
