//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(largestRectangleArea, test1) {
    int nums[] = {2, 1, 5, 6, 2, 3};
    int result = largestRectangleArea(nums, sizeof(nums) / sizeof(int));

    ASSERT_EQ(10, result);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
