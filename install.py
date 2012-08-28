#!/usr/bin/env python
# This script is run during 'make install' and 'make uninstall'
# All this does is 'hide' python.hpp, python/, and libboost_python.so
# and creates links to the corresponding boost::python V3 paths.
#
# This is less than ideal, since it swaps out boost::python globally,
# so *everything* you rebuild will be against this version.  Ideally
# it would be preferable to point cmake to just the new python component.
# I don't see an easy way to do that aside from maintaining a private
# version of FindBoost.cmake that provides that feature.  Probably the
# best way to go in the end.
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--boost_include_dir", dest="BOOST_INCLUDE_DIR",
                  help="Path to the boost include.", metavar="BOOST_INCLUDE_DIR")
parser.add_option("-l", "--boost_library_dir", dest="BOOST_LIBRARY_DIRS",
                  help="Path to the boost libraries.", metavar="BOOST_LIBRARY_DIRS")
parser.add_option("-I", "--source_include_dir", dest="SOURCE_INCLUDE_DIR",
                  help="Path to the installation source.", metavar="SOURCE_INCLUDE_DIR")
parser.add_option("-L", "--source_library_dir", dest="SOURCE_LIBRARY_DIR",
                  help="Path to the installation libraries.", metavar="SOURCE_LIBRARY_DIR")
parser.add_option("-u", "--uninstall", dest="UNINSTALL",
                  action="store_true", default = False,
                  help="Switch back to default boost::python.")
parser.add_option("-c", "--check_installation", dest="CHECK_INSTALLATION",
                  action="store_true", default = False,
                  help="Print whether boost::python V3 is installed or not.")
(options, args) = parser.parse_args()

import os, copy

def hide(pathname):
    old_pathname = copy.copy(pathname)
    if pathname.endswith("/"):
        pathname = pathname.rstrip("/")
    index = pathname.rfind("/")
    new_pathname = pathname[:index+1] + "." + pathname[index+1:]
    os.rename(old_pathname, new_pathname)

def ressurect(pathname):
    old_pathname = copy.copy(pathname)
    if pathname.count("/.") == 1 :
        new_pathname = pathname.replace("/.","/")
        os.rename(old_pathname, new_pathname)
    else:
        print "not sure how to handle this '%s'"\
              % pathname

def safe_rm(pathname):
    # verify they're soft links first so we don't do any real damage
    if os.path.islink(pathname):
        os.remove(pathname)
    else:
        print "this %s is NOT a link." % pathname

def is_installed():
    return os.path.islink(options.BOOST_INCLUDE_DIR + "/boost/python")\
           and os.path.islink(options.BOOST_INCLUDE_DIR + "/boost/python.hpp")\
           and os.path.islink(options.BOOST_LIBRARY_DIRS + "/libboost_python.so")

if options.CHECK_INSTALLATION:
    print "boost::python V3 is", "not installed" \
          if not is_installed() else "installed"
else:
    if options.UNINSTALL:
        # uninstall
        if is_installed():
            safe_rm(options.BOOST_INCLUDE_DIR + "/boost/python")
            safe_rm(options.BOOST_INCLUDE_DIR + "/boost/python.hpp")
            safe_rm(options.BOOST_LIBRARY_DIRS + "/libboost_python.so")
            
            ressurect(options.BOOST_INCLUDE_DIR + "/boost/.python")
            ressurect(options.BOOST_INCLUDE_DIR + "/boost/.python.hpp")
            ressurect(options.BOOST_LIBRARY_DIRS + "/.libboost_python.so")
        else:
            print "Not installed.  Doing nothing."
    
    else:
        # install
        if not is_installed():
            hide(options.BOOST_INCLUDE_DIR + "/boost/python")
            hide(options.BOOST_INCLUDE_DIR + "/boost/python.hpp")
            hide(options.BOOST_LIBRARY_DIRS + "/libboost_python.so")
            
            os.symlink(options.SOURCE_INCLUDE_DIR + "/boost/python",\
                       options.BOOST_INCLUDE_DIR + "/boost/python")
            
            os.symlink(options.SOURCE_INCLUDE_DIR + "/boost/python.hpp",\
                       options.BOOST_INCLUDE_DIR + "/boost/python.hpp")
            
            os.symlink(options.SOURCE_LIBRARY_DIR + "/libboost_python.so",\
                       options.BOOST_LIBRARY_DIRS + "/libboost_python.so")
            
        else:
            print "Already installed.  Doing nothing."

    
    
