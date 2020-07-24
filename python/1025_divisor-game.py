#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。 
# 
#  最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作： 
# 
#  
#  选出任一 x，满足 0 < x < N 且 N % x == 0 。 
#  用 N - x 替换黑板上的数字 N 。 
#  
# 
#  如果玩家无法执行这些操作，就会输掉游戏。 
# 
#  只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：2
# 输出：true
# 解释：爱丽丝选择 1，鲍勃无法进行操作。
#  
# 
#  示例 2： 
# 
#  输入：3
# 输出：false
# 解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 1000 
#  
#  Related Topics 数学 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def divisorGame(self, N: int) -> bool:
        """
        N 为奇数的时候 Alice（先手）必败，NN 为偶数的时候 Alice 必胜。 这个猜想是否正确呢？下面我们来想办法证明它。

        证明
        N = 1  和 N = 2  时结论成立。
        N > 2  时，假设 N≤k 时该结论成立，则 N = k + 1 时：
        """
        # 1. if we get an even, we can choose x = 1
        #    to make the opponent always get an odd
        # 2. if the opponent gets an odd, he can only choose x = 1 or other odds
        #    and we can still get an even
        # 3. at the end, the opponent can only choose x = 1 and we win
        # 4. in summary, we win if only if we get an even and
        #    keeps even until the opponent loses
        return N % 2 == 0


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def divisorGame(self, N: int) -> bool:
        target = [0 for i in range(N + 1)]
        target[1] = 0  # 若爱丽丝抽到1，则爱丽丝输
        if N <= 1:
            return False
        else:

            target[2] = 1  # 若爱丽丝抽到2，则爱丽丝赢
            for i in range(3, N + 1):
                for j in range(1, i // 2):
                    # 若j是i的余数且target[i-j]为假（0）的话，则代表当前为真（1）
                    if i % j == 0 and target[i - j] == 0:
                        target[i] = 1
                        break
            return target[N] == 1


@pytest.mark.parametrize("args,expected", [
    (2, True),
    (3, False),
    (4, True),
])
def test_solutions(args, expected):
    assert Solution().divisorGame(args) == expected
    assert Solution1().divisorGame(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
