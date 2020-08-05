#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 16:36:55
# @Last Modified : 2020-08-05 16:36:55
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出三个均为 严格递增排列 的整数数组 arr1，arr2 和 arr3。 
# 
#  返回一个由 仅 在这三个数组中 同时出现 的整数所构成的有序数组。 
# 
#  
# 
#  示例： 
# 
#  输入: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# 输出: [1,5]
# 解释: 只有 1 和 5 同时在这三个数组中出现.
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr1.length, arr2.length, arr3.length <= 1000 
#  1 <= arr1[i], arr2[i], arr3[i] <= 2000 
#  
#  Related Topics 哈希表 双指针 
#  👍 13 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        ans = []
        N1, N2, N3 = map(len, (arr1, arr2, arr3))
        while i < N1 and j < N2 and k < N3:
            max_v = max(arr1[i], arr2[j], arr3[k])
            if max_v == arr1[i] == arr2[j] == arr3[k]:
                ans.append(max_v)
                i += 1
                j += 1
                k += 1
            while i < N1 and arr1[i] < max_v:
                i += 1
            while j < N2 and arr2[j] < max_v:
                j += 1
            while k < N3 and arr3[k] < max_v:
                k += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(arr1=[1, 2, 3, 4, 5], arr2=[1, 2, 5, 7, 9], arr3=[1, 3, 4, 5, 8]), [1, 5]],
])
def test_solutions(kw, expected):
    assert Solution().arraysIntersection(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
