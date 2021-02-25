#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 05:44:08
# @Last Modified : 2021-02-25 05:44:08
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，其中的整数也 互不相同 。请你以 任意顺序 连接 pi
# eces 中的数组以形成 arr 。但是，不允许 对每个数组 pieces[i] 中的整数重新排序。 
# 
#  如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [85], pieces = [[85]]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [15,88], pieces = [[88],[15]]
# 输出：true
# 解释：依次连接 [15] 和 [88]
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [49,18,16], pieces = [[16,18,49]]
# 输出：false
# 解释：即便数字相符，也不能重新排列 pieces[0]
#  
# 
#  示例 4： 
# 
#  
# 输入：arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
# 输出：true
# 解释：依次连接 [91]、[4,64] 和 [78] 
# 
#  示例 5： 
# 
#  
# 输入：arr = [1,3,5,7], pieces = [[2,4,6,8]]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= pieces.length <= arr.length <= 100 
#  sum(pieces[i].length) == arr.length 
#  1 <= pieces[i].length <= arr.length 
#  1 <= arr[i], pieces[i][j] <= 100 
#  arr 中的整数 互不相同 
#  pieces 中的整数 互不相同（也就是说，如果将 pieces 扁平化成一维数组，数组中的所有整数互不相同） 
#  
#  Related Topics 排序 数组 哈希表 
#  👍 22 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        res = []

        for num in arr:
            res += mp.get(num, [])

        return res == arr


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[85], pieces=[[85]]), True],
    [dict(arr=[15, 88], pieces=[[88], [15]]), True],
    [dict(arr=[49, 18, 16], pieces=[[16, 18, 49]]), False],
    [dict(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]]), True],
    [dict(arr=[1, 3, 5, 7], pieces=[[2, 4, 6, 8]]), False],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().canFormArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
