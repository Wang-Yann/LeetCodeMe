#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个未排序的整数数组，找到最长递增子序列的个数。 
# 
#  示例 1: 
# 
#  
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
#  
# 
#  示例 2: 
# 
#  
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#  
# 
#  注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。 
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        假设对于以 nums[i] 结尾的序列，我们知道最长序列的长度 length[i]，以及具有该长度的序列的 count[i]。
        对于每一个 i<j 和一个 A[i]<A[j]，我们可以将一个 A[j] 附加到以 A[i] 结尾的最长子序列上。
        如果这些序列比 length[j] 长，那么我们就知道我们有count[i] 个长度为 length 的序列。
        如果这些序列的长度与 length[j] 相等，那么我们就知道现在有 count[i] 个额外的序列（即 count[j]+=count[i]）
        ---
        初始化：两个数组初始化为全1是有意义的，因为无论如何最长子序列长度至少为1，且通往的方法数至少为1（自身）。
        更新：在更新[i]位置的时候需要判断是否是第一次遇到符合条件的情况


        """
        N = len(nums)
        if N <= 1:
            return N
        lengths = [1] * N
        counter = [1] * N

        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:  # 代表第一次遇到最长子序列
                        lengths[i] = 1 + lengths[j]
                        counter[i] = counter[j]
                    elif lengths[j] + 1 == lengths[i]:  # 代表已经遇到过最长子序列
                        counter[i] = counter[i] + counter[j]
        longest = max(lengths)
        res = sum(counter[i] for i in range(N) if lengths[i] == longest)
        # print(nums, "Counts:{}| Lengths:{}".format(counter, lengths))
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    # ([1, 3, 5, 4, 6, 8, 4, 5, 6, 7], 2),
    ([1, 3, 5, 4, 7], 2),
    # ([2, 2, 2, 2, 2], 5),
    # ([1, 3, 2], 2),

])
def test_solutions(args, expected):
    assert Solution().findNumberOfLIS(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
