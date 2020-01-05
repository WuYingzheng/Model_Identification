cmake_minimum_required(VERSION 2.8.11)
project(dsp)

set(QLEDDIR ${CMAKE_CURRENT_SOURCE_DIR}/GuiLib/qled)
link_directories(${QLEDDIR})

# init_qt: Let's do the CMake job for us
set(CMAKE_AUTOMOC ON) # For meta object compiler
set(CMAKE_AUTORCC ON) # Resource files
# UI files https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC.html
set(CMAKE_AUTOUIC ON)               
set(CMAKE_AUTOUIC_SEARCH_PATHS GuiLib)  # where to search the .ui file
# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Find the QtWidgets library
find_package(Qt5 REQUIRED Widgets)
find_package(Qt5 REQUIRED Charts)

include_directories(
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        ${CMAKE_CURRENT_SOURCE_DIR}/GuiLib
        ${CMAKE_CURRENT_SOURCE_DIR}/GuiLib/chart
        )

link_directories( ${QLEDDIR} )

set(SOURCES
        main.cpp
        GuiLib/MainWindow.cpp
        GuiLib/chart/chart.cpp
        GuiLib/chart/chartview.cpp
        )

add_executable(${PROJECT_NAME} ${SOURCES})

target_link_libraries(
                ${PROJECT_NAME} 
                Qt5::Widgets
                Qt5::Charts
                )