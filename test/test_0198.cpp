//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(rob, test1) {
    int nums[] = {1,2,3,1};
    int nums1[] = {2,7,9,3,1};
    int result = rob(nums, sizeof(nums) / sizeof(int));
    int result1 = rob(nums1, sizeof(nums1) / sizeof(int));

    ASSERT_EQ( result,4);
    ASSERT_EQ( result1,12);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
