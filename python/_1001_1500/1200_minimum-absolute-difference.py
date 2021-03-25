#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你个整数数组 arr，其中每个元素都 不相同。 
# 
#  请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [4,2,1,3]
# 输出：[[1,2],[2,3],[3,4]]
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,3,6,10,15]
# 输出：[[1,3]]
#  
# 
#  示例 3： 
# 
#  输入：arr = [3,8,-10,23,19,-4,-14,27]
# 输出：[[-14,-10],[19,23],[23,27]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= arr.length <= 10^5 
#  -10^6 <= arr[i] <= 10^6 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        min_diff = float("inf")
        arr.sort()
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i + 1]]]
            elif diff == min_diff:
                result.append([arr[i], arr[i + 1]])
        return result


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        N = len(arr)
        min_gap = min(arr[i] - arr[i - 1] for i in range(1, N))
        ans = []
        arr_set = set(arr)
        for v in arr:
            if v + min_gap in arr_set:
                ans.append([v, v + min_gap])
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[4, 2, 1, 3]), [[1, 2], [2, 3], [3, 4]]],
    [dict(arr=[1, 3, 6, 10, 15]), [[1, 3]]],
    [dict(arr=[3, 8, -10, 23, 19, -4, -14, 27]), [[-14, -10], [19, 23], [23, 27]]],
])
def test_solutions(kw, expected):
    assert Solution().minimumAbsDifference(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
