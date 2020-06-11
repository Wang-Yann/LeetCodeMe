//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(dailyTemperatures, test1) {
    int nums[] = {73, 74, 75, 71, 69, 72, 76, 73};
    int expected[] = {1, 1, 4, 2, 1, 1, 0, 0};
    int returnSize;
    int* result = dailyTemperatures(nums, sizeof(nums) / sizeof(int),&returnSize);
    ASSERT_EQ(returnSize,sizeof(nums)/ sizeof(int));
    for (int i = 0; i < returnSize; ++i) {
        ASSERT_EQ(result[i], expected[i]);
    }
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
