//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(firstMissingPositive, test1) {
    int nums[] = {3, 4, -1, 1, -4};
    int res = firstMissingPositive(nums, sizeof(nums) / sizeof(int));
    ASSERT_EQ(res, 2);

}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}