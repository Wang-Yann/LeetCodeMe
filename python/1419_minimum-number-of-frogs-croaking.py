#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croak
# OfFrogs 中会混合多个 “croak” 。请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。 
# 
#  注意：要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它
# 就不会发出声音。 
# 
#  如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：croakOfFrogs = "croakcroak"
# 输出：1 
# 解释：一只青蛙 “呱呱” 两次
#  
# 
#  示例 2： 
# 
#  
# 输入：croakOfFrogs = "crcoakroak"
# 输出：2 
# 解释：最少需要两只青蛙，“呱呱” 声用黑体标注
# 第一只青蛙 "crcoakroak"
# 第二只青蛙 "crcoakroak"
#  
# 
#  示例 3： 
# 
#  
# 输入：croakOfFrogs = "croakcrook"
# 输出：-1
# 解释：给出的字符串不是 "croak" 的有效组合。
#  
# 
#  示例 4： 
# 
#  
# 输入：croakOfFrogs = "croakcroa"
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= croakOfFrogs.length <= 10^5 
#  字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k' 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """
        GOOD
        1、有多少只青蛙在叫==最多有多少个同时存在的字符c；
        2、对字母c、r、o、a、k计数，必须保持任意时刻（c>=r>=o>=a>=k）,才是正确的；
            否则就是错误的，返回-1；
        3、在遇到一个k前，要判断当前有多少个c，是否比曾经出现的最多的多，然后才利用出现的k对所有字符进行-1操作；
        4、遍历完字符串后，如果任意字母有剩，也是错误的。
          watermark is the the number of required Frogs (making sound simultaneously) we have seen so far. It is calculated based on the difference between number of encountered "c" (a Frog starts croaking by uttering "c") and "k" (by encountering which, a croaking frog is released and returned to the pool of frogs being ready to be used for the next croaking). let's put it another way: As soon as a Frog starts croaking, it will be busy croaking until a "k" is encountered, that's why maximum of busy Frogs seen in every step will be watermark.
        """
        watermark = c = r = o = a = k = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
                watermark = max(watermark, c - k)
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            else:
                k += 1
            if not c >= r >= o >= a >= k:
                return -1
        return watermark if c == k else -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(croakOfFrogs="croakcroak"), 1],
    [dict(croakOfFrogs="crcoakroak"), 2],
    [dict(croakOfFrogs="croakcrook"), -1],
    [dict(croakOfFrogs="croakcroa"), -1],
])
def test_solutions(kw, expected):
    assert Solution().minNumberOfFrogs(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
