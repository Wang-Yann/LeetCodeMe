#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。 
# 
#  完成所有替换操作后，请你返回这个数组。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：arr = [17,18,5,4,6,1]
# 输出：[18,6,6,6,1,-1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^4 
#  1 <= arr[i] <= 10^5 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        N = len(arr)
        ans = [0] * N
        for i in range(N - 1, -1, -1):
            ans[i] = max_val
            max_val = max(arr[i], max_val)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1])
])
def test_solutions(args, expected):
    assert Solution().replaceElements(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
