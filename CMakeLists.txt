cmake_minimum_required(VERSION 3.17)
project(LeetCodePyC)
enable_language(C)

# CMake version >= 3.10 due to gtest_discover_tests()
# See https://cmake.org/cmake/help/git-stage/module/GoogleTest.html

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} "-pthread")
message("SOURCE_DIR:\t" ${PROJECT_SOURCE_DIR} "\t Binary Out:"
        ${PROJECT_BINARY_DIR} "[Cur Project Dir]" ${CMAKE_CURRENT_LIST_DIR})

enable_testing()
find_package(Check REQUIRED)
add_subdirectory(C)
