#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 23:55:22
# @Last Modified : 2020-07-06 23:55:22
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。 
# 
#  序号代表了一个元素有多大。序号编号的规则如下： 
# 
#  
#  序号从 1 开始编号。 
#  一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。 
#  每个数字的序号都应该尽可能地小。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [40,10,20,30]
# 输出：[4,1,2,3]
# 解释：40 是最大的元素。 10 是最小的元素。 20 是第二小的数字。 30 是第三小的数字。 
# 
#  示例 2： 
# 
#  输入：arr = [100,100,100]
# 输出：[1,1,1]
# 解释：所有元素有相同的序号。
#  
# 
#  示例 3： 
# 
#  输入：arr = [37,12,28,9,100,56,80,5,12]
# 输出：[5,3,4,2,8,6,7,1,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= arr.length <= 105 
#  -109 <= arr[i] <= 109 
#  
#  Related Topics 数组 
#  👍 23 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        lookup = {v:i for i, v in enumerate(sorted(set(arr)),1)}
        return [lookup[x] for x in arr]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(arr=[40, 10, 20, 30]), [4, 1, 2, 3]),
    pytest.param(dict(arr=[100, 100, 100]), [1, 1, 1]),
    pytest.param(dict(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]), [5, 3, 4, 2, 8, 6, 7, 1, 3]),
])
def test_solutions(kwargs, expected):
    assert Solution().arrayRankTransform(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
