//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(isPalindrome, test1) {
    ASSERT_TRUE(isPalindrome(121));
    ASSERT_FALSE(isPalindrome(123));
    ASSERT_FALSE(isPalindrome(-121));
    ASSERT_FALSE(isPalindrome(2147483647));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
