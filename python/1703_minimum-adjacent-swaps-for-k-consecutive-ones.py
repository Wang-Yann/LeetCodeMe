#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 06:29:52
# @Last Modified : 2021-02-23 06:29:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 给你一个整数数组 nums 和一个整数 k 。 nums 仅包含 0 和 1 。每一次移动，你可以选择 相邻 两个数字并将它们交换。
# 
#  请你返回使 nums 中包含 k 个 连续 1 的 最少 交换次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,0,0,1,0,1], k = 2
# 输出：1
# 解释：在第一次操作时，nums 可以变成 [1,0,0,0,1,1] 得到连续两个 1 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,0,0,0,0,0,1,1], k = 3
# 输出：5
# 解释：通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,1,1,1] 。
#  
# 
#  示例 3： 
# 
#  输入：nums = [1,1,0,1], k = 2
# 输出：0
# 解释：nums 已经有连续 2 个 1 了。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  nums[i] 要么是 0 ，要么是 1 。 
#  1 <= k <= sum(nums) 
#  
#  Related Topics 栈 
#  👍 17 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/discuss/987347/JavaC%2B%2BPython-Solution
        Find all index of nums[i] if nums[i] == 1.
        Now the problem changes to,
        find k consecute element in A,
        that has minimum distance to their median sequence.
        To solve this, we need to use the prefix sum of A,
        which is B in this solution.
        ---
        EXPLANATIONS:
        I worked out how this magic works
        B[i + k] - B[k / 2 + i] - B[(k + 1) / 2 + i] + B[i])

        example indices (A):
        [0 3 5 6 7 9 10]
        mid = 6
        sum before mid => (6 - 6 - 0) + (6 - 3 - 1) + (6 - 5 - 2) + (6 - 0 - 3)
        => 6 * 4 - (0 + 3 + 5 + 6) - (0 + 1 + 2 + 3)

        sum after mid => (6 - 6 - 0) + (7 - 6 - 1) + (9 - 6 - 2) + (10 - 6 - 3)
        => (6 + 7 + 9 + 10) - 6 * 4 - (0 + 1 + 2 + 3)

        before + after => (6 + 7 + 9 + 10) - (0 + 3 + 5 + 6) - 2 * (1+2+3)
        => A[3]->A[6] - A[0]->A[3] - 2 * (3)(3+1) / 2
        => (B[7] - B[3]) - (B[4] - B[0]) - (k//2)*((k+1)//2)

        """
        A = [i for i, a in enumerate(nums) if a]
        N = len(A)
        prefix = [0] * (N + 1)
        res = float('inf')
        # compute the sum of the absolute difference between each element and the median element of the array
        for i in range(N):
            prefix[i + 1] = prefix[i] + A[i]
            # range_sum[k/2, k - 1] - range_sum[0, (k - 1)/2]
        for i in range(N - k + 1):
            res = min(res, prefix[i + k] - prefix[k // 2 + i] - (prefix[(k + 1) // 2 + i] - prefix[i]))
        res -= (k // 2) * ((k + 1) // 2)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 0, 0, 1, 0, 1], k=2), 1],
    [dict(nums=[1, 0, 0, 0, 0, 0, 1, 1], k=3), 5],
    [dict(nums=[1, 1, 0, 1], k=2), 0],
])
def test_solutions(kw, expected):
    assert Solution().minMoves(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
