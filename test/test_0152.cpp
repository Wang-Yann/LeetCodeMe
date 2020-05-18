//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(maxProduct, test1) {
    int nums[] = {2,3,-2,4};
    int nums1[] = {-2,0,-1};
    int nums2[] = {-4,-3};
    int result = maxProduct(nums, sizeof(nums) / sizeof(int));
    int result1 = maxProduct(nums1, sizeof(nums1) / sizeof(int));
    int result2 = maxProduct(nums2, sizeof(nums1) / sizeof(int));

    ASSERT_EQ(6, result);
    ASSERT_EQ(0, result1);
    ASSERT_EQ(12, result2);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
