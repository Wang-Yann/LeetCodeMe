#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 实现支持下列接口的「快照数组」- SnapshotArray： 
# 
#  
#  SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。 
#  void set(index, val) - 会将指定索引 index 处的元素设置为 val。 
#  int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。 
#  int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。 
#  
# 
#  
# 
#  示例： 
# 
#  输入：["SnapshotArray","set","snap","set","get"]
#      [[3],[0,5],[],[0,6],[0,0]]
# 输出：[null,null,0,null,5]
# 解释：
# SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
# snapshotArr.set(0,5);  // 令 array[0] = 5
# snapshotArr.snap();  // 获取快照，返回 snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= length <= 50000 
#  题目最多进行50000 次set，snap，和 get的调用 。 
#  0 <= index < length 
#  0 <= snap_id < 我们调用 snap() 的总次数 
#  0 <= val <= 10^9 
#  
#  Related Topics 数组

"""

import bisect

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class SnapshotArray:

    def __init__(self, length: int):
        self.A = [[(-1, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.A[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_right(self.A[index], (snap_id + 1, )) - 1
        # print(i,self.A)
        return self.A[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    snapshotArr = SnapshotArray(3)  # // 初始化一个长度为 3 的快照数组
    assert snapshotArr.set(0, 5)  is None  # // 令 array[0] = 5
    assert snapshotArr.snap() == 0  # // 获取快照，返回 snap_id = 0
    assert snapshotArr.set(0, 6) is None  #
    assert snapshotArr.get(0, 0) == 5  # // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
