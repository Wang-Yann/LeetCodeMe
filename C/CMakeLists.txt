enable_language(C)

include_directories(
        ${CMAKE_CURRENT_LIST_DIR}/include
)

add_subdirectory(include)
file(GLOB_RECURSE C_SRC_LIST ${CMAKE_CURRENT_LIST_DIR}/tests/*.c)
#AUX_SOURCE_DIRECTORY(./tests C_SRC_LIST)
foreach (V ${C_SRC_LIST})
    get_filename_component(EV ${V} NAME_WE)
    message("-------------------------EXE----------------------\n" ${EV} " --> " ${V})
    if (${EV} MATCHES "main_test")
        continue()
    endif ()

    if (${EV} MATCHES "^zz_")
        string(REPLACE "zz_" "" TV ${EV})
        add_executable(${TV} ${V})
        target_link_libraries(${TV} rock_lt_c check)
        continue()
    endif ()
    string(REPLACE "test" "T" TST_TARGET ${EV})
    message(${EV})
    add_executable(${EV} tests/main_test.c ${V})
    target_link_libraries(${EV}
            PRIVATE
            rock_lt_c
            check
            rt
            m
            subunit
            )
    message("------------------------------------------------\n")
endforeach ()
#
#add_executable(main_test tests/main_test.c tests/test_0002.c tests/test_0009.c)
#    target_link_libraries(main_test
#            PRIVATE
#            rock_lt_c
#            check
#            pthread
#            rt
#            m
#            subunit
#            )