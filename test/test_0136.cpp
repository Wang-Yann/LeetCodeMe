//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(singleNumber, test1) {
    int nums[] = {2, 2, 1};
    int nums1[] = {4, 1, 2, 1, 2};
    int result = singleNumber(nums, sizeof(nums) / sizeof(int));
    int result1 = singleNumber(nums1, sizeof(nums1) / sizeof(int));

    ASSERT_EQ(1, result);
    ASSERT_EQ(4, result1);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
