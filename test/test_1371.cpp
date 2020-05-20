//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(findTheLongestSubstring, test1) {
    char s1[] = "eleetminicoworoep";
    char s2[] = "leetcodeisgreat";
    char *s3 = "bcbcbc";
    ASSERT_EQ(findTheLongestSubstring(s1),13);
    ASSERT_EQ(findTheLongestSubstring(s2),5);
    ASSERT_EQ(findTheLongestSubstring(s3),6);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
