// Copyright Troy D. Straszheim 2009
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

//  See http://www.boost.org/libs/python for documentation.

#ifndef PYTHON_LIMITS_TDS_20090917_HPP_INCLUDED
# define PYTHON_LIMITS_TDS_20090917_HPP_INCLUDED

# ifdef FUSION_MAX_VECTOR_SIZE
#  error BOOST_FUSION_INVOKE_MAX_ARITY already defined.  Fusion may balk at signatures with large numbers of arguments.
# endif

# ifndef BOOST_PYTHON_MAX_ARITY
#  define BOOST_PYTHON_MAX_ARITY 15
#  define FUSION_MAX_VECTOR_SIZE BOOST_PYTHON_MAX_ARITY
#  define FUSION_MAX_LIST_SIZE BOOST_PYTHON_MAX_ARITY
#  define BOOST_FUSION_INVOKE_MAX_ARITY BOOST_PYTHON_MAX_ARITY
# endif

# ifndef BOOST_PYTHON_MAX_BASES
#  define BOOST_PYTHON_MAX_BASES 10
# endif 

// check to be sure we're not over the hardcoded limit
// of 24 arguments in type_traits
#if BOOST_PYTHON_MAX_ARITY > 24
#error "BOOST_PYTHON_MAX_ARITY is too high.  boost::is_member_function_pointer is required by boost.python, and it has a hardcoded limit of 24 arguments."
#endif

#endif // PYTHON_LIMITS_TDS_20090917_HPP_INCLUDED
