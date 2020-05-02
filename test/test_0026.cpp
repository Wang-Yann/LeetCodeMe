//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
extern  "C"
{
#include "leetcode_functions.h"

}


TEST(nthUglyNumberTest, test1) {
    int n=3;
    int res = nthUglyNumber(n);
    ASSERT_EQ(res, 3);
}

TEST(nthUglyNumberTest1, test2) {
    int n=10;
    int res = nthUglyNumber(n);
    ASSERT_EQ(res, 12);
}

//int main(int argc, char **argv) {
//    ::testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();
//}
