#
# Copyright Troy D. Straszheim
#
# Distributed under the Boost Software License, Version 1.0.
# See http://www.boost.org/LICENSE_1_0.txt
#
cmake_minimum_required(VERSION 2.8)

enable_testing()

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin)

find_package(PythonLibs)
find_package(PythonInterp)

if (CMAKE_BUILD_TYPE MATCHES "Deb")
  add_definitions(-DBOOST_PYTHON_DEBUG)
endif()

find_package(Boost)
message("Boost headers at ${Boost_INCLUDE_DIRS}")

set(INCLUDE_PATH   
  ${PYTHON_INCLUDE_PATH} 
  ${CMAKE_CURRENT_SOURCE_DIR}/include
  ${Boost_INCLUDE_DIRS})

include_directories(${INCLUDE_PATH})

#
#  Macro for building python extensions
#
macro(python_extension MODULE_NAME)

  add_library(${MODULE_NAME} SHARED
    ${ARGN}
    )
  target_link_libraries(${MODULE_NAME} boost_python)

  set_target_properties(${MODULE_NAME}
    PROPERTIES
    OUTPUT_NAME "${MODULE_NAME}"
    PREFIX ""
    COMPILE_FLAGS "-DBPL_EXTENSION_MODULE=${MODULE_NAME}"
    )

endmacro()


add_subdirectory(src)
add_subdirectory(test)

# Can't get this to work properly.  Also there's not an 'uninstall'
# target, and I find cmake a little clunky for things like this.
# So as always, I'll turn to python.
#
#install(SCRIPT install.cmake)
#create a file name install.cmake and add the following lines:
# find_package(Boost)
# message("Boost headers at ${Boost_INCLUDE_DIRS}")
# ...
# -- Could NOT find Boost
# Boost_INCLUDE_DIRS = Boost_INCLUDE_DIR-NOTFOUND
# 
# It's not clear to me why it couldn't find boost
# in the install.cmake script since it could find it just
# fine above.

add_custom_target(install ${CMAKE_CURRENT_SOURCE_DIR}/install.py 
  "-i${Boost_INCLUDE_DIRS}" 
  "-l${Boost_LIBRARY_DIRS}"
  "-I${CMAKE_CURRENT_SOURCE_DIR}/include"
  "-L${CMAKE_CURRENT_BINARY_DIR}/lib")

add_custom_target(uninstall ${CMAKE_CURRENT_SOURCE_DIR}/install.py 
  "--uninstall"
  "-i${Boost_INCLUDE_DIRS}" 
  "-l${Boost_LIBRARY_DIRS}")

add_custom_target(check_install ${CMAKE_CURRENT_SOURCE_DIR}/install.py 
  "--check_installation"
  "-i${Boost_INCLUDE_DIRS}" 
  "-l${Boost_LIBRARY_DIRS}")


