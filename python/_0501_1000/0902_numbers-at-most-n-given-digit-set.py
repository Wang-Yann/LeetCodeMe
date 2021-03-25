#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们有一组排序的数字 D，它是 {'1','2','3','4','5','6','7','8','9'} 的非空子集。（请注意，'0' 不包括在内。） 
# 
#  现在，我们用这些数字进行组合写数字，想用多少次就用多少次。例如 D = {'1','3','5'}，我们可以写出像 '13', '551', '13513
# 15' 这样的数字。 
# 
#  返回可以用 D 中的数字写出的小于或等于 N 的正整数的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：D = ["1","3","5","7"], N = 100
# 输出：20
# 解释：
# 可写出的 20 个数字是：
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
#  
# 
#  示例 2： 
# 
#  输入：D = ["1","4","9"], N = 1000000000
# 输出：29523
# 解释：
# 我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
# 81 个四位数字，243 个五位数字，729 个六位数字，
# 2187 个七位数字，6561 个八位数字和 19683 个九位数字。
# 总共，可以使用D中的数字写出 29523 个整数。 
# 
#  
# 
#  提示： 
# 
#  
#  D 是按排序顺序的数字 '1'-'9' 的子集。 
#  1 <= N <= 10^9 
#  
#  Related Topics 数学 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        """
        小于N位数的数字直接计算，等于N位数的数组从前向后依次计算

        举例
        D=["1","2","3","4","7","8","9"]
        N=32901345

        看第一位 3
        D中有3,2,1可以取
        先计算第一位为2或1时
        再计算第一位为3时，这时需要看下一位（若D中不存在与3相等的，则直接返回即可，不需要再看下一位了）
        重复上面
        直到第四位
       https://leetcode-cn.com/problems/numbers-at-most-n-given-digit-set/solution/902-zui-da-wei-n-de-shu-zi-zu-he-by-shi-jie-na-you/

        """
        str_N = str(N)
        set_D = set(D)
        res = sum(len(D) ** i for i in range(1, len(str_N)))
        # print("begin", res)
        i = 0
        while i < len(str_N):
            res += sum(c < str_N[i] for c in D) * (len(D)) ** (len(str_N) - i - 1)
            # print(i, str_N[i], len(str_N) - i - 1, res)
            if str_N[i] not in set_D:
                break
            i += 1
        return res + int(i == len(str_N))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(D=["1", "3", "5", "7"], N=100), 20),
    (dict(D=["1", "3", "5", "7"], N=1660), 132),
    pytest.param(dict( D = ["1","4","9"], N = 1000000000  ), 29523),
])
def test_solutions(kwargs, expected):
    assert Solution().atMostNGivenDigitSet(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
