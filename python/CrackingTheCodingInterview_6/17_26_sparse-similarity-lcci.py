#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-15 16:27:52
# @Last Modified : 2020-07-15 16:27:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 两个(具有不同单词的)文档的交集(intersection)中元素的个数除以并集(union)中元素的个数，就是这两个文档的相似度。例如，{1, 5, 3}
#  和 {1, 7, 2, 3} 的相似度是 0.4，其中，交集的元素有 2 个，并集的元素有 5 个。给定一系列的长篇文档，每个文档元素各不相同，并与一个 ID
#  相关联。它们的相似度非常“稀疏”，也就是说任选 2 个文档，相似度都很接近 0。请设计一个算法返回每对文档的 ID 及其相似度。只需输出相似度大于 0 的组合
# 。请忽略空文档。为简单起见，可以假定每个文档由一个含有不同整数的数组表示。 
# 
#  输入为一个二维数组 docs，docs[i] 表示 id 为 i 的文档。返回一个数组，其中每个元素是一个字符串，代表每对相似度大于 0 的文档，其格式为
#  {id1},{id2}: {similarity}，其中 id1 为两个文档中较小的 id，similarity 为相似度，精确到小数点后 4 位。以任意顺序
# 返回数组均可。 
# 
#  示例: 
# 
#  输入: 
# [
#  [14, 15, 100, 9, 3],
#  [32, 1, 9, 3, 5],
#  [15, 29, 2, 6, 8, 7],
#  [7, 10]
# ]
# 输出:
# [
#  "0,1: 0.2500",
#  "0,2: 0.1000",
#  "2,3: 0.1429"
# ] 
# 
#  提示： 
# 
#  
#  docs.length <= 500 
#  docs[i].length <= 500 
#  
#  Related Topics 哈希表 
#  👍 9 👎 0

"""

import collections
from typing import List

import pytest

from sample_datas import BIG_17_26


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        """
        TODO GOOD
        关于小数的舍入 (二进制保存的值有点误差导致的)
        round(1.315,2)==1.31
        print(Decimal(1.325))
        1.3249999999999999555910790149937383830547332763671875
        print(round(1.145,2))
        #打印结果
        1.15
        print(Decimal(1.145))
        #打印结果
        1.145000000000000017763568394002504646778106689453125

        """

        def round_up(f, n):
            """这样解决上面文档字符串的舍入问题"""
            return int(f * 10 ** n) / 10 ** n

        dic1 = collections.defaultdict(list)
        for i, doc in enumerate(docs):
            for num in doc:
                dic1[num].append(i)
        dic2 = collections.defaultdict(int)
        for li in dic1.values():
            for p in range(len(li)):
                for q in range(p + 1, len(li)):
                    pair = li[p], li[q]
                    dic2[pair] += 1
        # print(dic1,dic2,sep="\n")
        res = []
        min_ellipis = 1e-9  # 解决测试用例　'74,90: 0.0312'　舍入问题
        for (p, q), i in dic2.items():
            u = len(docs[p]) + len(docs[q]) - i
            res.append("{0:d},{1:d}: {2:.4f}".format(p, q, i / u + min_ellipis))
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        docs=[
            [14, 15, 100, 9, 3],
            [32, 1, 9, 3, 5],
            [15, 29, 2, 6, 8, 7],
            [7, 10]
        ]
    ),
        [
            "0,1: 0.2500",
            "0,2: 0.1000",
            "2,3: 0.1429"
        ]
    ],

    [dict(docs=BIG_17_26.BIG_CASE), BIG_17_26.BIG_RES],
])
def test_solutions(kw, expected):
    assert sorted(Solution().computeSimilarities(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
