#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-03 11:35:52
# @Last Modified : 2020-08-03 11:35:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出一个有序数组 A，数组中的每个数字都是 独一无二的，找出从数组最左边开始的第 K 个缺失数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [4,7,9,10], K = 1
# 输出：5
# 解释：
# 第一个缺失数字为 5 。
#  
# 
#  示例 2： 
# 
#  输入：A = [4,7,9,10], K = 3
# 输出：8
# 解释： 
# 缺失数字有 [5,6,8,...]，因此第三个缺失数字为 8 。
#  
# 
#  示例 3： 
# 
#  输入：A = [1,2,4], K = 3
# 输出：6
# 解释：
# 缺失数字有 [3,5,6,7,...]，因此第三个缺失数字为 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 50000 
#  1 <= A[i] <= 1e7 
#  1 <= K <= 1e8 
#  
#  Related Topics 二分查找 
#  👍 23 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing_count(idx):
            return (nums[idx] - nums[0] + 1) - (idx - 0 + 1)

        def check(idx):
            return k <= missing_count(idx)

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid-1
            else:
                l = mid + 1
        # print(l,r)
        return nums[r] + (k - missing_count(r))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A=[4, 7, 9, 10], K=1), 5],
    [dict(A=[4, 7, 9, 10], K=3), 8],
    [dict(A=[1, 2, 4], K=3), 6],
    [dict(A=[1, 2, 4], K=30), 33],
])
def test_solutions(kw, expected):
    kw["nums"] = kw.pop("A")
    kw["k"] = kw.pop("K")
    assert Solution().missingElement(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
