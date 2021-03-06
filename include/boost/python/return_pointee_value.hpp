// Copyright Roman Yakovenko, Maximilian Matthe 2006, 2008.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)
/*
 * Generic return value policy for functions returning pointers which should be 
 * exposed as values. Can be used to return pointers to non-exposed types.
 *
 * The code is adapted from 
 * http://mail.python.org/pipermail/c++-sig/2006-November/011568.html .
 */
#ifndef RETURN_POINTEE_VALUE_HPP_TDS20091024
#define RETURN_POINTEE_VALUE_HPP_TDS20091024

# include <boost/python/detail/prefix.hpp>
# include <boost/python/detail/indirect_traits.hpp>
# include <boost/python/object.hpp>
# include <boost/mpl/if.hpp>
# include <boost/python/to_python_indirect.hpp>
# include <boost/type_traits/composite_traits.hpp>


namespace boost{ 
  namespace python{ 
    namespace detail{

      struct make_value_holder
      {
	template <class T>
	static PyObject* execute(T* p)
	{
	  if (p == 0)
	    {
	      return python::detail::none();
	    }
	  else
	    {
	      object p_value( *p );
	      return incref( p_value.ptr() );
	    }
	}
      };

      template <class R>
      struct return_pointee_value_requires_a_pointer_return_type
# if defined(__GNUC__) && __GNUC__ >= 3 || defined(__EDG__)
      {}
# endif
      ;

    } //detail

    struct return_pointee_value
    {
      template <class T>
      struct apply
      {
	BOOST_STATIC_CONSTANT( bool, ok = is_pointer<T>::value );

	typedef typename mpl::if_c<
	  ok, 
	  to_python_indirect<T, detail::make_value_holder>,
	  detail::return_pointee_value_requires_a_pointer_return_type<T>
	  >::type type;
    };
  };


} } //boost::python 

#endif
