//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(translateNum, test1) {
    int res = translateNum(12258);
    ASSERT_EQ(res,5);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

//bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize)