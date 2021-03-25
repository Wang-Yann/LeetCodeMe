#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。 
# 
#  在开始时，我们同时把一些多米诺骨牌向左或向右推。 
# 
#  
# 
#  每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。 
# 
#  同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。 
# 
#  如果同时有多米诺骨牌落在一张垂直竖立的多米诺骨牌的两边，由于受力平衡， 该骨牌仍然保持不变。 
# 
#  就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。 
# 
#  给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；如果第 i 张多米诺骨牌被推向右边，则 S[i] = '
# R'；如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。 
# 
#  返回表示最终状态的字符串。 
# 
#  示例 1： 
# 
#  输入：".L.R...LR..L.."
# 输出："LL.RR.LLRRLL.." 
# 
#  示例 2： 
# 
#  输入："RR.L"
# 输出："RR.L"
# 说明：第一张多米诺骨牌没有给第二张施加额外的力。 
# 
#  提示： 
# 
#  
#  0 <= N <= 10^5 
#  表示多米诺骨牌状态的字符串只含有 'L'，'R'; 以及 '.'; 
#  
#  Related Topics 双指针 动态规划

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(-1,"L")]+[(i,x) for i,x in enumerate(dominoes) if x!="."]+[(len(dominoes),"R")]
        ans = list(dominoes)
        for (i,x),(j,y)  in zip(symbols,symbols[1:]):
            if x==y:
                for k in range(i+1,j):
                    ans[k]=x
            #R>L
            elif x>y:
                for k in range(i+1,j):
                    # ans[k] = '.LR'[cmp(k-i, j-k)]
                    if k-i>j-k:
                        ans[k] = "L"
                    elif k-i<j-k:
                        ans[k]="R"
                    else:
                        ans[k]="."
        return  "".join(ans)



        
# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (".L.R...LR..L..", "LL.RR.LLRRLL.." ),
    pytest.param("RR.L", "RR.L"),
])
def test_solutions(args, expected):
    assert Solution().pushDominoes(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

