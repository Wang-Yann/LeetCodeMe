#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”： 
# 
#  
#  B.length >= 3 
#  存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B
# [B.length - 1] 
#  
# 
#  （注意：B 可以是 A 的任意子数组，包括整个数组 A。） 
# 
#  给出一个整数数组 A，返回最长 “山脉” 的长度。 
# 
#  如果不含有 “山脉” 则返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
#  
# 
#  示例 2： 
# 
#  输入：[2,2,2]
# 输出：0
# 解释：不含 “山脉”。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 10000 
#  0 <= A[i] <= 10000 
#  
#  Related Topics 双指针

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestMountain(self, A: List[int]) -> int:
        res, up_len, down_len = 0, 0, 0
        for i in range(1, len(A)):
            if (down_len and A[i - 1] < A[i]) or A[i - 1] == A[i]:
                up_len = down_len = 0
            up_len += A[i - 1] < A[i]
            down_len += A[i - 1] > A[i]
            if up_len and down_len:
                res = max(res, up_len + down_len + 1)
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([2, 1, 4, 7, 3, 2, 5], 5),
    pytest.param([2, 2, 2], 0),
])
def test_solutions(args, expected):
    assert Solution().longestMountain(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
