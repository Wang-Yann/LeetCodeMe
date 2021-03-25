#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-07 23:09:51
# @Last Modified : 2020-07-07 23:09:51
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 房间中有 n 枚灯泡，编号从 1 到 n，自左向右排成一排。最初，所有的灯都是关着的。 
# 
#  在 k 时刻（ k 的取值范围是 0 到 n - 1），我们打开 light[k] 这个灯。 
# 
#  灯的颜色要想 变成蓝色 就必须同时满足下面两个条件： 
# 
#  
#  灯处于打开状态。 
#  排在它之前（左侧）的所有灯也都处于打开状态。 
#  
# 
#  请返回能够让 所有开着的 灯都 变成蓝色 的时刻 数目 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：light = [2,1,3,5,4]
# 输出：3
# 解释：所有开着的灯都变蓝的时刻分别是 1，2 和 4 。
#  
# 
#  示例 2： 
# 
#  输入：light = [3,2,4,1,5]
# 输出：2
# 解释：所有开着的灯都变蓝的时刻分别是 3 和 4（index-0）。
#  
# 
#  示例 3： 
# 
#  输入：light = [4,1,2,3]
# 输出：1
# 解释：所有开着的灯都变蓝的时刻是 3（index-0）。
# 第 4 个灯在时刻 3 变蓝。
#  
# 
#  示例 4： 
# 
#  输入：light = [2,1,4,3,6,5]
# 输出：3
#  
# 
#  示例 5： 
# 
#  输入：light = [1,2,3,4,5,6]
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == light.length 
#  1 <= n <= 5 * 10^4 
#  light 是 [1, 2, ..., n] 的一个排列。 
#  
#  Related Topics 数组 
#  👍 20 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:

        """
        Iterate the input light A,
        update right = max(right, A[i]).

        Now we have lighted up i + 1 bulbs,
        if right == i + 1,
        it means that all the previous bulbs (to the left) are turned on too.
        Then we increment res
        """
        right = res = 0
        for i, num in enumerate(light,1):
            right = max(right, num)
            res += right == i
            # print(right,res,"|",i,num)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(light=[2, 1, 3, 5, 4]), 3),
    pytest.param(dict(light=[3, 2, 4, 1, 5]), 2),
    pytest.param(dict(light=[4, 1, 2, 3]), 1),
    pytest.param(dict(light=[2, 1, 4, 3, 6, 5]), 3),
    pytest.param(dict(light=[1, 2, 3, 4, 5, 6]), 6),
])
def test_solutions(kwargs, expected):
    assert Solution().numTimesAllBlue(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
