//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(kidsWithCandies, test1) {
    int candies[] = {2, 3, 5, 1, 3};
    int candiesSize = sizeof(candies)/ sizeof(int);
    int extraCandies = 3;
    int returnSize;
    bool expected[]={true,true,true,false,true};
    bool *res = kidsWithCandies(candies, candiesSize, extraCandies, &returnSize);
    sleep(30);
    ASSERT_EQ(returnSize,candiesSize);
//    ASSERT_EQ(sizeof(expected), sizeof(res));
    for (int i = 0; i < returnSize; ++i) {
        ASSERT_EQ(res[i], expected[i]);
    }
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

//bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize)