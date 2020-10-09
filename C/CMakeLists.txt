message("SOURCE_DIR:\t" ${PROJECT_SOURCE_DIR} "\t Binary Out:"
        ${PROJECT_BINARY_DIR} "[Cur Project Dir]" ${CMAKE_CURRENT_LIST_DIR})
include_directories(${CMAKE_CURRENT_LIST_DIR}/include)

ADD_SUBDIRECTORY(include)
file(GLOB_RECURSE C_SRC_LIST ${CMAKE_CURRENT_LIST_DIR}/test/*.c)
foreach (V ${C_SRC_LIST})
    get_filename_component(EV ${V} NAME_WE)
    message("\n--------------------------EXE----------------------\n" ${EV} " --> " ${V})
    if(${EV} MATCHES "main_test")
        continue()
    endif()
    set(TST_TARGET TST_${EV})
    add_executable(${TST_TARGET} test/main_test.c ${V})
    target_link_libraries(${TST_TARGET}
        PRIVATE
        rock_lt_c
        check
        rt
        m
        subunit
    )
endforeach ()

