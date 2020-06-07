#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i
# ]]], ... }且遵守以下的规则。 
# 
#  假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元
# 素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: A = [5,4,0,3,1,6,2]
# 输出: 4
# 解释: 
# A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
# 
# 其中一种最长的 S[K]:
# S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
#  
# 
#  
# 
#  提示： 
# 
#  
#  N是[1, 20,000]之间的整数。 
#  A中不含有重复的元素。 
#  A中的元素大小在[0, N-1]之间。 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def arrayNesting(self, nums: List[int]) -> int:
        """
        按照题意遍历整个数组，每找到一个数字将其标记为已访问过。 最后的答案为每次遍历的长度最大值。

        """
        ans, step, n = 0, 0, len(nums)
        seen = [False] * n
        for i in range(n):
            while not seen[i]:
                seen[i] = True
                i = nums[i]
                step += 1
            ans = max(ans, step)
            step = 0
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([5, 4, 0, 3, 1, 6, 2], 4),
])
def test_solutions(args, expected):
    assert Solution().arrayNesting(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
