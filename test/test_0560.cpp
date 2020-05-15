//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(subarraySum, test1) {
    int nums[] = {1, 1, 1};
    int result = subarraySum(nums, sizeof(nums) / sizeof(int),2);

    ASSERT_EQ(2, result);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
