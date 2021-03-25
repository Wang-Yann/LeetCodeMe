#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 10:43:46
# @Last Modified : 2021-02-25 10:43:46
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。 
# 
#  数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。 
# 
#  在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力 
# 。 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,5,2,6], k = 2
# 输出：[2,6]
# 解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,4,3,3,5,4,9,6], k = 4
# 输出：[2,3,3,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  0 <= nums[i] <= 109 
#  1 <= k <= nums.length 
#  
#  Related Topics 栈 堆 贪心算法 队列 
#  👍 49 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """单调栈"""
        stack = []
        N = len(nums)
        for i, a in enumerate(nums):
            while stack and stack[-1] > a and N - i > k - len(stack):
                stack.pop()
            if len(stack) < k:
                stack.append(a)
        return stack


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[3, 5, 2, 6], k=2), [2, 6]],
    [dict(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4), [2, 3, 3, 4]],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().mostCompetitive(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
