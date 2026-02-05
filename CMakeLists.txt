cmake_minimum_required(VERSION 3.10)
project(Argus_ALPR)

set(CMAKE_CXX_STANDARD 17)

# Find OpenCV package on the system
find_package(OpenCV REQUIRED)

# Include OpenCV headers
include_directories(${OpenCV_INCLUDE_DIRS})

# Create the executable from main.cpp
add_executable(argus_core src/main.cpp)

# Link the executable to OpenCV libraries
target_link_libraries(argus_core ${OpenCV_LIBS})
