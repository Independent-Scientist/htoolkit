from base.functors.functor import *
from base.functors.functor_manager import *

class GenericFunctor(Functor):

    def __init__(self):
        super(GenericFunctor, self).__init__()
        self.msg = 'Hello World'

    @functor_doc_assert
    def doc(self):
        print self.initialized
        return None

    def initialize(self, *args, **kwargs):
        print "Functor initialized ..."

    def perform(self):
        print 'Hello World!'

    def finalize(self):
        print 'Functor finalized ...'

    def some_function(self):
        print self.msg


if __name__ == '__main__':

    gf = GenericFunctor()
    FUNCTOR_MANAGER.functor_call(gf)