//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(productExceptSelf, test1) {
    int nums[] = {1,2,3,4};
    int expected[] = {24,12,8,6};
    int returnSize;
    int* result = productExceptSelf(nums, sizeof(nums) / sizeof(int),&returnSize);
    for (int i = 0; i < returnSize; ++i) {
        ASSERT_EQ(result[i], expected[i]);
    }
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
