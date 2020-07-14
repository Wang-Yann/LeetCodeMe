#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 21:08:01
# @Last Modified : 2020-07-14 21:08:01
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。 
# 
#  示例 1： 
# 
#  输入：[1,2,5,9,5,9,5,5,5]
# 输出：5 
# 
#  
# 
#  示例 2： 
# 
#  输入：[3,2]
# 输出：-1 
# 
#  
# 
#  示例 3： 
# 
#  输入：[2,2,1,1,1,2,2]
# 输出：2 
# 
#  
# 
#  说明： 
# 你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？ 
#  Related Topics 位运算 数组 分治算法 
#  👍 22 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        if not nums:
            return -1
        major = None  # 主要元素
        count = 0  # 对抗阶段的权值
        # 对抗阶段
        for i in range(len(nums)):  # O(n)
            if count == 0:  # 权值为0，说明目前没有主要元素，令当前元素为major
                major = nums[i]
                count += 1
            else:
                if nums[i] == major:  # 当前元素与major相同
                    count += 1
                else:
                    count -= 1  # 权重抵消掉
        # 判定阶段
        # 对抗阶段生成的major有可能是前面全部抵消后的剩余的元素，也有可能是真的主要元素
        # 再遍历一遍数组，以确认major元素的个数
        n_major = 0  # 计数
        for v in nums:
            if v == major:
                n_major += 1
            if n_major > len(nums) // 2:
                return major

        return -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([1, 2, 5, 9, 5, 9, 5, 5, 5], 5),
    pytest.param([3, 2], -1),
    pytest.param([2, 2, 1, 1, 1, 2, 2], 2),
])
def test_solutions(args, expected):
    assert Solution().majorityElement(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
