package com.rock.ltc;

import com.rock.ltc.utils.TreeNode;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * @Author: Rock
 * @Date: 2021-05-17 22:22
 * @Description:
 */
public class Solution1to1000Test {
    private final Solution0403 solution0403 = new Solution0403();
    private final Solution0810 solution0810 = new Solution0810();
    private final Solution0993 solution0993 = new Solution0993();
    
    static Stream<Arguments> testSolution0443() {
        return Stream.of(
                Arguments.of(new int[]{0, 1, 3, 5, 6, 8, 12, 17}, true),
                Arguments.of(new int[]{0, 1, 2, 3, 4, 8, 9, 11}, false)
        );
    }
    
    
    static Stream<Arguments> testSolution0810() {
        return Stream.of(
                Arguments.of(new int[]{1, 1, 2}, false)
        );
    }
    
    static Stream<Arguments> testSolution0993() {
        return Stream.of(
                Arguments.of(TreeNode.initTree(new Integer[]{1, 2, 3, 4}), 4, 3, false),
                Arguments.of(TreeNode.initTree(new Integer[]{1, 2, 3, null, 4, null, 5}), 5, 4, true),
                Arguments.of(TreeNode.initTree(new Integer[]{1, 2, 3, null, 4}), 2, 3, false)
        );
    }
    
    
    @ParameterizedTest
    @MethodSource
    void testSolution0993(TreeNode root, int x, int y, Boolean res) {
        TreeNode.printMidOrderTree(root);
        assertEquals(solution0993.isCousins(root, x, y), res);
    }
    
    
    @ParameterizedTest
    @MethodSource
    void testSolution0443(int[] stones, Boolean res) {
        assertEquals(solution0403.canCross(stones), res);
    }
    
    @ParameterizedTest
    @MethodSource
    void testSolution0810(int[] nums, Boolean res) {
        assertEquals(solution0810.xorGame(nums), res);
    }
    
}
