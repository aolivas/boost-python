// Copyright Troy D. Straszheim 2009
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#include <boost/python.hpp>

#include "bpl_test.hpp"
#include "overloads.hpp"

BPL_TEST_MODULE()
{
  r<float>();
  r<double>();
}


