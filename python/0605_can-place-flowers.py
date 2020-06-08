#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。 
# 
#  给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True
# ，不能则返回False。 
# 
#  示例 1: 
# 
#  
# 输入: flowerbed = [1,0,0,0,1], n = 1
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: flowerbed = [1,0,0,0,1], n = 2
# 输出: False
#  
# 
#  注意: 
# 
#  
#  数组内已种好的花不会违反种植规则。 
#  输入的数组长度范围为 [1, 20000]。 
#  n 是非负整数，且不会超过输入数组的大小。 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and \
                    (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        length = len(flowerbed)
        if flowerbed.count(0) < n:
            return False
        i = 0
        while i < length:
            if flowerbed[i] == 1:
                i += 2
            else:
                if (i > 0 and flowerbed[i - 1] == 1) \
                        or (i + 1 < length and flowerbed[i + 1] == 1):
                    i += 1
                else:
                    cnt += 1
                    flowerbed[i] = 1
                    i += 2

        # print(cnt, flowerbed)
        return cnt >= n


@pytest.mark.parametrize("kw,expected", [
    [dict(flowerbed=[1, 0, 0, 0, 1], n=1), True],
    [dict(flowerbed=[1, 0, 0, 0, 1], n=2), False],
])
def test_solutions(kw, expected):
    assert Solution().canPlaceFlowers(**kw) == expected
    assert Solution1().canPlaceFlowers(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
