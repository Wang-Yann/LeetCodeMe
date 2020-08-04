#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 18:35:38
# @Last Modified : 2020-08-04 18:35:38
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 为了评估某网站的用户转化率，我们需要对用户的访问行为进行分析，并建立用户行为模型。日志文件中已经记录了用户名、访问时间 以及 页面路径。 
# 
#  为了方便分析，日志文件中的 N 条记录已经被解析成三个长度相同且长度都为 N 的数组，分别是：用户名 username，访问时间 timestamp 和 
# 页面路径 website。第 i 条记录意味着用户名是 username[i] 的用户在 timestamp[i] 的时候访问了路径为 website[i] 的
# 页面。 
# 
#  我们需要找到用户访问网站时的 『共性行为路径』，也就是有最多的用户都 至少按某种次序访问过一次 的三个页面路径。需要注意的是，用户 可能不是连续访问 这三
# 个路径的。 
# 
#  『共性行为路径』是一个 长度为 3 的页面路径列表，列表中的路径 不必不同，并且按照访问时间的先后升序排列。 
# 
#  如果有多个满足要求的答案，那么就请返回按字典序排列最小的那个。（页面路径列表 X 按字典序小于 Y 的前提条件是：X[0] < Y[0] 或 X[0] =
# = Y[0] 且 (X[1] < Y[1] 或 X[1] == Y[1] 且 X[2] < Y[2])） 
# 
#  题目保证一个用户会至少访问 3 个路径一致的页面，并且一个用户不会在同一时间访问两个路径不同的页面。 
# 
#  
# 
#  示例： 
# 
#  输入：username = ["joe","joe","joe","james","james","james","james","mary","mary
# ","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career
# ","home","cart","maps","home","home","about","career"]
# 输出：["home","about","career"]
# 解释：
# 由示例输入得到的记录如下：
# ["joe", 1, "home"]
# ["joe", 2, "about"]
# ["joe", 3, "career"]
# ["james", 4, "home"]
# ["james", 5, "cart"]
# ["james", 6, "maps"]
# ["james", 7, "home"]
# ["mary", 8, "home"]
# ["mary", 9, "about"]
# ["mary", 10, "career"]
# 有 2 个用户至少访问过一次 ("home", "about", "career")。
# 有 1 个用户至少访问过一次 ("home", "cart", "maps")。
# 有 1 个用户至少访问过一次 ("home", "cart", "home")。
# 有 1 个用户至少访问过一次 ("home", "maps", "home")。
# 有 1 个用户至少访问过一次 ("cart", "maps", "home")。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= N = username.length = timestamp.length = website.length <= 50 
#  1 <= username[i].length <= 10 
#  0 <= timestamp[i] <= 10^9 
#  1 <= website[i].length <= 10 
#  username[i] 和 website[i] 都只含小写字符 
#  
#  Related Topics 排序 数组 哈希表 
#  👍 4 👎 0

"""

import collections
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        理解题意
        最恶心的！！！！！！！！ 那就是他要的是最多客户访问的答案，不是最多访问次数。
        也就是有的路径三个人，分别访问了一次，算作3，但是如果是一个人访问了3次，只算1

        """
        data_hub = sorted(list(zip(timestamp, username, website)))
        lookup = collections.defaultdict(list)
        for t, u, w in data_hub:
            lookup[u].append(w)
        counter = collections.Counter()
        # TODO　学习下这种写法
        # counter = sum([collections.Counter(set(itertools.combinations(lookup[u], 3))) for u in lookup], collections.Counter())
        for ws in lookup.values():
            for l in set(itertools.combinations(ws, 3)):
                tl = tuple(l)
                counter[tl] += 1
        # print(counter)
        return list(min(counter, key=lambda x: (-counter[x], x)))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
        timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]

    ), ["home", "about", "career"]],
    [dict(
        username=["u1", "u1", "u1", "u2", "u2", "u2"],
        timestamp=[1, 2, 3, 4, 5, 6],
        website=["a", "b", "a", "a", "b", "c"]

    ), ["a", "b", "a"]],
    [dict(
        username=["h", "eiy", "cq", "h", "cq", "txldsscx", "cq", "txldsscx", "h", "cq", "cq"],
        timestamp=[527896567, 334462937, 517687281, 134127993, 859112386, 159548699, 51100299, 444082139, 926837079,
                   317455832, 411747930],
        website=["hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi",
                 "hibympufi", "yljmntrclw", "hibympufi", "yljmntrclw"]

    ), ["hibympufi", "hibympufi", "yljmntrclw"]],
    # code_output:["hibympufi","hibympufi","hibympufi"]

])
def test_solutions(kw, expected):
    assert Solution().mostVisitedPattern(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
