#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 你想要用小写字母组成一个目标字符串 target。 
# 
#  开始的时候，序列由 target.length 个 '?' 记号组成。而你有一个小写字母印章 stamp。 
# 
#  在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行 10 * target.length 个回合。 
# 
#  举个例子，如果初始序列为 "?????"，而你的印章 stamp 是 "abc"，那么在第一回合，你可以得到 "abc??"、"?abc?"、"??abc
# "。（请注意，印章必须完全包含在序列的边界内才能盖下去。） 
# 
#  如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。 
# 
#  例如，如果序列是 "ababc"，印章是 "abc"，那么我们就可以返回与操作 "?????" -> "abc??" -> "ababc" 相对应的答案 
# [0, 2]； 
# 
#  另外，如果可以印出序列，那么需要保证可以在 10 * target.length 个回合内完成。任何超过此数字的答案将不被接受。 
# 
#  
# 
#  示例 1： 
# 
#  输入：stamp = "abc", target = "ababc"
# 输出：[0,2]
# （[1,0,2] 以及其他一些可能的结果也将作为答案被接受）
#  
# 
#  示例 2： 
# 
#  输入：stamp = "abca", target = "aabcaca"
# 输出：[3,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= stamp.length <= target.length <= 1000 
#  stamp 和 target 只包含小写字母。 
#  
#  Related Topics 贪心算法 字符串

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """
        9 Zhang
        我先找到最后一次章盖的位置，即在target序列中找stamp，记下盖的序列的最左边位置，然后把相应位置全部替换为‘?’，相当于就是例2中的 "a????ca"，
        然后把这个？看成一个万能的字母，它可以为任意的，再找stamp，这样，一直到最后全部变成target，这些序列就是从最后一次到第一次盖章的位置，
        """
        stamp = list(stamp)
        target = list(target)
        NS = len(stamp)
        NT = len(target)

        right = NT
        res = []
        flag = True  # if nothing is changed during one loop, then finish the while loop
        while right > 0 and flag:
            flag = False
            for i in range(NT - NS + 1):
                if right == 0:  # 当左端位置到达起始位置，结束退出。
                    break

                if all([target[i + j] == '?' for j in range(NS)]):  # 均为?不做处理
                    continue

                if all([stamp[j] == target[i + j] or target[i + j] == '?' for j in range(NS)]):  # 字母和?一起时，继续替换操作
                    flag = True
                    res.insert(0, i)  # 头部插入下标，最终结果逆序。
                    for j in range(NS):
                        if stamp[j] == target[i + j]:
                            target[i + j] = '?'  # 使用?替换
                            right -= 1
        # print(stamp,target)
        return res if right == 0 else []


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(stamp="abc", target="ababc"), ([0, 2], [1, 0, 2])),
    pytest.param(dict(stamp="abca", target="aabcaca"), ([2, 3, 0, 1], [0, 3, 1])),
])
def test_solutions(kwargs, expected):
    assert Solution().movesToStamp(**kwargs) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
