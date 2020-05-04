//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"
extern  "C"
{
#include "leetcode_functions.h"

}


TEST(reverse, reverse1) {

    ASSERT_EQ(reverse(123), 321);
    ASSERT_EQ(reverse(-123), -321);
    ASSERT_EQ(reverse(2147483647), 0);
}

TEST(reverse, reverse2) {

    ASSERT_EQ(reverse(1200), 21);
    ASSERT_EQ(reverse(120), 21);
    ASSERT_EQ(reverse(0), 0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
