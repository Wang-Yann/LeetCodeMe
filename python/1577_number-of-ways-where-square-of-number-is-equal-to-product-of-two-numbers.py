#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 06:14:09
# @Last Modified : 2021-02-24 06:14:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
 给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：


  类型 1：三元组 (i, j, k) ，如果 nums1[i]2 == nums2[j] * nums2[k] 其中 0 <= i < nums1.len
 gth 且 0 <= j < k < nums2.length
  类型 2：三元组 (i, j, k) ，如果 nums2[i]2 == nums1[j] * nums1[k] 其中 0 <= i < nums2.len
 gth 且 0 <= j < k < nums1.length




  示例 1：

  输入：nums1 = [7,4], nums2 = [5,2,8,9]
 输出：1
 解释：类型 1：(1,1,2), nums1[1]^2 = nums2[1] * nums2[2] (4^2 = 2 * 8)

  示例 2：

  输入：nums1 = [1,1], nums2 = [1,1,1]
 输出：9
 解释：所有三元组都符合题目要求，因为 1^2 = 1 * 1
 类型 1：(0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2), nums1[i]^2 = nums2[
 j] * nums2[k]
 类型 2：(0,0,1), (1,0,1), (2,0,1), nums2[i]^2 = nums1[j] * nums1[k]


  示例 3：

  输入：nums1 = [7,7,8,3], nums2 = [1,2,9,7]
 输出：2
 解释：有两个符合题目要求的三元组
 类型 1：(3,0,2), nums1[3]^2 = nums2[0] * nums2[2]
 类型 2：(3,0,1), nums2[3]^2 = nums1[0] * nums1[1]


  示例 4：

  输入：nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
 输出：0
 解释：不存在符合题目要求的三元组




  提示：


  1 <= nums1.length, nums2.length <= 1000
  1 <= nums1[i], nums2[i] <= 10^5

  Related Topics 哈希表 数学
  👍 7 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        ans = 0
        for i in range(2):
            for k1, v1 in counter1.items():
                for k2, v2 in counter2.items():
                    quotient, rest = divmod(k1 ** 2, k2)
                    if rest != 0 or quotient not in counter2:
                        continue
                    # print(k1,v1,k2,v2)
                    if quotient == k2:
                        ans += v1 * v2 * (v2 - 1)
                    else:
                        ans += v1 * v2 * counter2[quotient]
            counter2, counter1 = counter1, counter2
        return ans // 2


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums1=[7, 4], nums2=[5, 2, 8, 9]), 1],
    [dict(nums1=[1, 1], nums2=[1, 1, 1]), 9],
    [dict(nums1=[7, 7, 8, 3], nums2=[1, 2, 9, 7]), 2],
    [dict(nums1=[4, 7, 9, 11, 23], nums2=[3, 5, 1024, 12, 18]), 0],
])
@pytest.mark.parametrize("SolutionCls", [Solution, ])
def test_solutions(kw, expected, SolutionCls):
    assert SolutionCls().numTriplets(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
