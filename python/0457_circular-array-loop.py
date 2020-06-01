#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个含有正整数和负整数的环形数组 nums。 如果某个索引中的数 k 为正数，则向前移动 k 个索引。相反，如果是负数 (-k)，则向后移动 k 个索引
# 。因为数组是环形的，所以可以假设最后一个元素的下一个元素是第一个元素，而第一个元素的前一个元素是最后一个元素。 
# 
#  确定 nums 中是否存在循环（或周期）。循环必须在相同的索引处开始和结束并且循环长度 > 1。此外，一个循环中的所有运动都必须沿着同一方向进行。换句话说
# ，一个循环中不能同时包括向前的运动和向后的运动。 
#  
# 
#  示例 1： 
# 
#  输入：[2,-1,1,2,2]
# 输出：true
# 解释：存在循环，按索引 0 -> 2 -> 3 -> 0 。循环长度为 3 。
#  
# 
#  示例 2： 
# 
#  输入：[-1,2]
# 输出：false
# 解释：按索引 1 -> 1 -> 1 ... 的运动无法构成循环，因为循环的长度为 1 。根据定义，循环的长度必须大于 1 。
#  
# 
#  示例 3: 
# 
#  输入：[-2,1,-1,-2,-2]
# 输出：false
# 解释：按索引 1 -> 2 -> 1 -> ... 的运动无法构成循环，因为按索引 1 -> 2 的运动是向前的运动，而按索引 2 -> 1 的运动是向后的
# 运动。一个循环中的所有运动都必须沿着同一方向进行。 
# 
#  
# 
#  提示： 
# 
#  
#  -1000 ≤ nums[i] ≤ 1000 
#  nums[i] ≠ 0 
#  0 ≤ nums.length ≤ 5000 
#  
# 
#  
# 
#  进阶： 
# 
#  你能写出时间时间复杂度为 O(n) 和额外空间复杂度为 O(1) 的算法吗？ 
#  Related Topics 数组 双指针

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        https://leetcode-cn.com/problems/circular-array-loop/solution/c-xun-huan-wen-ti-jiu-yong-kuai-man-zhi-zhen-by-fu/
        """

        def get_index(idx):
            return (idx + nums[idx]) % len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            slow, fast = i, get_index(i)
            while nums[fast] * nums[i] > 0 \
                    and nums[get_index(fast)] * nums[i] > 0:
                if slow == fast:
                    if slow == get_index(slow):
                        break
                    return True
                slow = get_index(slow)
                fast = get_index(get_index(fast))
            slow = i
            # //当 while 循环退出后，我们需要标记已经走过的结点，从而提高运算效率，方法就是将慢指针重置为i，再用一个 while 循环，条件是 nums[i] 和 慢指针指的数正负相同
            while nums[slow] * nums[i] > 0:
                # //然后计算下一个位置，并且 nums[slow] 标记为0，并且慢指针移动到 next 位置。
                nex = get_index(slow)
                nums[slow] = 0
                slow = nex
        return False


# leetcode submit region end(Prohibit modification and deletion)



@pytest.mark.parametrize("args,expected", [
    ([2, -1, 1, 2, 2], True),
    ([-2, 1, -1, -2, -2], False),
    pytest.param([-1, 2], False),
])
def test_solutions(args, expected):
    assert Solution().circularArrayLoop(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
