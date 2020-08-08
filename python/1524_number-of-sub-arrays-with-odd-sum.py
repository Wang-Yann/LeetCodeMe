#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-08 18:29:50
# @Last Modified : 2020-08-08 18:29:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr 。请你返回和为 奇数 的子数组数目。 
# 
#  由于答案可能会很大，请你将结果对 10^9 + 7 取余后返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [1,3,5]
# 输出：4
# 解释：所有的子数组为 [[1],[1,3],[1,3,5],[3],[3,5],[5]] 。
# 所有子数组的和为 [1,4,9,3,8,5].
# 奇数和包括 [1,9,3,5] ，所以答案为 4 。
#  
# 
#  示例 2 ： 
# 
#  输入：arr = [2,4,6]
# 输出：0
# 解释：所有子数组为 [[2],[2,4],[2,4,6],[4],[4,6],[6]] 。
# 所有子数组和为 [2,6,12,4,10,6] 。
# 所有子数组和都是偶数，所以答案为 0 。
#  
# 
#  示例 3： 
# 
#  输入：arr = [1,2,3,4,5,6,7]
# 输出：16
#  
# 
#  示例 4： 
# 
#  输入：arr = [100,100,99,99]
# 输出：4
#  
# 
#  示例 5： 
# 
#  输入：arr = [7]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  1 <= arr[i] <= 100 
#  
#  Related Topics 数组 数学 
#  👍 8 👎 0
	 

"""

import pytest,traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode,ListNode
from sample_datas import BIG_CASE





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        GOOD
        统计一下前缀和中有几个奇数几个偶数，答案其实就是 奇数的个数×偶数的个数+奇数的个数
        从前缀和里随意选出两个数做差，差值就是子数组的和，当选出的两个数是一个奇数一个偶数时，
        子数组的和是奇数，所以这样的选法一共有 奇数的个数×偶数的个数 这么多种


        """
        MOD=10**9+7
        odd = sum(i & 1 for i in itertools.accumulate(arr))
        # print(list(itertools.accumulate(arr)))
        return odd * (len(arr) - odd + 1) % MOD

# leetcode submit region end(Prohibit modification and deletion)
	

@pytest.mark.parametrize("kwargs,expected", [
    [dict(      arr = [1,3,5]                          ), 4],

    pytest.param(dict(  arr = [2,4,6]                   ), 0),
    pytest.param(dict(  arr = [1,2,3,4,5,6,7]                   ), 16),
    pytest.param(dict(  arr = [100,100,99,99]                 ), 4),
    pytest.param(dict(  arr = [7]                ), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().numOfSubarrays(**kwargs) == expected







if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])