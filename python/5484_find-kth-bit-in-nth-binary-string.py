#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 12:32:38
# @Last Modified : 2020-08-09 12:32:38
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个正整数 n 和 k，二进制字符串 Sn 的形成规则如下： 
# 
#  
#  S1 = "0" 
#  当 i > 1 时，Si = Si-1 + "1" + reverse(invert(Si-1)) 
#  
# 
#  其中 + 表示串联操作，reverse(x) 返回反转 x 后得到的字符串，而 invert(x) 则会翻转 x 中的每一位（0 变为 1，而 1 变为 
# 0） 
# 
#  例如，符合上述描述的序列的前 4 个字符串依次是： 
# 
#  
#  S1 = "0" 
#  S2 = "011" 
#  S3 = "0111001" 
#  S4 = "011100110110001" 
#  
# 
#  请你返回 Sn 的 第 k 位字符 ，题目数据保证 k 一定在 Sn 长度范围以内。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 3, k = 1
# 输出："0"
# 解释：S3 为 "0111001"，其第 1 位为 "0" 。
#  
# 
#  示例 2： 
# 
#  输入：n = 4, k = 11
# 输出："1"
# 解释：S4 为 "011100110110001"，其第 11 位为 "1" 。
#  
# 
#  示例 3： 
# 
#  输入：n = 1, k = 1
# 输出："0"
#  
# 
#  示例 4： 
# 
#  输入：n = 2, k = 3
# 输出："1"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= 2n - 1 
#  
#  Related Topics 字符串 
#  👍 0 👎 0
	 

"""

import pytest,traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode,ListNode
from sample_datas import BIG_CASE





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        hash_map = {"0": "1", "1": "0"}
        s = ["0"]
        for i in range(n - 1):
            rs = [hash_map[b] for b in s][::-1]
            s = s + ["1"] + rs
        # print(s)
        return s[k - 1]

# leetcode submit region end(Prohibit modification and deletion)




# @pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=3, k=1), "0"],
    pytest.param(dict(n=4, k=11), "1"),
    pytest.param(dict(n=1, k=1), "0"),
    pytest.param(dict(n=2, k=3), "1"),
])
def test_solutions2(kwargs, expected):
    assert Solution().findKthBit(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])