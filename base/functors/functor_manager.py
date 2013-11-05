from base.functors.functor import *


class FunctorManager(object):

    def find_by_name(self, name):
        pass

    def functor_call(self, fnctr, *args, **kwargs):

        try:
            fnctr.initialize(*args, **kwargs)
        except FunctorImplException as e:
            print e.message

        try:
            result = fnctr.perfom()
        except Exception as e:
            print e.message

        try:
            fnctr.finalize()
        except Exception as e:
            print e.message

        return result

    def functor_call_by_name(self, name, *args, **kwargs):

        find_



