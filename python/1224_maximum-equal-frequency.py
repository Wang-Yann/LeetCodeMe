#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回其长度： 
# 
#  
#  从前缀中 删除一个 元素后，使得所剩下的每个数字的出现次数相同。 
#  
# 
#  如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [2,2,1,1,5,3,3,5]
# 输出：7
# 解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4]=5，就可以得到 [2,2,1,1,3,3]，里面每个数字都
# 出现了两次。
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# 输出：13
#  
# 
#  示例 3： 
# 
#  输入：nums = [1,1,1,2,2,2]
# 输出：5
#  
# 
#  示例 4： 
# 
#  输入：nums = [10,2,8,9,3,8,1,5,2,3,7,6]
# 输出：8
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10^5 
#  1 <= nums[i] <= 10^5 
#  
#  Related Topics 哈希表

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        """
        理解答案都费力
        count[a] means the frequency of number a
        freq[c] means how many numbers that occur c times.

        Iterate the input array A and we count the n first numbers.

        There actually only 2 situations to discuss:

        1.we delete the current number a.
        In this case, the n - 1 first numbers have the same frequency,
        and we can easier detect this case when we iterate the previous number A[n - 1]

        2.we don't delete the current number a
        the current a occurs c times.
        So except all numbers that also occurs c times,
        it should leave one single number, or c + 1 same number.

        """
        counter = collections.Counter()
        freq = [0 for _ in range(len(nums) + 1)]
        res = 0
        for idx, a_num in enumerate(nums, 1):
            freq[counter[a_num]] -= 1
            freq[counter[a_num] + 1] += 1
            counter[a_num] += 1
            c = counter[a_num]
            # print(idx,a_num,freq,c )
            if freq[c] * c == idx and idx < len(nums):
                res = idx + 1
            remain = idx - freq[c] * c
            if remain in [c + 1, 1] and freq[remain] == 1:
                res = idx
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[2, 2, 1, 1, 5, 3, 3, 5]), 7],
    # [dict(nums=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]), 13],
    # [dict(nums=[1, 1, 1, 2, 2, 2]), 5],
    # [dict(nums=[10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]), 8],
])
def test_solutions(kw, expected):
    assert Solution().maxEqualFreq(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
