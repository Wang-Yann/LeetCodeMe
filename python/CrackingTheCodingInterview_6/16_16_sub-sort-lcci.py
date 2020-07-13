#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 17:51:54
# @Last Modified : 2020-07-13 17:51:54
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短
# 序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。 
#  示例： 
#  输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
# 输出： [3,9]
#  
#  提示： 
#  
#  0 <= len(array) <= 1000000 
#  
#  Related Topics 排序 数组 
#  👍 25 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        N = len(array)
        maxx, minn = -10000000, 10000000
        l, r = -1, -1
        for i in range(N):
            if array[i] < maxx:
                r = i
            else:
                maxx = array[i]
        for i in range(N - 1, -1, -1):
            if array[i] > minn:
                l = i
            else:
                minn = array[i]
        return [l, r]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19], [3, 9])
])
def test_solutions(args, expected):
    assert Solution().subSort(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
