#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 03:35:24
# @Last Modified : 2021-02-25 03:35:24
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 如果一个数列由至少两个元素组成，且每两个连续元素之间的差值都相同，那么这个序列就是 等差数列 。更正式地，数列 s 是等差数列，只需要满足：对于每个有效的 
# i ， s[i+1] - s[i] == s[1] - s[0] 都成立。 
# 
#  例如，下面这些都是 等差数列 ： 
# 
#  1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9 
# 
#  下面的数列 不是等差数列 ： 
# 
#  1, 1, 2, 5, 7 
# 
#  给你一个由 n 个整数组成的数组 nums，和两个由 m 个整数组成的数组 l 和 r，后两个数组表示 m 组范围查询，其中第 i 个查询对应范围 [l[
# i], r[i]] 。所有数组的下标都是 从 0 开始 的。 
# 
#  返回 boolean 元素构成的答案列表 answer 。如果子数组 nums[l[i]], nums[l[i]+1], ... , nums[r[i]]
#  可以 重新排列 形成 等差数列 ，answer[i] 的值就是 true；否则answer[i] 的值就是 false 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
# 输出：[true,false,true]
# 解释：
# 第 0 个查询，对应子数组 [4,6,5] 。可以重新排列为等差数列 [6,5,4] 。
# 第 1 个查询，对应子数组 [4,6,5,9] 。无法重新排列形成等差数列。
# 第 2 个查询，对应子数组 [5,9,3,7] 。可以重新排列为等差数列 [3,5,7,9] 。 
# 
#  示例 2： 
# 
#  输入：nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4
# ,4,9,7,9,10]
# 输出：[false,true,false,false,true,true]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  m == l.length 
#  m == r.length 
#  2 <= n <= 500 
#  1 <= m <= 500 
#  0 <= l[i] < r[i] < n 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics 排序 
#  👍 9 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArith(arr):
            st = set(arr)
            if len(arr) != len(st):
                return len(st) == 1  # take care of duplicates
            mx, mn, = max(arr), min(arr)
            if (mx - mn) % (len(arr) - 1) != 0:
                return False
            step = (mx - mn) // (len(arr) - 1)
            for i in range(mn, mx, step):
                if i not in st:
                    return False
            return True

        return [isArith(nums[start:stop + 1]) for start, stop in zip(l, r)]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
          l=[0, 1, 6, 4, 8, 7], r=[4, 4, 9, 7, 9, 10]), [False, True, False, False, True, True]],
    [dict(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]), [True, False, True]],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().checkArithmeticSubarrays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
