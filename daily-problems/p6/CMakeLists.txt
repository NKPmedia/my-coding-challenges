cmake_minimum_required(VERSION 3.13)  # CMake version check
project(p6)               # Create project "simple_example"
set(CMAKE_CXX_STANDARD 14)            # Enable c++14 standard

# Add main.cpp file of project root directory as source file
set(SOURCE_FILES main.cpp List.cpp List.h Element.cpp Element.h)

# Add executable target with source files listed in SOURCE_FILES variable
add_executable(p6 ${SOURCE_FILES})