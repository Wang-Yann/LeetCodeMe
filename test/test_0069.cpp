//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(mySqrt2, test1) {
    int n = 4;
    int res = mySqrt(n);
    ASSERT_EQ(res, 2);
}

TEST(mySqrt1, test2) {
    int n = 8;
    int res = mySqrt(n);
    ASSERT_EQ(res, 2);
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
