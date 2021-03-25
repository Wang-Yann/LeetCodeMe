#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 13:48:09
# @Last Modified : 2020-08-04 13:48:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 本题我们会将数字旋转 180° 来生成一个新的数字。 
# 
#  比如 0、1、6、8、9 旋转 180° 以后，我们得到的新数字分别为 0、1、9、8、6。 
# 
#  2、3、4、5、7 旋转 180° 后，是 无法 得到任何数字的。 
# 
#  易混淆数（Confusing Number）指的是一个数字在整体旋转 180° 以后，能够得到一个和原来 不同 的数，且新数字的每一位都应该是有效的。（请
# 注意，旋转后得到的新数字可能大于原数字） 
# 
#  给出正整数 N，请你返回 1 到 N 之间易混淆数字的数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：20
# 输出：6
# 解释：
# 易混淆数为 [6,9,10,16,18,19]。
# 6 转换为 9
# 9 转换为 6
# 10 转换为 01 也就是 1
# 16 转换为 91
# 18 转换为 81
# 19 转换为 61
#  
# 
#  示例 2： 
# 
#  输入：100
# 输出：19
# 解释：
# 易混淆数为 [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 10^9 
#  
#  Related Topics 数学 回溯算法 
#  👍 10 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def confusingNumberII(self, N: int) -> int:
        """枚举"""
        lookup = {"0": "0", "1": "1", "9": "6", "8": "8", "6": "9"}
        self.count = 0

        def get_rotated(num):
            return int("".join(lookup[x] for x in reversed(str(num))))

        def search(cur):
            if cur > N:
                return
            if cur != get_rotated(cur):
                self.count += 1
            if cur > 0:
                search(cur * 10)
            search(cur * 10 + 1)
            search(cur * 10 + 6)
            search(cur * 10 + 8)
            search(cur * 10 + 9)

        search(0)
        return self.count


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (20, 6),
    (100, 19),
    (1000000000, 1950627),
])
def test_solutions(args, expected):
    assert Solution().confusingNumberII(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
