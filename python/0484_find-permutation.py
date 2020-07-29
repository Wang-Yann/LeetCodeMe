#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 14:27:14
# @Last Modified : 2020-07-29 14:27:14
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 现在给定一个只由字符 'D' 和 'I' 组成的 秘密签名。'D' 表示两个数字间的递减关系，'I' 表示两个数字间的递增关系。并且 秘密签名 是由一个特定
# 的整数数组生成的，该数组唯一地包含 1 到 n 中所有不同的数字（秘密签名的长度加 1 等于 n）。例如，秘密签名 "DI" 可以由数组 [2,1,3] 或 [
# 3,1,2] 生成，但是不能由数组 [3,2,4] 或 [2,1,3,4] 生成，因为它们都不是合法的能代表 "DI" 秘密签名 的特定串。 
# 
#  现在你的任务是找到具有最小字典序的 [1, 2, ... n] 的排列，使其能代表输入的 秘密签名。 
# 
#  示例 1： 
# 
#  输入： "I"
# 输出： [1,2]
# 解释： [1,2] 是唯一合法的可以生成秘密签名 "I" 的特定串，数字 1 和 2 构成递增关系。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入： "DI"
# 输出： [2,1,3]
# 解释： [2,1,3] 和 [3,1,2] 可以生成秘密签名 "DI"，
# 但是由于我们要找字典序最小的排列，因此你需要输出 [2,1,3]。
#  
# 
#  
# 
#  注： 
# 
#  
#  输出字符串只会包含字符 'D' 和 'I'。 
#  输入字符串的长度是一个正整数且不会超过 10,000。 
#  
# 
#  
#  Related Topics 贪心算法 
#  👍 21 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        """
        果出现了连续的 I，我们会顺序填入数；如果出现了 D，我们会逆序填入数。因此我们可以先将所有的数从小到大依次填入，
        组成 [1 .. n] 的排列，随后对于秘密中连续的 D，我们将对应位置的区间进行翻转

        """
        N = len(s)
        res = list(range(1, N + 2))
        i = 1
        while i <= N:
            j = i
            while i <= N and s[i - 1] == "D":
                i += 1
            res[j - 1:i] = res[j - 1:i][::-1]
            i += 1

        return res


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def findPermutation(self, s: str) -> List[int]:
        N = len(s)
        result = []
        for i in range(N + 1):
            if i == N or s[i] == 'I':
                result += range(i + 1, len(result), -1)
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(s="I"), [1, 2]],
    [dict(s="DI"), [2, 1, 3]],
    [dict(s="DDIIDI"), [3, 2, 1, 4, 6, 5, 7]],
])
def test_solutions(kw, expected):
    assert Solution().findPermutation(**kw) == expected
    assert Solution1().findPermutation(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
