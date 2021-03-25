#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 03:55:45
# @Last Modified : 2021-02-22 03:55:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 nums 表示 1 到 n 的一个排列。我们按照元素在 nums 中的顺序依次插入一个初始为空的二叉查找树（BST）。请你统计将 nums 重
# 新排序后，统计满足如下条件的方案数：重排后得到的二叉查找树与 nums 原本数字顺序得到的二叉查找树相同。 
# 
#  比方说，给你 nums = [2,1,3]，我们得到一棵 2 为根，1 为左孩子，3 为右孩子的树。数组 [2,3,1] 也能得到相同的 BST，但 [3
# ,2,1] 会得到一棵不同的 BST 。 
# 
#  请你返回重排 nums 后，与原数组 nums 得到相同二叉查找树的方案数。 
# 
#  由于答案可能会很大，请将结果对 10^9 + 7 取余数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：nums = [2,1,3]
# 输出：1
# 解释：我们将 nums 重排， [2,3,1] 能得到相同的 BST 。没有其他得到相同 BST 的方案了。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：nums = [3,4,5,1,2]
# 输出：5
# 解释：下面 5 个数组会得到相同的 BST：
# [3,1,2,4,5]
# [3,1,4,2,5]
# [3,1,4,5,2]
# [3,4,1,2,5]
# [3,4,1,5,2]
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：nums = [1,2,3]
# 输出：0
# 解释：没有别的排列顺序能得到相同的 BST 。
#  
# 
#  示例 4： 
# 
#  
# 
#  输入：nums = [3,1,2,5,4,6]
# 输出：19
#  
# 
#  示例 5： 
# 
#  输入：nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
# 输出：216212978
# 解释：得到相同 BST 的方案数是 3216212999。将它对 10^9 + 7 取余后得到 216212978。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= nums.length 
#  nums 中所有数 互不相同 。 
#  
#  Related Topics 动态规划 
#  👍 24 👎 0

"""

from typing import List

import pytest
from scipy.special import comb


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    # math.comb()Python中的method方法用於獲取從n個項目中選擇k個項目(不重複且無順序)的方法數量。
    # 它本質上評估為n！ /(k！*(n-k)！)它也被稱為二項式係數，因為它等效於表達式(1 + x)的多項式展開中的k-th項的係數n。
    # 此方法是Python版本3.8中的新增功能
    """
    首先我们发现一个子树所有可能的方案数是该子树所有节点（除去根节点）的全排列
    但是由于分为左子树右子树，所以全排列肯定是多算的。所以让我们把左右子树分开，那么就是一个组合(n,l)
    即在所有子节点中选出左子树节点的方案数（根据组合特性，选右子树是等价的）。
    但是此时我们发现又少算了左子树和右子树的排列。这里的排列并不是全排列，而是方案数！

    """

    def numOfWays(self, nums: List[int]) -> int:
        def dp(arr):
            if len(arr) < 3:
                return 1
            left = [num for num in arr if num < arr[0]]
            right = [num for num in arr if num > arr[0]]
            l, r = dp(left), dp(right)
            res = comb(len(arr) - 1, len(left)) * l * r
            return res

        return (dp(nums) - 1) % (10 ** 9 + 7)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[2, 1, 3]), 1],
    [dict(nums=[3, 4, 5, 1, 2]), 5],
    [dict(nums=[1, 2, 3]), 0],
    [dict(nums=[3, 1, 2, 5, 4, 6]), 19],
    [dict(nums=[9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18]), 216212978],
])
def test_solutions(kw, expected):
    assert Solution().numOfWays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
