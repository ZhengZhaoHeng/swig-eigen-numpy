# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_permutohedral')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_permutohedral')
    _permutohedral = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_permutohedral', [dirname(__file__)])
        except ImportError:
            import _permutohedral
            return _permutohedral
        if fp is not None:
            try:
                _mod = imp.load_module('_permutohedral', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _permutohedral = swig_import_helper()
    del swig_import_helper
else:
    import _permutohedral
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _permutohedral.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self) -> "PyObject *":
        return _permutohedral.SwigPyIterator_value(self)

    def incr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _permutohedral.SwigPyIterator_incr(self, n)

    def decr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _permutohedral.SwigPyIterator_decr(self, n)

    def distance(self, x: 'SwigPyIterator') -> "ptrdiff_t":
        return _permutohedral.SwigPyIterator_distance(self, x)

    def equal(self, x: 'SwigPyIterator') -> "bool":
        return _permutohedral.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _permutohedral.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _permutohedral.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _permutohedral.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _permutohedral.SwigPyIterator_previous(self)

    def advance(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _permutohedral.SwigPyIterator_advance(self, n)

    def __eq__(self, x: 'SwigPyIterator') -> "bool":
        return _permutohedral.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: 'SwigPyIterator') -> "bool":
        return _permutohedral.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _permutohedral.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _permutohedral.SwigPyIterator___isub__(self, n)

    def __add__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _permutohedral.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _permutohedral.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _permutohedral.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vectorMatrixXf(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _permutohedral.vectorMatrixXf_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _permutohedral.vectorMatrixXf___nonzero__(self)

    def __bool__(self) -> "bool":
        return _permutohedral.vectorMatrixXf___bool__(self)

    def __len__(self) -> "std::vector< Eigen::MatrixXf >::size_type":
        return _permutohedral.vectorMatrixXf___len__(self)

    def pop(self) -> "std::vector< Eigen::MatrixXf >::value_type":
        return _permutohedral.vectorMatrixXf_pop(self)

    def __getslice__(self, i: 'std::vector< Eigen::MatrixXf >::difference_type', j: 'std::vector< Eigen::MatrixXf >::difference_type') -> "std::vector< Eigen::MatrixXf,std::allocator< Eigen::MatrixXf > > *":
        return _permutohedral.vectorMatrixXf___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _permutohedral.vectorMatrixXf___setslice__(self, *args)

    def __delslice__(self, i: 'std::vector< Eigen::MatrixXf >::difference_type', j: 'std::vector< Eigen::MatrixXf >::difference_type') -> "void":
        return _permutohedral.vectorMatrixXf___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _permutohedral.vectorMatrixXf___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< Eigen::MatrixXf >::value_type const &":
        return _permutohedral.vectorMatrixXf___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _permutohedral.vectorMatrixXf___setitem__(self, *args)

    def append(self, x: 'std::vector< Eigen::MatrixXf >::value_type const &') -> "void":
        return _permutohedral.vectorMatrixXf_append(self, x)

    def empty(self) -> "bool":
        return _permutohedral.vectorMatrixXf_empty(self)

    def size(self) -> "std::vector< Eigen::MatrixXf >::size_type":
        return _permutohedral.vectorMatrixXf_size(self)

    def swap(self, v: 'vectorMatrixXf') -> "void":
        return _permutohedral.vectorMatrixXf_swap(self, v)

    def begin(self) -> "std::vector< Eigen::MatrixXf >::iterator":
        return _permutohedral.vectorMatrixXf_begin(self)

    def end(self) -> "std::vector< Eigen::MatrixXf >::iterator":
        return _permutohedral.vectorMatrixXf_end(self)

    def rbegin(self) -> "std::vector< Eigen::MatrixXf >::reverse_iterator":
        return _permutohedral.vectorMatrixXf_rbegin(self)

    def rend(self) -> "std::vector< Eigen::MatrixXf >::reverse_iterator":
        return _permutohedral.vectorMatrixXf_rend(self)

    def clear(self) -> "void":
        return _permutohedral.vectorMatrixXf_clear(self)

    def get_allocator(self) -> "std::vector< Eigen::MatrixXf >::allocator_type":
        return _permutohedral.vectorMatrixXf_get_allocator(self)

    def pop_back(self) -> "void":
        return _permutohedral.vectorMatrixXf_pop_back(self)

    def erase(self, *args) -> "std::vector< Eigen::MatrixXf >::iterator":
        return _permutohedral.vectorMatrixXf_erase(self, *args)

    def __init__(self, *args):
        this = _permutohedral.new_vectorMatrixXf(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x: 'std::vector< Eigen::MatrixXf >::value_type const &') -> "void":
        return _permutohedral.vectorMatrixXf_push_back(self, x)

    def front(self) -> "std::vector< Eigen::MatrixXf >::value_type const &":
        return _permutohedral.vectorMatrixXf_front(self)

    def back(self) -> "std::vector< Eigen::MatrixXf >::value_type const &":
        return _permutohedral.vectorMatrixXf_back(self)

    def assign(self, n: 'std::vector< Eigen::MatrixXf >::size_type', x: 'std::vector< Eigen::MatrixXf >::value_type const &') -> "void":
        return _permutohedral.vectorMatrixXf_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _permutohedral.vectorMatrixXf_resize(self, *args)

    def insert(self, *args) -> "void":
        return _permutohedral.vectorMatrixXf_insert(self, *args)

    def reserve(self, n: 'std::vector< Eigen::MatrixXf >::size_type') -> "void":
        return _permutohedral.vectorMatrixXf_reserve(self, n)

    def capacity(self) -> "std::vector< Eigen::MatrixXf >::size_type":
        return _permutohedral.vectorMatrixXf_capacity(self)
    __swig_destroy__ = _permutohedral.delete_vectorMatrixXf
    __del__ = lambda self: None
vectorMatrixXf_swigregister = _permutohedral.vectorMatrixXf_swigregister
vectorMatrixXf_swigregister(vectorMatrixXf)

class vectorVectorXf(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _permutohedral.vectorVectorXf_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _permutohedral.vectorVectorXf___nonzero__(self)

    def __bool__(self) -> "bool":
        return _permutohedral.vectorVectorXf___bool__(self)

    def __len__(self) -> "std::vector< Eigen::VectorXf >::size_type":
        return _permutohedral.vectorVectorXf___len__(self)

    def pop(self) -> "std::vector< Eigen::VectorXf >::value_type":
        return _permutohedral.vectorVectorXf_pop(self)

    def __getslice__(self, i: 'std::vector< Eigen::VectorXf >::difference_type', j: 'std::vector< Eigen::VectorXf >::difference_type') -> "std::vector< Eigen::VectorXf,std::allocator< Eigen::VectorXf > > *":
        return _permutohedral.vectorVectorXf___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _permutohedral.vectorVectorXf___setslice__(self, *args)

    def __delslice__(self, i: 'std::vector< Eigen::VectorXf >::difference_type', j: 'std::vector< Eigen::VectorXf >::difference_type') -> "void":
        return _permutohedral.vectorVectorXf___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _permutohedral.vectorVectorXf___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< Eigen::VectorXf >::value_type const &":
        return _permutohedral.vectorVectorXf___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _permutohedral.vectorVectorXf___setitem__(self, *args)

    def append(self, x: 'std::vector< Eigen::VectorXf >::value_type const &') -> "void":
        return _permutohedral.vectorVectorXf_append(self, x)

    def empty(self) -> "bool":
        return _permutohedral.vectorVectorXf_empty(self)

    def size(self) -> "std::vector< Eigen::VectorXf >::size_type":
        return _permutohedral.vectorVectorXf_size(self)

    def swap(self, v: 'vectorVectorXf') -> "void":
        return _permutohedral.vectorVectorXf_swap(self, v)

    def begin(self) -> "std::vector< Eigen::VectorXf >::iterator":
        return _permutohedral.vectorVectorXf_begin(self)

    def end(self) -> "std::vector< Eigen::VectorXf >::iterator":
        return _permutohedral.vectorVectorXf_end(self)

    def rbegin(self) -> "std::vector< Eigen::VectorXf >::reverse_iterator":
        return _permutohedral.vectorVectorXf_rbegin(self)

    def rend(self) -> "std::vector< Eigen::VectorXf >::reverse_iterator":
        return _permutohedral.vectorVectorXf_rend(self)

    def clear(self) -> "void":
        return _permutohedral.vectorVectorXf_clear(self)

    def get_allocator(self) -> "std::vector< Eigen::VectorXf >::allocator_type":
        return _permutohedral.vectorVectorXf_get_allocator(self)

    def pop_back(self) -> "void":
        return _permutohedral.vectorVectorXf_pop_back(self)

    def erase(self, *args) -> "std::vector< Eigen::VectorXf >::iterator":
        return _permutohedral.vectorVectorXf_erase(self, *args)

    def __init__(self, *args):
        this = _permutohedral.new_vectorVectorXf(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x: 'std::vector< Eigen::VectorXf >::value_type const &') -> "void":
        return _permutohedral.vectorVectorXf_push_back(self, x)

    def front(self) -> "std::vector< Eigen::VectorXf >::value_type const &":
        return _permutohedral.vectorVectorXf_front(self)

    def back(self) -> "std::vector< Eigen::VectorXf >::value_type const &":
        return _permutohedral.vectorVectorXf_back(self)

    def assign(self, n: 'std::vector< Eigen::VectorXf >::size_type', x: 'std::vector< Eigen::VectorXf >::value_type const &') -> "void":
        return _permutohedral.vectorVectorXf_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _permutohedral.vectorVectorXf_resize(self, *args)

    def insert(self, *args) -> "void":
        return _permutohedral.vectorVectorXf_insert(self, *args)

    def reserve(self, n: 'std::vector< Eigen::VectorXf >::size_type') -> "void":
        return _permutohedral.vectorVectorXf_reserve(self, n)

    def capacity(self) -> "std::vector< Eigen::VectorXf >::size_type":
        return _permutohedral.vectorVectorXf_capacity(self)
    __swig_destroy__ = _permutohedral.delete_vectorVectorXf
    __del__ = lambda self: None
vectorVectorXf_swigregister = _permutohedral.vectorVectorXf_swigregister
vectorVectorXf_swigregister(vectorVectorXf)

class Neighbors(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    n1 = _swig_property(_permutohedral.Neighbors_n1_get, _permutohedral.Neighbors_n1_set)
    n2 = _swig_property(_permutohedral.Neighbors_n2_get, _permutohedral.Neighbors_n2_set)

    def __init__(self, n1: 'int'=0, n2: 'int'=0):
        this = _permutohedral.new_Neighbors(n1, n2)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _permutohedral.delete_Neighbors
    __del__ = lambda self: None
Neighbors_swigregister = _permutohedral.Neighbors_swigregister
Neighbors_swigregister(Neighbors)

class Permutohedral(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        this = _permutohedral.new_Permutohedral()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def init(self, features: 'Eigen::MatrixXf const &') -> "void":
        return _permutohedral.Permutohedral_init(self, features)

    def compute(self, *args) -> "void":
        return _permutohedral.Permutohedral_compute(self, *args)

    def gradient(self, df: 'float *', a: 'float const *', b: 'float const *', value_size: 'int') -> "void":
        return _permutohedral.Permutohedral_gradient(self, df, a, b, value_size)
    __swig_destroy__ = _permutohedral.delete_Permutohedral
    __del__ = lambda self: None
Permutohedral_swigregister = _permutohedral.Permutohedral_swigregister
Permutohedral_swigregister(Permutohedral)


