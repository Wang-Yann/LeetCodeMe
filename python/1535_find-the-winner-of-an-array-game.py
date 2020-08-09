#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 14:56:08
# @Last Modified : 2020-08-09 14:56:08
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个由 不同 整数组成的整数数组 arr 和一个整数 k 。 
# 
#  每回合游戏都在数组的前两个元素（即 arr[0] 和 arr[1] ）之间进行。比较 arr[0] 与 arr[1] 的大小，较大的整数将会取得这一回合的
# 胜利并保留在位置 0 ，较小的整数移至数组的末尾。当一个整数赢得 k 个连续回合时，游戏结束，该整数就是比赛的 赢家 。 
# 
#  返回赢得比赛的整数。 
# 
#  题目数据 保证 游戏存在赢家。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [2,1,3,5,4,6,7], k = 2
# 输出：5
# 解释：一起看一下本场游戏每回合的情况：
# 
# 因此将进行 4 回合比赛，其中 5 是赢家，因为它连胜 2 回合。
#  
# 
#  示例 2： 
# 
#  输入：arr = [3,2,1], k = 10
# 输出：3
# 解释：3 将会在前 10 个回合中连续获胜。
#  
# 
#  示例 3： 
# 
#  输入：arr = [1,9,8,2,3,7,6,4,5], k = 7
# 输出：9
#  
# 
#  示例 4： 
# 
#  输入：arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
# 输出：99
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= arr.length <= 10^5 
#  1 <= arr[i] <= 10^6 
#  arr 所含的整数 各不相同 。 
#  1 <= k <= 10^9 
#  
#  Related Topics 数组 
#  👍 7 👎 0
	 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        """
        解答成功: 执行耗时:5444 ms,击败了5.04% 的Python3用户 内存消耗:24.3 MB,击败了43.33% 的Python3用户
        """
        cnt = 0
        N = len(arr)
        if k >= N:
            return max(arr)
        while True:
            if arr[0] > arr[1]:
                cnt += 1
                arr.append(arr.pop(1))
            else:
                cnt = 1
                arr.append(arr.pop(0))
            if cnt >= k or cnt >= N:
                return arr[0]
            # print(arr)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):

    def getWinner(self, arr, k):

        result = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if arr[i] > result:
                result = arr[i]
                count = 0
            count += 1
            if count == k:
                break
        return result


@pytest.mark.parametrize("kwargs,expected", [
    [dict(arr=[2, 1, 3, 5, 4, 6, 7], k=2), 5],
    [dict(arr=[1, 11, 22, 33, 44, 55, 66, 77, 88, 99], k=1000000000), 99],
    [dict(arr=[1, 9, 8, 2, 3, 7, 6, 4, 5], k=7), 9],

    pytest.param(dict(arr=[3, 2, 1], k=10), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().getWinner(**kwargs) == expected
    assert Solution1().getWinner(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
