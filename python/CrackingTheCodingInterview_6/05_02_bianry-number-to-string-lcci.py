#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 23:37:09
# @Last Modified : 2020-07-12 23:37:09
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字不在0和1之间，或者无法精确地用32位以内
# 的二进制表示，则打印“ERROR”。 
# 
#  示例1: 
# 
#   输入：0.625
#  输出："0.101"
#  
# 
#  示例2: 
# 
#   输入：0.1
#  输出："ERROR"
#  提示：0.1无法被二进制准确表示
#  
# 
#  提示： 
# 
#  
#  32位包括输出中的"0."这两位。 
#  
#  Related Topics 字符串 
#  👍 8 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def printBin(self, num: float) -> str:
        res = "0."
        i = 30
        while num > 0 and i:
            num *= 2
            if num >= 1:
                res += "1"
                num -= 1
            else:
                res += "0"
            i -= 1
        return res if not num else "ERROR"


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            0.625
            , "0.101"),
    pytest.param(0.1, "ERROR"),
])
def test_solutions(args, expected):
    assert Solution().printBin(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
