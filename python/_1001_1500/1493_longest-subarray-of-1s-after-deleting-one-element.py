#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 18:10:09
# @Last Modified : 2020-07-10 18:10:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个二进制数组 nums ，你需要从中删掉一个元素。 
# 
#  请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。 
# 
#  如果不存在这样的子数组，请返回 0 。 
# 
#  
# 
#  提示 1： 
# 
#  输入：nums = [1,1,0,1]
# 输出：3
# 解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。 
# 
#  示例 2： 
# 
#  输入：nums = [0,1,1,1,0,1,1,0,1]
# 输出：5
# 解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。 
# 
#  示例 3： 
# 
#  输入：nums = [1,1,1]
# 输出：2
# 解释：你必须要删除一个元素。 
# 
#  示例 4： 
# 
#  输入：nums = [1,1,0,0,1,1,1,0,1]
# 输出：4
#  
# 
#  示例 5： 
# 
#  输入：nums = [0,0,0]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  nums[i] 要么是 0 要么是 1 。 
#  
#  Related Topics 数组 
#  👍 6 👎 0

"""

import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result, count, left = 0, 0, 0
        for right in range(len(nums)):
            count += (nums[right] == 0)
            while count >= 2:
                count -= (nums[left] == 0)
                left += 1
            result = max(result, right - left + 1)
        return result - 1


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        AC
        Success: Runtime:40 ms, faster than 100.00% of Python3 online submissions.
         Memory Usage:16.1 MB, less than 100.00% of Python3 online submissions
        """
        ans = 0
        arr = [(num, len(list(grp))) for num, grp in itertools.groupby(nums)]
        if len(arr) == 1:
            return 0 if arr[0][0] == 0 else arr[0][1] - 1
        elif len(arr) == 2:
            return max(cnt if num == 1 else 0 for num, cnt in arr)
        else:
            arr = [(0, 0)] + arr + [(0, 0)]
            for i in range(1, len(arr) - 1):
                if arr[i] == (0, 1):
                    ans = max(arr[i - 1][1] + arr[i + 1][1], ans)
                elif arr[i][0] == 1:
                    ans = max(ans, arr[i][1])
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 1, 0, 1]), 3],
    [dict(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]), 5],
    [dict(nums=[1, 1, 1]), 2],
    [dict(nums=[1, 1, 0, 0, 1, 1, 1, 0, 1]), 4],
    [dict(nums=[0, 0, 0]), 0],
    [dict(nums=[1, 0, 0, 0, 0]), 1],
])
def test_solutions(kw, expected):
    assert Solution().longestSubarray(**kw) == expected
    assert Solution1().longestSubarray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
