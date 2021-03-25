#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。 
# 
#  注意：请不要在超过该数组长度的位置写入元素。 
# 
#  要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,0,2,3,0,4,5,0]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
#  
# 
#  示例 2： 
# 
#  输入：[1,2,3]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10000 
#  0 <= arr[i] <= 9 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        i = 0
        while i < N:
            if arr[i] == 0:
                for j in range(N - 1, i, -1):
                    arr[j] = arr[j - 1]
                i += 2
            else:
                i += 1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
    # ([1, 2, 3], [1, 2, 3]),
])
def test_solutions(args, expected):
    Solution().duplicateZeros(args)
    assert args == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
