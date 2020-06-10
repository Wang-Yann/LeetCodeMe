#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。 
# 
#  （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。） 
# 
#  示例 1: 
# 
#  输入: N = 10
# 输出: 9
#  
# 
#  示例 2: 
# 
#  输入: N = 1234
# 输出: 1234
#  
# 
#  示例 3: 
# 
#  输入: N = 332
# 输出: 299
#  
# 
#  说明: N 是在 [0, 10^9] 范围内的一个整数。 
#  Related Topics 贪心算法

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """ 贪心　
        对于 N 的每一位数字，我们构建答案 ans 的下一位数字。我们找到数字 d，其中 d 满足 ans + (d repeating) > N（按字符串比较）
        且 d-1 满足 ans + (d-1 repeating) <= N，因此我们将 d-1 添加到我们的答案中。如果找不到这样一个数字 d，则在答案中添加 9。

        """
        digits = []
        A = list(int(x) for x in str(N))
        for i in range(len(A)):
            for digit in range(1, 10):
                if digits + [digit] * (len(A) - i) > A:
                    digits.append(digit - 1)
                    break
            else:
                digits.append(9)
        # print(digits)
        return int("".join(map(str, digits)))


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (10, 9),
    (1234, 1234),
    (332, 299),
    (100, 99),
])
def test_solutions(args, expected):
    assert Solution().monotoneIncreasingDigits(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
