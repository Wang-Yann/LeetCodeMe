#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 23:34:56
# @Last Modified : 2020-07-14 23:34:56
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？ 
# 
#  以任意顺序返回这两个数字均可。 
# 
#  示例 1: 
# 
#  输入: [1]
# 输出: [2,3] 
# 
#  示例 2: 
# 
#  输入: [2,3]
# 输出: [1,4] 
# 
#  提示： 
# 
#  
#  nums.length <= 30000 
#  
#  Related Topics 数组 数学 
#  👍 18 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sumTwoBlank = (n + 2) * (n + 3) // 2 - sum(nums)
        # print(sumTwoBlank)
        div = sumTwoBlank / 2
        # 分组异或
        a, b = 0, 0
        for num in nums:
            if num >= div:
                a ^= num
            else:
                b ^= num
        for i in range(1, n + 3):
            if i >= div:
                a ^= i
            else:
                b ^= i
        return [a, b]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([1], [2, 3]),
    pytest.param([2, 3], [1, 4]),
])
def test_solutions(args, expected):
    res = Solution().missingTwo(args)
    assert sorted(res) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
