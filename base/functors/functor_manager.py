from base.functors.functor import *


class FunctorManager(object):

    def __init__(self, *args, **kwargs):
        # initialize base
        super(FunctorManager, self).__init__()

        #properties.
        self.verbose = False

    def find_by_name(self, name):
        return ""

    def functor_call(self, fnctr, *args, **kwargs):

        result = None

        try:
            fnctr.meta()
        except FunctorImplException as e:
            print e.message
            return

        try:
            fnctr.initialize(*args, **kwargs)
        except FunctorImplException as e:
            print e.message
            return
        try:
            result = fnctr.perform()
        except Exception as e:
            print e.message
            return

        try:
            fnctr.finalize()
        except Exception as e:
            print e.message
            return

        return result

    def functor_call_by_name(self, name, *args, **kwargs):

        fnctr = self.find_by_name(name)
        self.functor_call(fnctr, *args, **kwargs)



FUNCTOR_MANAGER = FunctorManager()