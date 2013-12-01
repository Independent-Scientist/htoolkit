import abc


class FunctorImplException(Exception):
    pass


class Functor(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        object.__init__(self)
        self.initialized = False
        self.meta_data = dict()

    @abc.abstractmethod
    def meta(self):
        """
            Functor documentation. it should return a dictionary following this pattern.
            Some fields are required and will be asserted on the @functor_doc_base_assert.

            meta_data = { 'version': '0.0.1',
                          'name': 'TheFunctorName',
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
        return self.meta_data

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


def functor_assert_meta(fn_meta):
    """
        meta data assertion *decorator*
    """

    from functools import wraps
    @wraps(fn_meta)
    def wrapper(*args):

        meta_data = args[0].meta_data

        if not type(meta_data) is dict or len(meta_data) == 0:
            raise FunctorImplException("Not a dictionary data!")

        if meta_data['name'] is None or meta_data['name'] == "":
            raise FunctorImplException("Functor without a name!")

        if meta_data['description'] is None or meta_data['name'] == "":
            raise FunctorImplException("Functor without a name!")

        return fn_meta(*args)

    return wrapper




__author__ = 'leozito'