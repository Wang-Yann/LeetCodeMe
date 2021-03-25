#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 10:51:05
# @Last Modified : 2021-02-25 10:51:05
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个长度为 偶数 n 的整数数组 nums 和一个整数 limit 。每一次操作，你可以将 nums 中的任何整数替换为 1 到 limit 之间的另一
# 个整数。 
# 
#  如果对于所有下标 i（下标从 0 开始），nums[i] + nums[n - 1 - i] 都等于同一个数，则数组 nums 是 互补的 。例如，数组 
# [1,2,3,4] 是互补的，因为对于所有下标 i ，nums[i] + nums[n - 1 - i] = 5 。 
# 
#  返回使数组 互补 的 最少 操作次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,4,3], limit = 4
# 输出：1
# 解释：经过 1 次操作，你可以将数组 nums 变成 [1,2,2,3]（加粗元素是变更的数字）：
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# 对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,2,1], limit = 2
# 输出：2
# 解释：经过 2 次操作，你可以将数组 nums 变成 [2,2,2,2] 。你不能将任何数字变更为 3 ，因为 3 > limit 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,2,1,2], limit = 2
# 输出：0
# 解释：nums 已经是互补的。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  2 <= n <= 105 
#  1 <= nums[i] <= limit <= 105 
#  n 是偶数。 
#  
#  Related Topics 贪心算法 
#  👍 39 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
       https://leetcode-cn.com/problems/minimum-moves-to-make-array-complementary/solution/chai-fen-sao-miao-by-lucifer1004/
       差分数组
        HARD  TODO
        """
        N = len(nums)
        # 差分数组 d，范围是 [1, 2*limit+1]
        delta = [0] * (limit * 2 + 2)
        for i in range(N // 2):
            low = 1 + min(nums[i], nums[N - i - 1])
            high = limit + max(nums[i], nums[N - i - 1])
            sum_val = nums[i] + nums[N - i - 1]
            # 对差分数组进行操作
            delta[low] -= 1
            delta[sum_val] -= 1
            delta[sum_val + 1] += 1
            delta[high + 1] += 1

        ans = now = N
        for i in range(2, limit * 2 + 1):
            now += delta[i]
            ans = min(ans, now)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 4, 3], limit=4), 1],
    [dict(nums=[1, 2, 2, 1], limit=2), 2],
    [dict(nums=[1, 2, 1, 2], limit=2), 0],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().minMoves(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
