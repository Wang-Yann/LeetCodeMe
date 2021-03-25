#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个数组 A，我们可以将它按一个非负整数 K 进行轮调，这样可以使数组变为 A[K], A[K+1], A{K+2], ... A[A.length -
#  1], A[0], A[1], ..., A[K-1] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。 
# 
#  例如，如果数组为 [2, 4, 1, 3, 0]，我们按 K = 2 进行轮调后，它将变成 [1, 3, 0, 2, 4]。这将记作 3 分，因为 1 >
#  0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 
# 4 [one point]。 
# 
#  在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调索引 K。如果有多个答案，返回满足条件的最小的索引 K。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[2, 3, 1, 4, 0]
# 输出：3
# 解释：
# 下面列出了每个 K 的得分：
# K = 0,  A = [2,3,1,4,0],    score 2
# K = 1,  A = [3,1,4,0,2],    score 3
# K = 2,  A = [1,4,0,2,3],    score 3
# K = 3,  A = [4,0,2,3,1],    score 4
# K = 4,  A = [0,2,3,1,4],    score 3
# 所以我们应当选择 K = 3，得分最高。 
# 
#  示例 2： 
# 
#  输入：[1, 3, 0, 2, 4]
# 输出：0
# 解释：
# A 无论怎么变化总是有 3 分。
# 所以我们将选择最小的 K，即 0。
#  
# 
#  
# 
#  提示： 
# 
#  
#  A 的长度最大为 20000。 
#  A[i] 的取值范围是 [0, A.length]。 
#  
# 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def bestRotation(self, A: List[int]) -> int:
        """
        https://www.jiuzhang.com/solution/smallest-rotation-with-highest-score#tag-highlight-lang-python
        当Ai = 0 或 N 的话，0这个数字在任何位置都会小于等于坐标值，所以在任何位置都会得分的，不会对最大值产生任何影响，
         同理，如果Ai = N的时候，数字N在任何位置都不得分，同样也不会对最大值产生任何影响。 1, N-1这个范围内的数字在旋转数组的过程中，
         从位置0变到N-1位置的时候，一定会得分，因为此范围的数字最大就是N-1。 对于某个数字Ai，我们想知道其什么时候能旋转到坐标位置为Ai的地方，这样就可以得分了。
         这个最后能得分的临界位置是通过 (i - Ai + N) % N 得到，那么此时如果K再增加1的话，Ai就开始不得分了， 所以我们可以在这个刚好开始不得分的地方标记一下，
         通过-1进行标记，这个位置就是 (i - Ai + 1 + N) % N。 用一个长度为N的change数组，对于每个数字，找到其刚好不得分的地方，进行-1操作，
         change i就表示数组中的数字在i位置会不得分的个数，累加change数组，并且K每增加1的时候，加上额外的1， 最后change数组中最大数字的位置就是要求的K值了
        """
        N = len(A)
        change = [1] * N
        for i in range(N):
            change[(i - A[i] + 1) % N] -= 1

        for i in range(1, N):
            change[i] += change[i - 1]
        # print(change)
        return change.index(max(change))


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([2, 3, 1, 4, 0], 3),
    pytest.param([1, 3, 0, 2, 4], 0),
])
def test_solutions(args, expected):
    assert Solution().bestRotation(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
