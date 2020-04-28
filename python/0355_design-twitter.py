#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-13 21:02:00
# @Last Modified : 2020-04-13 21:02:00
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import collections
import heapq
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # userId-> List[twitterIds]
        self.__user_tweet_map = collections.defaultdict(list)
        # userId-> Set[flowerIds]
        self.__user_followers_map = collections.defaultdict(set)
        # userId-> List[twitterIds]
        self.__time = 0
        self.__cnt_of_recent_tweets = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.__time += 1
        self.__user_tweet_map[userId].append((self.__time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        max_heap = []
        limit = self.__cnt_of_recent_tweets
        if self.__user_tweet_map[userId]:
            for times, t_id in self.__user_tweet_map[userId][-limit:]:
                heapq.heappush(max_heap, (-times, userId, t_id))
        for uid in self.__user_followers_map[userId]:
            if self.__user_tweet_map[uid]:
                for times, t_id in self.__user_tweet_map[uid][-limit:]:
                    heapq.heappush(max_heap, (-times, uid, t_id))
        result = []
        while max_heap and len(result) < limit:
            times, uid, t_id = heapq.heappop(max_heap)
            result.append(t_id)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.__user_followers_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.__user_followers_map[followerId].discard(followeeId)

    def __str__(self) -> str:
        return "Tweeter: {}\nFollows: {}\n".format(
            self.__user_tweet_map,
            self.__user_followers_map,
        )


if __name__ == '__main__':
    twitter = Twitter()
    print(None)
    print(twitter.postTweet(1, 1))
    print(twitter.getNewsFeed(1))
    print(twitter.follow(2, 1))
    # print(twitter)
    print(twitter.getNewsFeed(2))
    print(twitter.unfollow(2, 1))
    print(twitter.getNewsFeed(2))
