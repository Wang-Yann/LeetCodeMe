#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i
# +1]×…×A[n-1]。不能使用除法。 
# 
#  
# 
#  示例: 
# 
#  输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24] 
# 
#  
# 
#  提示： 
# 
#  
#  所有元素乘积之和不会溢出 32 位整数 
#  a.length <= 100000 
#  
# 

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]
        # print(b)
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp
        return b


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
])
def test_solutions(args, expected):
    assert Solution().constructArr(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
