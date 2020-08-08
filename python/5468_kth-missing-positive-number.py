#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 01:55:55
# @Last Modified : 2020-08-09 01:55:55
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。 
# 
#  请你找到这个数组里第 k 个缺失的正整数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [2,3,4,7,11], k = 5
# 输出：9
# 解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,2,3,4], k = 2
# 输出：6
# 解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 1000 
#  1 <= arr[i] <= 1000 
#  1 <= k <= 1000 
#  对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j] 
#  
#  Related Topics 数组 哈希表 
#  👍 0 👎 0
	 

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
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = 1
        for num in arr:
            k -= (num-last)
            if k <= 0:
                return num+k-1
            last = num+1

        return last+k-1

# leetcode submit region end(Prohibit modification and deletion)



class Solution5468:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        N = len(arr)
        i = 0
        cur = 1
        while i < N:
            if cur != arr[i]:
                k -= 1
                cur += 1
            else:
                cur += 1
                i += 1
            if k == 0:
                break

        return cur + k - 1


@pytest.mark.parametrize("kwargs,expected", [
    [dict(arr=[2, 3, 4, 7, 11], k=5), 9],

    pytest.param(dict(arr=[1, 2, 3, 4], k=2), 6),
    pytest.param(dict(arr=[2], k=1), 1),
])
def test_solutions5468(kwargs, expected):
    assert Solution5468().findKthPositive(**kwargs) == expected
    assert Solution().findKthPositive(**kwargs) == expected



if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])