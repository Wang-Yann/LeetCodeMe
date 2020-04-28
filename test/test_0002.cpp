//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"
extern  "C"
{
#include "leetcode_functions.h"

}


TEST(two_sum_test, twoSum002) {
    int nums[4] = {2, 8, 11, 15};
    int target = 9;
    int numsSize = 3;
    int ret = 2;
    int *result = twoSum(nums, numsSize, target, &ret);

    ASSERT_EQ(0, *result);
    ASSERT_EQ(1, *(result + 1));
}

TEST(two_sum_test, twoSum001) {
    int nums[4] = {2, 7, 11, 15};
    int target = 9;
    int numsSize = 4;
    int ret = 2;
    int *result = twoSum(nums, numsSize, target, &ret);

    ASSERT_EQ(0, *result);
    ASSERT_EQ(1, *(result + 1));
}

//int main(int argc, char **argv) {
//    ::testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();
//}
