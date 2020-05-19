//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(validPalindrome, test1) {
    char s1[] = "abcd";
    char s2[] = "abb";
    char * s3 = "deeee";
    char s4[] = "eeccccbebaeeabebccceea";
    ASSERT_FALSE(validPalindrome(s1));
    ASSERT_FALSE(validPalindrome(s4));
    ASSERT_TRUE(validPalindrome(s2));
    ASSERT_TRUE(validPalindrome(s3));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
