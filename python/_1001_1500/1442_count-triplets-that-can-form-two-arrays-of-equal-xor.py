#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-09 23:21:14
# @Last Modified : 2020-07-09 23:21:14
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一个整数数组 arr 。 
# 
#  现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。 
# 
#  a 和 b 定义如下： 
# 
#  
#  a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] 
#  b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k] 
#  
# 
#  注意：^ 表示 按位异或 操作。 
# 
#  请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [2,3,1,6,7]
# 输出：4
# 解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,1,1,1,1]
# 输出：10
#  
# 
#  示例 3： 
# 
#  输入：arr = [2,3]
# 输出：0
#  
# 
#  示例 4： 
# 
#  输入：arr = [1,3,5,7,9]
# 输出：3
#  
# 
#  示例 5： 
# 
#  输入：arr = [7,11,12,9,5,2,7,17,22]
# 输出：8
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 300 
#  1 <= arr[i] <= 10^8 
#  
#  Related Topics 位运算 数组 数学 
#  👍 23 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        """
        Because we once we determine the pair (i,k),
j can be any number that i < j <= k,
so we need to plus k - i - 1 to the result res
        """
        arr.insert(0, 0)
        N = len(arr)
        for i in range(N - 1):
            arr[i + 1] ^= arr[i]
        res = 0
        for i in range(N):
            for j in range(i + 1, N):
                if arr[i] == arr[j]:
                    res += j - i - 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(arr=[2, 3, 1, 6, 7]), 4],
    [dict(arr=[1, 1, 1, 1, 1]), 10],
    [dict(arr=[2, 3]), 0],
    [dict(arr=[1, 3, 5, 7, 9]), 3],
    [dict(arr=[7, 11, 12, 9, 5, 2, 7, 17, 22]), 8],

])
def test_solutions(kwargs, expected):
    assert Solution().countTriplets(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
