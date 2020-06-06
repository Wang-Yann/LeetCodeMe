//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(longestConsecutive, test1) {
    int nums[] = {100, 4, 200, 1, 3, 2};
    int result = longestConsecutive(nums, sizeof(nums) / sizeof(int));

    ASSERT_EQ(4, result);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
