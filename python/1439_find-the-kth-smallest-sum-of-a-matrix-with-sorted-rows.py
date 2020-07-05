#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 23:17:50
# @Last Modified : 2020-07-05 23:17:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。 
# 
#  你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。 
# 
#  
# 
#  示例 1： 
# 
#  输入：mat = [[1,3,11],[2,4,6]], k = 5
# 输出：7
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。  
# 
#  示例 2： 
# 
#  输入：mat = [[1,3,11],[2,4,6]], k = 9
# 输出：17
#  
# 
#  示例 3： 
# 
#  输入：mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
# 输出：9
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9 。 
#  
# 
#  示例 4： 
# 
#  输入：mat = [[1,1,10],[2,2,9]], k = 7
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat.length[i] 
#  1 <= m, n <= 40 
#  1 <= k <= min(200, n ^ m) 
#  1 <= mat[i][j] <= 5000 
#  mat[i] 是一个非递减数组 
#  
#  Related Topics 堆 
#  👍 24 👎 0

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """
        Heap
        最小堆存储的是[curr_sum, pointers]二元组，pointers是指针数组，curr_sum是该pointers指向的元素的和。初始化pointers全为0，
                求出相应的curr_sum，并将其入堆。
        重复下列步骤k次：
            从堆中pop出curr_sum和pointers。
            遍历pointers的每个索引，将该索引加一，求出新的和，如果没有出现过，push入堆。

        """
        m, n = len(mat), len(mat[0])
        pointers = tuple([0] * m)
        min_heap = []
        cur_sum = 0
        for i in range(m):
            cur_sum += mat[i][0]
        heapq.heappush(min_heap, [cur_sum, pointers])

        seen = {pointers}
        idx = 0
        while idx < k:
            cur_sum, pointers = heapq.heappop(min_heap)
            for i, j in enumerate(pointers):
                if j < n - 1:
                    new_pointers = list(pointers)
                    new_pointers[i] = j + 1
                    new_pointers = tuple(new_pointers)
                    if new_pointers not in seen:
                        new_sum = cur_sum + mat[i][j + 1] - mat[i][j]
                        heapq.heappush(min_heap, [new_sum, new_pointers])
                        seen.add(new_pointers)
            idx += 1
        return cur_sum


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    """二分"""

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def countArraysHaveSumLessOrEqual(k, r, target):  # Time: O(k + m) ~ O(k * m)
            if target < 0:
                return 0
            if r == len(mat):
                return 1
            result = 0
            for c in range(len(mat[0])):
                cnt = countArraysHaveSumLessOrEqual(k - result, r + 1, target - mat[r][c])
                if not cnt:
                    break
                result += cnt
                if result > k:
                    break
            return result

        MAX_NUM = 5000
        left, right = len(mat), len(mat) * MAX_NUM
        while left <= right:
            mid = left + (right - left) // 2
            cnt = countArraysHaveSumLessOrEqual( k, 0, mid)
            if cnt >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left


@pytest.mark.parametrize("kwargs,expected", [
    (dict(mat=[[1, 3, 11], [2, 4, 6]], k=5), 7),
    pytest.param(dict(mat=[[1, 3, 11], [2, 4, 6]], k=9), 17),
    pytest.param(dict(mat=[[1, 10, 10], [1, 4, 5], [2, 3, 6]], k=7), 9),
    pytest.param(dict(mat=[[1, 1, 10], [2, 2, 9]], k=7), 12),
])
def test_solutions(kwargs, expected):
    assert Solution().kthSmallest(**kwargs) == expected
    assert Solution1().kthSmallest(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
