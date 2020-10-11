cmake_minimum_required(VERSION 3.17)
project(LeetCodePyC)
enable_language(C)



#set(CMAKE_BUILD_RPATH ${PROJECT_SOURCE_DIR}/build/)
#set(PROJECT_BINARY_DIR ${PROJECT_SOURCE_DIR}/bin/)
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR})
# CMake version >= 3.10 due to gtest_discover_tests()
# See https://cmake.org/cmake/help/git-stage/module/GoogleTest.html
#https://libcheck.github.io/check/doc/check_html/check_4.html
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

set(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} "-pthread")
message("SOURCE_DIR:\t" ${PROJECT_SOURCE_DIR}
        "\t BINARY Out:" ${PROJECT_BINARY_DIR}
        "[Cur Project Dir]" ${CMAKE_CURRENT_LIST_DIR})
enable_testing()
find_package(Check REQUIRED)
add_subdirectory(C)
