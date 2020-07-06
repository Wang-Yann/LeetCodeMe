#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个以行程长度编码压缩的整数列表 nums 。 
# 
#  考虑每对相邻的两个元素 [freq, val] = [nums[2*i], nums[2*i+1]] （其中 i >= 0 ），每一对都表示解压后子列表中
# 有 freq 个值为 val 的元素，你需要从左到右连接所有子列表以生成解压后的列表。 
# 
#  请你返回解压后的列表。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [1,2,3,4]
# 输出：[2,4,4,4]
# 解释：第一对 [1,2] 代表着 2 的出现频次为 1，所以生成数组 [2]。
# 第二对 [3,4] 代表着 4 的出现频次为 3，所以生成数组 [4,4,4]。
# 最后将它们串联到一起 [2] + [4,4,4] = [2,4,4,4]。 
# 
#  示例 2： 
# 
#  输入：nums = [1,1,2,3]
# 输出：[1,3,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 100 
#  nums.length % 2 == 0 
#  1 <= nums[i] <= 100 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        N = len(nums)
        for i in range(1, N,2):
            cnt, num = nums[i - 1], nums[i]
            ans.extend([num] * cnt)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 3, 4]), [2, 4, 4, 4]],
])
def test_solutions(kw, expected):
    assert Solution().decompressRLElist(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
