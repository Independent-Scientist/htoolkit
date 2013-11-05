import abc


def functor_doc_assert(fn):
    """
        Please use this *decorator* on inhereted doc functions
    """
    from functools import wraps
    @wraps(fn)
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)

    return wrapper


def functor_perform_assert(fn):
    """
        Please use this *decorator* on inhereted doc functions
    """
    from functools import wraps
    @wraps(fn)
    def wrapper(*args, **kwargs):

        if not self.initilized:
            raise Exception()

        fn(self)

    return wrapper


class FunctorImplException(Exception):
    pass


class Functor(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        object.__init__(self)
        self.initialized = False


    @abc.abstractmethod
    def doc(self):
        """
            Functor documentation. it should return a dictionary following this pattern.
            Some fields are required and will be asserted on the @functor_doc_base_assert.

            doc_obj = { 'name': 'TheFunctorName',
                        'description' : 'The Functor description',
                        'tags': {'get','perform','transform'},
                        'depends': { 'module1', 'module2' },
                        'params': {'x','y','z'},
                        'params_description': {},
                        'params_types': {'int', 'complex', 'CustomType'},
                        'returns_description': { 'A tuple containg info ...' },
                        'returns_type': TupleType }
                      }
        """
        print "hello from doc base ..."

    @abc.abstractmethod
    def initialize(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def perform(self):
        pass

    @abc.abstractmethod
    def finalize(self):
        pass

    def initialized(self):
        return self.initialized










__author__ = 'leozito'