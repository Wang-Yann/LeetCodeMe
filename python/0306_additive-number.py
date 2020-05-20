#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 累加数是一个字符串，组成它的数字可以形成累加序列。 
# 
#  一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。 
# 
#  给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。 
# 
#  说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。 
# 
#  示例 1: 
# 
#  输入: "112358"
# 输出: true 
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#  
# 
#  示例 2: 
# 
#  输入: "199100199"
# 输出: true 
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199 
# 
#  进阶: 
# 你如何处理一个溢出的过大的整数输入? 
#  Related Topics 回溯算法

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        """TODO"""
        def add(x, y):
            return str(int(x) + int(y))

        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                s1, s2 = num[0:i], num[i:j]
                if (len(s1) > 1 and s1[0] == '0') or \
                        (len(s2) > 1 and s2[0] == '0'):
                    continue

                expected = add(s1, s2)
                cur = s1 + s2 + expected
                while len(cur) < len(num):
                    s1, s2, expected = s2, expected, add(s2, expected)
                    cur += expected
                if cur == num:
                    return True
        return False


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num)
        for x in range(length // 2):
            if x > 0 and num[0] == "0":
                break
            for y in range(x + 1, length):
                if y - x > 1 and num[x + 1] == "0":
                    break
                i, j, k = 0, x, y
                while k < length:
                    a = int(num[i:j + 1])
                    b = int(num[j + 1:k + 1])
                    add = str(int(a + b))
                    if not num.startswith(add, k + 1):
                        break
                    if len(add) + 1 + k == len(num):
                        return True
                    i = j + 1
                    j = k
                    k += len(add)
        return False


@pytest.mark.parametrize("args,expected", [
    ("112358", True),
    ("199100199", True),
])
def test_solutions(args, expected):
    assert Solution().isAdditiveNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
