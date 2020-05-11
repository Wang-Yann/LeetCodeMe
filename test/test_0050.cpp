//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(myPow, test1) {
    int res = myPow(2.0,10);
    ASSERT_EQ(res, 1024.00000);
    ASSERT_DOUBLE_EQ(myPow(2.10000,3), 9.26100);
    ASSERT_DOUBLE_EQ(myPow(2.00000, -2), 0.25000);
    ASSERT_DOUBLE_EQ(myPow(1.00000, -2147483648), 1);
}



int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
