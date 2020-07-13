#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 14:13:16
# @Last Modified : 2020-07-13 14:13:16
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若
# 有多个相同元素，返回索引值最小的一个。 
# 
#  示例1: 
# 
#   输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
#  输出: 8（元素5在该数组中的索引）
#  
# 
#  示例2: 
# 
#   输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
#  输出：-1 （没有找到）
#  
# 
#  提示: 
# 
#  
#  arr 长度范围在[1, 1000000]之间 
#  
#  Related Topics 数组 二分查找 
#  👍 21 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1
        left, right = 0, len(arr) - 1
        while left < right:  # 循环结束条件left==right
            mid = (left + right) >> 1
            if arr[left] < arr[mid]:  # 如果左值小于中值，说明左边区间升序
                if arr[left] <= target <= arr[mid]:  # 如果目标在左边的升序区间中，右边界移动到mid
                    right = mid
                else:  # 否则目标在右半边，左边界移动到mid+1
                    left = mid + 1
            elif arr[left] > arr[mid]:  # 如果左值大于中值，说明左边不是升序，右半边升序
                if arr[left] <= target or target <= arr[mid]:  # 如果目标在左边，右边界移动到mid
                    right = mid
                else:  # 否则目标在右半边的升序区间中，左边界移动到mid+1
                    left = mid + 1
            elif arr[left] == arr[mid]:  # 如果左值等于中值，可能是已经找到了目标，也可能是遇到了重复值
                if arr[left] != target:  # 如果左值不等于目标，说明还没找到，需要逐一清理重复值
                    left += 1
                else:  # 如果左值等于目标，说明已经找到最左边的目标值
                    right = left  # 将右边界移动到left，循环结束
        return left if arr[left] == target else -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=5), 8],
    [dict(arr=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=11), -1],
    [dict(arr=[1, 5, 5, 1, 2, 3, 4, 5], target=5), 1],
    [dict(arr=[5, 5, 5, 1, 2, 3, 4, 5], target=5), 0],
])
def test_solutions(kw, expected):
    assert Solution().search(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
