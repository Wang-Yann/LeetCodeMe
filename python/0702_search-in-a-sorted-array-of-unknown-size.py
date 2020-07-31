#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 11:50:25
# @Last Modified : 2020-07-31 11:50:25
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个升序整数数组，写一个函数搜索 nums 中数字 target。如果 target 存在，返回它的下标，否则返回 -1。注意，这个数组的大小是未知的。
# 你只可以通过 ArrayReader 接口访问这个数组，ArrayReader.get(k) 返回数组中第 k 个元素（下标从 0 开始）。 
# 
#  你可以认为数组中所有的整数都小于 10000。如果你访问数组越界，ArrayReader.get 会返回 2147483647。 
# 
#  
# 
#  样例 1： 
# 
#  输入: array = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 存在在 nums 中，下标为 4
#  
# 
#  样例 2： 
# 
#  输入: array = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不在数组中所以返回 -1 
# 
#  
# 
#  注释 ： 
# 
#  
#  你可以认为数组中所有元素的值互不相同。 
#  数组元素的值域是 [-9999, 9999]。 
#  
#  Related Topics 二分查找 
#  👍 11 👎 0

"""

import pytest


class ArrayReader:
    def get(self, index: int) -> int:
        if not 0 <= index <= len(array) - 1:
            return 2147483647
        return array[index]


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l, r = 0, 0x7fffffff
        while l <= r:
            mid = l + (r - l) // 2
            if reader.get(mid) > target:
                r = mid - 1
            elif reader.get(mid) < target:
                l = mid + 1
            else:
                return mid
        return -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(array=[-1, 0, 3, 5, 9, 12], target=9), 4],
    [dict(array=[-1, 0, 3, 5, 9, 12], target=2), -1],
])
def test_solutions(kw, expected):
    global array
    array = kw["array"]
    reader = ArrayReader()
    assert Solution().search(reader, kw["target"]) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
