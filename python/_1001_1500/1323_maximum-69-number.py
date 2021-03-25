#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 23:16:44
# @Last Modified : 2020-07-06 23:16:44
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个仅由数字 6 和 9 组成的正整数 num。 
# 
#  你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。 
# 
#  请返回你可以得到的最大数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：num = 9669
# 输出：9969
# 解释：
# 改变第一位数字可以得到 6669 。
# 改变第二位数字可以得到 9969 。
# 改变第三位数字可以得到 9699 。
# 改变第四位数字可以得到 9666 。
# 其中最大的数字是 9969 。
#  
# 
#  示例 2： 
# 
#  输入：num = 9996
# 输出：9999
# 解释：将最后一位从 6 变到 9，其结果 9999 是最大的数。 
# 
#  示例 3： 
# 
#  输入：num = 9999
# 输出：9999
# 解释：无需改变就已经是最大的数字了。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num <= 10^4 
#  num 每一位上的数字都是 6 或者 9 。 
#  
#  Related Topics 数学 
#  👍 28 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))



# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def maximum69Number(self, num: int) -> int:
        digits = list(str(num))
        for i, digit in enumerate(digits):
            if digit == "6":
                digits[i] = "9"
                break

        return int("".join(digits))

@pytest.mark.parametrize("kwargs,expected", [
    (dict(num=9669), 9969),
    pytest.param(dict(num=9996), 9999),
    pytest.param(dict(num=9999), 9999),
])
def test_solutions(kwargs, expected):
    assert Solution().maximum69Number(**kwargs) == expected
    assert Solution1().maximum69Number(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
