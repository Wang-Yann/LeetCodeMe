//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}
//421
//400
//47 结果偏差 2e-6

TEST(new21Game, test1) {
    ASSERT_DOUBLE_EQ(new21Game(6, 1, 10), 0.6);
    double res = new21Game(21, 17, 10);
    ASSERT_TRUE(abs(res - 0.73278) < 1e-5);
//    ASSERT_NEAR(new21Game(21,17,10), 0.73278,1e-6);

    ASSERT_DOUBLE_EQ(new21Game(10, 1, 10), 1.0);
//    ASSERT_DOUBLE_EQ(new21Game(421,400,47), 0.71188);
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
