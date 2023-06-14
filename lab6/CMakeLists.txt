cmake_minimum_required(VERSION 3.10)

project(lab6)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED true)

add_library(shortest_path shortest_path.cpp)

add_executable(t6 t6.cpp)

target_link_libraries(t6 shortest_path)