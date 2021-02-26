#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 07:48:34
# @Last Modified : 2021-02-26 07:48:34
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个二进制字符串 binary ，它仅有 0 或者 1 组成。你可以使用下面的操作任意次对它进行修改： 
# 
#  
#  操作 1 ：如果二进制串包含子字符串 "00" ，你可以用 "10" 将其替换。
# 
#  
#  比方说， "00010" -> "10010" 
#  
#  
#  操作 2 ：如果二进制串包含子字符串 "10" ，你可以用 "01" 将其替换。
#  
#  比方说， "00010" -> "00001" 
#  
#  
#  
# 
#  请你返回执行上述操作任意次以后能得到的 最大二进制字符串 。如果二进制字符串 x 对应的十进制数字大于二进制字符串 y 对应的十进制数字，那么我们称二进制
# 字符串 x 大于二进制字符串 y 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：binary = "000110"
# 输出："111011"
# 解释：一个可行的转换为：
# "000110" -> "000101" 
# "000101" -> "100101" 
# "100101" -> "110101" 
# "110101" -> "110011" 
# "110011" -> "111011"
#  
# 
#  示例 2： 
# 
#  
# 输入：binary = "01"
# 输出："01"
# 解释："01" 没办法进行任何转换。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= binary.length <= 105 
#  binary 仅包含 '0' 和 '1' 。 
#  
#  Related Topics 贪心算法 
#  👍 9 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        """
        for rest part, we can always use "10" -> "01" to put all ones to the end of the string and hence move all zeros ahead of these ones;
        for all the zeros, apply "00" -> "10" from left to right, till only one "0" remaining, it is the maximum.
        """
        leading_ones = binary.find('0')
        if leading_ones < 0:
            return binary
        N = len(binary)
        zeros = binary.count('0')
        rest_ones = N - leading_ones - zeros
        return '1' * (leading_ones + zeros - 1) + '0' + '1' * rest_ones


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(binary="000110"), "111011"],
    [dict(binary="01"), "01"],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maximumBinaryString(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
