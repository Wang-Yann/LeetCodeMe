#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。 
# 
#  给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始） 
# 
#  
# 例子: 
# 
#  输入: N = 1, K = 1
# 输出: 0
# 
# 输入: N = 2, K = 1
# 输出: 0
# 
# 输入: N = 2, K = 2
# 输出: 1
# 
# 输入: N = 4, K = 5
# 输出: 1
# 
# 解释:
# 第一行: 0
# 第二行: 01
# 第三行: 0110
# 第四行: 01101001
#  
# 
#  
# 注意： 
# 
#  
#  N 的范围 [1, 30]. 
#  K 的范围 [1, 2^(N-1)]. 
#  
#  Related Topics 递归

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def kthGrammar(self, N: int, K: int) -> int:
        """
        总结出规律，第 K 个数字是上一行第 (K+1) / 2 个数字生成的。如果上一行的数字为 0，被生成的数字为 1 - (K%2)，如果上一行的数字为 1，被生成的数字为 K%2

        """
        if N == 1:
            return 0
        return (1 - K % 2) ^ self.kthGrammar(N - 1, (K + 1) // 2)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def kthGrammar(self, N: int, K: int) -> int:
        """
        #求解K-1二进制中1 的个数为奇数还是偶数
         row 1: 0 row 2: 01 row 3: 0110 row 4: 01101001 进行观察，对于每行第K个字符，
         如果K-1的二进制表示中有奇数个1时，返回1，如果有偶数个，返回0。

        """
        return bin(K - 1).count('1') % 2


@pytest.mark.parametrize("kwargs,expected", [
    (dict(N=1, K=1), 0),
    (dict(N=2, K=1), 0),
    (dict(N=2, K=2), 1),
    pytest.param(dict(N=4, K=5), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().kthGrammar(**kwargs) == expected
    assert Solution1().kthGrammar(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
