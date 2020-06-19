//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
#include "test_common.cpp"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(isPalindrome1, test1) {
    char s1[]= "A man, a plan, a canal: Panama ";
    char s2[]= "race a car";
    char s3[]= "0P";
    ASSERT_EQ(isPalindrome1(s1), true);
    ASSERT_EQ(isPalindrome1(s2), false);
    ASSERT_FALSE(isPalindrome1(s3));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}