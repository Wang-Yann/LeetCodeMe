#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-08 18:02:36
# @Last Modified : 2020-08-08 18:02:36
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

#
# 
#  Winston 构造了一个如上所示的函数 func 。他有一个整数数组 arr 和一个整数 target ，他想找到让 |func(arr, l, r) 
# - target| 最小的 l 和 r 。 
#

# def func(arr,l,r):
#     if r<l:
#         return -10**9
#     ans=arr[l]
#     for i in range(l+1,r+1):
#         ans&=arr[i]
#     return ans

#  请你返回 |func(arr, l, r) - target| 的最小值。 
# 
#  请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [9,12,3,7,15], target = 5
# 输出：2
# 解释：所有可能的 [l,r] 数对包括 [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,
# 2],[1,3],[2,4],[0,3],[1,4],[0,4]]， Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0
# ,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为 2 。
#  
# 
#  示例 2： 
# 
#  输入：arr = [1000000,1000000,1000000], target = 1
# 输出：999999
# 解释：Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。
#  
# 
#  示例 3： 
# 
#  输入：arr = [1,2,4,8,16], target = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  1 <= arr[i] <= 10^6 
#  0 <= target <= 10^7 
#  
#  Related Topics 位运算 线段树 二分查找 
#  👍 15 👎 0
	 


import pytest, traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode, ListNode
from sample_datas import BIG_CASE


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def closestToTarget(self, arr: List[int], target: int) -> int:
        """
        按位与运算满足交换律，即 a&b 等于 b&a；
        按位与运算满足结合律。 a&b&c=a&(b&c)
        所以给定的若干个数按照任意顺序进行按位与运算，得到的值都是相同的，即「按位与之和」的定义无歧义
        在按位与运算中，0 不能变回 1。因此值的变化的次数不会超过  arr[r] 二进制表示中 1 的个数，即  func(arr,l,r) 的值最多只有 20种。

        """

        ans = abs(arr[0] - target)
        valid = {arr[0]}
        for num in arr:
            valid = {x & num for x in valid} | {num}
            # print(valid)
            cur_min = min(abs(x - target) for x in valid)
            ans = min(ans, cur_min)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(arr=[9, 12, 3, 7, 15], target=5), 2],

    pytest.param(dict(arr=[1000000, 1000000, 1000000], target=1), 999999),
    pytest.param(dict(arr=[1, 2, 4, 8, 16], target=0), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().closestToTarget(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
