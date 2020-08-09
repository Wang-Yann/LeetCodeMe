#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 14:49:08
# @Last Modified : 2020-08-09 14:49:08
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。 
# 
#  如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。 
# 
#  
#  0 <= i < j < k < arr.length 
#  |arr[i] - arr[j]| <= a 
#  |arr[j] - arr[k]| <= b 
#  |arr[i] - arr[k]| <= c 
#  
# 
#  其中 |x| 表示 x 的绝对值。 
# 
#  返回 好三元组的数量 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# 输出：4
# 解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# 输出：0
# 解释：不存在满足所有条件的三元组。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= arr.length <= 100 
#  0 <= arr[i] <= 1000 
#  0 <= a, b, c <= 1000 
#  
#  Related Topics 数组 
#  👍 0 👎 0
	 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        ans = 0
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, N):
                    if abs(arr[j] - arr[k]) > b or abs(arr[k] - arr[i]) > c:
                        continue
                    else:
                        ans += 1
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3), 4],

    pytest.param(dict(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1), 0),
    pytest.param(dict(arr=[7, 3, 7, 3, 12, 1, 12, 2, 3], a=5, b=8, c=1), 12),
])
def test_solutions(kwargs, expected):
    assert Solution().countGoodTriplets(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
