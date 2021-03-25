#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 写一个程序，输出从 1 到 n 数字的字符串表示。 
# 
#  1. 如果 n 是3的倍数，输出“Fizz”； 
# 
#  2. 如果 n 是5的倍数，输出“Buzz”； 
# 
#  3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。 
# 
#  示例： 
# 
#  n = 15,
# 
# 返回:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
#  
# 

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def fizzBuzz(self, n: int) -> List[str]:
        if n<=0:
            return []
        ans =[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans

    def fizzBuzz1(self, n: int) -> List[str]:
        l = [str(x) for x in range(n + 1)]
        l3 = range(0, n + 1, 3)
        l5 = range(0, n + 1, 5)
        for i in l3:
            l[i] = 'Fizz'
        for i in l5:
            if l[i] == 'Fizz':
                l[i] += 'Buzz'
            else:
                l[i] = 'Buzz'
        return l[1:]



# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (15,
     [
         "1",
         "2",
         "Fizz",
         "4",
         "Buzz",
         "Fizz",
         "7",
         "8",
         "Fizz",
         "Buzz",
         "11",
         "Fizz",
         "13",
         "14",
         "FizzBuzz"
     ]),
])
def test_solutions(args, expected):
    assert Solution().fizzBuzz(args) == expected
    assert Solution().fizzBuzz1(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
