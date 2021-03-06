# Copyright Troy D. Straszheim 2009. Distributed under the Boost
# Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
'''
>>> from ambig1_ext import *
Traceback (most recent call last):
...
AmbiguousOverload: Boost.Python function ambig1_ext.f
has ambiguous overloads.  C++ signatures
  f(float) -> std::string
and
  f(double) -> std::string
are indistinguishable to python.
'''
