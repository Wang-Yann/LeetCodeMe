//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
#include "test_common.cpp"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(isValid, test1) {
    char s1[]= "()[]{}";
    char s2[]= "(]";
    char s3[] = "()";
    char s4[] = "([)]";
    ASSERT_EQ(isValid(s1), true);
    ASSERT_EQ(isValid(s2), true);
    ASSERT_EQ(isValid(s3), true);
    ASSERT_EQ(isValid(s4), true);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}