#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 23:07:02
# @Last Modified : 2021-02-22 23:07:02
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 秋日市集上有个奇怪的黑盒，黑盒的主视图为 n*m 的矩形。从黑盒的主视图来看，黑盒的上面和下面各均匀分布有 m 个小孔，黑盒的左面和右面各均匀分布有 n
# 个小孔。黑盒左上角小孔序号为 0，按顺时针编号，总共有 2*(m+n) 个小孔。每个小孔均可以打开或者关闭，初始时，所有小孔均处于关闭状态。每个小孔上的盖子均为
# 镜面材质。例如一个 2*3 的黑盒主视图与其小孔分布如图所示:
# 
# ![image.png](https://pic.leetcode-cn.com/1598951281-ZCBrif-image.png){:height=
# "200px"}
# 
# 店长告诉小扣，这里是「几何学的快问快答」，店长可能有两种操作：
# 
# - `open(int index, int direction)` - 若小孔处于关闭状态，则打开小孔，照入光线；否则直接照入光线；
# - `close(int index)` - 关闭处于打开状态小孔，店长保证不会关闭已处于关闭状态的小孔；
# 
# 其中：
# - `index`： 表示小孔序号
# - `direction`：`1` 表示光线沿 $y=x$ 方向，`-1` 表示光线沿 $y=-x$ 方向。
# 
# ![image.png](https://pic.leetcode-cn.com/1599620810-HdOlMi-image.png){:height=
# "200px"}
# 
# 
# 当光线照至边界时：若边界上的小孔为开启状态，则光线会射出；否则，光线会在小孔之间进行反射。特别地：
# 1. 若光线射向未打开的拐角（黑盒顶点），则光线会原路反射回去；
# 2. 光线自拐角处的小孔照入时，只有一种入射方向（如自序号为 0 的小孔照入方向只能为 `-1`）
# 
# ![image.png](https://pic.leetcode-cn.com/1598953840-DLiAsf-image.png){:height=
# "200px"}
# 
# 请帮助小扣判断并返回店长每次照入的光线从几号小孔射出。
# 
# 
# **示例 1：**
# >输入：
# >`["BlackBox","open","open","open","close","open"]`
# >`[[2,3],[6,-1],[4,-1],[0,-1],[6],[0,-1]]`
# >
# >输出：`[null,6,4,6,null,4]`
# >
# >解释：
# >BlackBox b = BlackBox(2,3); // 新建一个 2x3 的黑盒
# >b.open(6,-1) // 打开 6 号小孔，并沿 y=-x 方向照入光线，光线至 0 号小孔反射，从 6 号小孔射出
# >b.open(4,-1) // 打开 4 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 4-2-8-2-4，从 4 号小孔射出
# >b.open(0,-1) // 打开 0 号小孔，并沿 y=-x 方向照入光线，由于 6 号小孔为开启状态，光线从 6 号小孔射出
# >b.close(6) // 关闭 6 号小孔
# >b.shoot(0,-1) // 从 0 号小孔沿 y=-x 方向照入光线，由于 6 号小孔为关闭状态，4 号小孔为开启状态，光线轨迹为 0-6-4，从 
# 4 号小孔射出
# 
# **示例 2：**
# >输入：
# >`["BlackBox","open","open","open","open","close","open","close","open"]`
# >`[[3,3],[1,-1],[5,1],[11,-1],[11,1],[1],[11,1],[5],[11,-1]]`
# >
# >输出：`[null,1,1,5,1,null,5,null,11]`
# >
# >解释：
# >
# >![image.png](https://pic.leetcode-cn.com/1599204202-yGDMVk-image.png){:height
# ="300px"}
# >
# >BlackBox b = BlackBox(3,3); // 新建一个 3x3 的黑盒
# >b.open(1,-1) // 打开 1 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 1-5-7-11-1，从 1 号小孔射出
# >b.open(5,1) // 打开 5 号小孔，并沿 y=x 方向照入光线，光线轨迹为 5-7-11-1，从 1 号小孔射出
# >b.open(11,-1) // 打开 11 号小孔，并沿逆 y=-x 方向照入光线，光线轨迹为 11-7-5，从 5 号小孔射出
# >b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1，从 1 号小孔射出
# >b.close(1) // 关闭 1 号小孔
# >b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1-5，从 5 号小孔射出
# >b.close(5) // 关闭 5 号小孔
# >b.open(11,-1) // 从 11 号小孔沿 y=-x 方向照入光线，光线轨迹为 11-1-5-7-11，从 11 号小孔射出
# 
# 
# 
# **提示：**
# - `1 <= n, m <= 10000`
# - `1 <= 操作次数 <= 10000`
# - `direction` 仅为 `1` 或 `-1`
# - `0 <= index < 2*(m+n)`
#  👍 12 👎 0
"""
import bisect

import pytest


# https://leetcode-cn.com/problems/IQvJ9i/solution/yu-chu-li-chu-suo-you-de-xun-huan-_python3ban-ben-/
# from sortedcontainers import SortedDict as TreeMap

# leetcode submit region begin(Prohibit modification and deletion)


class TreeSet(object):
    """
    Binary-tree set like java Treeset.
    Duplicate elements will not be added.
    When added new element, TreeSet will be sorted automatically.
    """

    def __init__(self, elements):
        self._treeset = []
        self.addAll(elements)

    def addAll(self, elements):
        for element in elements:
            if element in self:
                continue
            self.add(element)

    def add(self, element):
        if element not in self:
            bisect.insort(self._treeset, element)

    def ceiling_index(self, e, exclusive=False):
        index = bisect.bisect_right(self._treeset, e)
        if exclusive:
            return index
        if index > 0 and self[index - 1] == e:
            return index - 1
        return index

    def floor_index(self, e, exclusive=False):
        index = bisect.bisect_left(self._treeset, e)
        if exclusive:
            return index - 1
        if index < len(self) and self[index] == e:
            return index
        return index - 1

    def ceiling(self, e, exclusive=False):
        index = self.ceiling_index(e, exclusive)
        if 0 <= index < len(self):
            return self[index]
        return None

    def floor(self, e, exclusive=False):
        index = self.floor_index(e, exclusive)
        if 0 <= index < len(self):
            return self[index]
        return None

    def __getitem__(self, num):
        return self._treeset[num]

    def __len__(self):
        return len(self._treeset)

    def clear(self):
        """
        Delete all elements in TreeSet.
        """
        self._treeset = []

    def clone(self):
        """
        Return shallow copy of self.
        """
        return TreeSet(self._treeset)

    def remove(self, element):
        """
        Remove element if element in TreeSet.
        """
        try:
            self._treeset.remove(element)
        except ValueError:
            return False
        return True

    def __iter__(self):
        """
        Do ascending iteration for TreeSet
        """
        for element in self._treeset:
            yield element

    def pop(self, index):
        return self._treeset.pop(index)

    def __str__(self):
        return str(self._treeset)

    def __eq__(self, target):
        if isinstance(target, TreeSet):
            return self._treeset == target.treeset
        elif isinstance(target, list):
            return self._treeset == target

    def __contains__(self, e):
        """
        Fast attribution judgment by bisect
        """
        try:
            return e == self._treeset[bisect.bisect_left(self._treeset, e)]
        except:
            return False


class TreeMap(dict):
    """
    "TreeMap" is a dictionary with sorted keys similar to java TreeMap.
    Keys, iteration, items, values will all return values ordered by key.
    Otherwise it should behave just like the builtin dict.
    """

    def __init__(self, seq=None, **kwargs):
        if seq is None:
            super().__init__(**kwargs)
        else:
            super().__init__(seq, **kwargs)
        self.sorted_keys = TreeSet(super().keys())

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.sorted_keys.add(key)

    def __delitem__(self, key):
        super().__delitem__(key)
        self.sorted_keys.remove(key)

    def keys(self):
        return self.sorted_keys

    def items(self):
        return [(k, self[k]) for k in self.sorted_keys]

    def __iter__(self):
        for k in self.sorted_keys:
            yield k

    def values(self):
        for k in self.sorted_keys:
            yield self[k]

    def clear(self):
        super().clear()
        self.sorted_keys.clear()

    def ceiling_index(self, e, exclusive=False):
        return self.sorted_keys.ceiling_index(e, exclusive)

    def floor_index(self, e, exclusive=False):
        return self.sorted_keys.floor_index(e, exclusive)

    def ceiling_key(self, e, exclusive=False):
        return self.sorted_keys.ceiling(e, exclusive)

    def floor_key(self, e, exclusive=False):
        return self.sorted_keys.floor(e, exclusive)

    def ceiling_value(self, e, exclusive=False):
        key = self.ceiling_key(e, exclusive)
        return self[key] if key is not None else None

    def floor_value(self, e, exclusive=False):
        key = self.floor_key(e, exclusive)
        return self[key] if key is not None else None


class BlackBox:

    # pip install sortedcontainers

    def __init__(self, n: int, m: int):
        self.groupPos, self.groupNeg, self.groupStats = [], [], []
        ptCount = (n + m) * 2
        self.groupPos, self.groupNeg = [(-1, -1) for _ in range(ptCount)], [(-1, -1) for _ in range(ptCount)]
        for i in range(ptCount):
            # 如果不是左上角或者右下角的小孔，那么从 y=x 方向射出找循环
            if i != 0 and i != m + n and self.groupPos[i][0] == -1:
                self.createGroup(n, m, i, 1)
            # 如果不是左下角或者右上角的小孔，那么从 y=-x 方向射出找循环
            if i != m and i != m * 2 + n and self.groupNeg[i][0] == -1:
                self.createGroup(n, m, i, -1)

    def createGroup(self, n: int, m: int, index: int, direction: int):
        groupId = len(self.groupStats)
        groupLoc = 0
        self.groupStats.append(TreeMap())
        # 不断模拟光线的路径，直到走到一个已经遇见过的状态，这样就找到了一个循环
        while not (direction == 1 and self.groupPos[index][0] != -1) and not (direction == -1 and self.groupNeg[index][0] != -1):
            if direction == 1:
                self.groupPos[index] = (groupId, groupLoc)
                index = (n + m) * 2 - index
            else:
                self.groupNeg[index] = (groupId, groupLoc)
                index = m * 2 - index if index <= m * 2 else (m * 2 + n) * 2 - index
            # 如果小孔不在角上，就改变方向
            if index != 0 and index != m and index != m + n and index != m * 2 + n:
                direction = -direction
            groupLoc += 1

    def open(self, index: int, direction: int) -> int:
        # 插入二元组
        groupId, groupLoc = self.groupPos[index]
        if groupId != -1:
            self.groupStats[groupId][groupLoc] = index
        groupId, groupLoc = self.groupNeg[index]
        if groupId != -1:
            self.groupStats[groupId][groupLoc] = index

        # 查询
        groupId, groupLoc = self.groupPos[index] if direction == 1 else self.groupNeg[index]
        store = self.groupStats[groupId]
        ceiling = store.ceiling_value(groupLoc, exclusive=True)
        if ceiling:
            return ceiling
        return store[store.keys()[0]]

    def close(self, index: int) -> None:
        # 删除二元组
        groupId, groupLoc = self.groupPos[index]
        if groupId != -1:
            del self.groupStats[groupId][groupLoc]
        groupId, groupLoc = self.groupNeg[index]
        if groupId != -1:
            del self.groupStats[groupId][groupLoc]


# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox(n, m)
# param_1 = obj.open(index,direction)
# obj.close(index)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    b = BlackBox(3, 3)  # 新建一个 3x3 的黑盒
    assert b.open(1, -1) == 1  # 打开 1 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 1-5-7-11-1，从 1 号小孔射出
    assert b.open(5, 1) == 1  # 打开 5 号小孔，并沿 y=x 方向照入光线，光线轨迹为 5-7-11-1，从 1 号小孔射出
    assert b.open(11, -1) == 5  # 打开 11 号小孔，并沿逆 y=-x 方向照入光线，光线轨迹为 11-7-5，从 5 号小孔射出
    assert b.open(11, 1) == 1  # 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1，从 1 号小孔射出
    b.close(1)  # 关闭 1 号小孔
    assert b.open(11, 1) == 5  # 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1-5，从 5 号小孔射出
    b.close(5)  # 关闭 5 号小孔
    assert b.open(11, -1) == 11  # 从 11 号小孔沿 y=-x 方向照入光线，光线轨迹为 11-1-5-7-11，从 11 号小孔射出


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
