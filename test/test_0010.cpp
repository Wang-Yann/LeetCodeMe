//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
#include "test_common.cpp"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(isMatch, test1) {
    char s1[]= "mississippi";
    char p1[]= "mis*is*p*.";
    ASSERT_EQ(isMatch(s1,p1), false);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}