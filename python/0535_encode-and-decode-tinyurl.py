#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:25:20
# @Last Modified : 2020-05-05 16:25:20
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import hashlib
import hmac


class Codec:

    def __init__(self):
        self._cache = {}
        self.url = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_obj = hmac.new(b"secret",longUrl.encode(), digestmod="sha256")
        key = hash_obj.hexdigest()[0:6]
        self._cache[key] = longUrl
        print(key)
        return self.url + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.replace(self.url, "")
        return self._cache[key]


if __name__ == '__main__':
    codec = Codec()
    url = "https://leetcode-cn.com/problemset/all/?topicSlugs=math"
    res = codec.decode(codec.encode(url))
    print(res)
