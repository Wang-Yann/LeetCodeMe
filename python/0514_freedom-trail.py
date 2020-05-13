#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 视频游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。 
# 
#  给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。 
# 
#  最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，
# 以此逐个拼写完 key 中的所有字符。 
# 
#  旋转 ring 拼出 key 字符 key[i] 的阶段中： 
# 
#  
#  您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符
#  key[i] 。 
#  如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段
# ）, 直至完成所有拼写。 
#  
# 
#  示例： 
# 
#  
# 
# 
#  
# 
#  输入: ring = "godding", key = "gd"
# 输出: 4
# 解释:
#  对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。 
#  对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
#  当然, 我们还需要1步进行拼写。
#  因此最终的输出是 4。
#  
# 
#  提示： 
# 
#  
#  ring 和 key 的字符串长度取值范围均为 1 至 100； 
#  两个字符串中都只有小写字符，并且均可能存在重复字符； 
#  字符串 key 一定可以由字符串 ring 旋转拼出。 
#  Related Topics 深度优先搜索 分治算法 动态规划

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        TODO TODO
        https://leetcode-cn.com/problems/freedom-trail/solution/shi-yong-shen-du-you-xian-sou-suo-jia-ji-yi-hua-by/
        ring="godding", key="gd"
        """

        @functools.lru_cache(None)
        def dfs(ring, key, index):
            if index >= len(key):
                return 0

            res = 0
            # 找到所有能旋转的位置
            l_index = ring.find(key[index])

            min_val = []
            while l_index != -1:
                # 如果当前位置在字符串左半边，使用逆时针旋转 + 1 是拼写操作
                if l_index <= len(ring) // 2:
                    min_val.append(l_index + 1)
                else:
                    # 否则使用顺时针旋转
                    min_val.append(len(ring) - l_index + 1)
                # 获得旋转后的新表盘
                new_ring = ring[l_index:] + ring[:l_index]

                # 寻找下一个旋转点
                min_val[-1] += dfs(new_ring, key, index + 1)
                l_index = ring.find(key[index], l_index + 1)

            res = res + min(min_val) if min_val else 0
            return res

        return dfs(ring, key, 0)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        https://leetcode-cn.com/problems/freedom-trail/solution/dong-tai-gui-hua-wu-xu-er-wei-shu-zu-by-zhong-wu-q/
        """
        # 用哈希字典 charPos 记录 ring 中每个字符出现的所有位置，加快查找
        charPos = {}
        for i, char in enumerate(ring):
            if char not in charPos:
                charPos[char] = []
            charPos[char].append(i)

        n = len(ring)

        # last，curr 中存放二元组：
        #       （轮盘指针处在的位置，到达该位置需要的最少步数）
        # last 表示上一个找到字符的情况
        # curr 表示当前字符的情况，每一轮进行填充
        # last 初始化为一个元素(0, 0)，表示最开始轮盘处在位置 0，已经走了0 步
        last = [(0, 0)]
        curr = []

        for char in key:  # 当前要找的字符
            for currPos in charPos[char]:  # 要指向该字符，指针应该到达的所有位置
                leastStep = last[0][1] + n  # 到达该位置所需最少步数，初始化为一个较大的值
                for (lastPos, lastStep) in last:  # 上个字符所有可能位置，及其相应累积的最少步数
                    # 从上个字符的位置，到达当前位置，所需的最少步数
                    leastStep = min(lastStep + min((currPos + n - lastPos) % n,
                                                   (lastPos + n - currPos) % n) + 1, leastStep)
                # 找到到达当前位置的最少步数，把（位置，步数）放入 curr
                curr.append((currPos, leastStep))

            # 填好 curr 后，滚动 last 和 curr 两个数组
            last, curr = curr, last
            curr.clear()

        # 返回最少步数
        return min(list(map(lambda x: x[1], last)))


@pytest.mark.parametrize("kw,expected", [
    (dict(ring="godding", key="gd"), 4)
])
def test_solutions(kw, expected):
    assert Solution().findRotateSteps(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
