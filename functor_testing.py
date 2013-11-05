from base.functors.functor import *


class GenericFunctor(Functor):

    def __init__(self):
        super(GenericFunctor, self).__init__()
        self.msg = 'Hello World'

    @functor_doc_assert
    def doc(self):
        print self.initialized
        return None

    def initialize(self, *args, **kwargs):
        pass

    @functor_perform_assert
    def perform(self):
        super(GenericFunctor, self).perfom()

    def finalize(self):
        pass

    def some_function(self):
        print self.msg


if __name__ == '__main__':

    gf = GenericFunctor()
    gf.doc()
    gf.perform()
