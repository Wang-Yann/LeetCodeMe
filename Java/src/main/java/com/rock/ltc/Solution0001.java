package com.rock.ltc;

// @Author        : Rock Wayne
// @Created       : 2021-09-30 23:09:03
// @Last Modified : 2021-09-30 23:09:03

// 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
//
// 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
//
// 你可以按任意顺序返回答案。
//
//
//
// 示例 1：
//
//
// 输入：nums = [2,7,11,15], target = 9
// 输出：[0,1]
// 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
//
//
// 示例 2：
//
//
// 输入：nums = [3,2,4], target = 6
// 输出：[1,2]
//
//
// 示例 3：
//
//
// 输入：nums = [3,3], target = 6
// 输出：[0,1]
//
//
//
//
// 提示：
//
//
// 2 <= nums.length <= 10⁴
// -10⁹ <= nums[i] <= 10⁹
// -10⁹ <= target <= 10⁹
// 只会存在一个有效答案
//
//
// 进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？
// Related Topics 数组 哈希表 👍 12245 👎 0

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.*;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

class Solution0001 {

  static Stream<Arguments> testSolution() {
    return Stream.of(
        Arguments.of(new int[] {2, 7, 11, 15}, 9, new int[] {0, 1}),
        Arguments.of(new int[] {3, 2, 4}, 6, new int[] {1, 2}),
        Arguments.of(new int[] {3, 3}, 6, new int[] {0, 1}));
  }
  // leetcode submit region end(Prohibit modification and deletion)

  @ParameterizedTest
  @MethodSource
  void testSolution(int[] nums, int target, int[] res) {
    Solution solution = new Solution();
    assertArrayEquals(solution.twoSum(nums, target), res);
  }

  // leetcode submit region begin(Prohibit modification and deletion)
  class Solution {
    public int[] twoSum(int[] nums, int target) {
      Map<Integer, Integer> map = new HashMap<>();
      for (int i = 0; i < nums.length; i++) {
        if (map.containsKey(target - nums[i])) {
          return new int[] {map.get(target - nums[i]), i};
        } else {

          map.put(nums[i], i);
        }
      }
      return new int[] {-1, -1};
    }
  }
}
