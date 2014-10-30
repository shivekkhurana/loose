#! /usr/bin/python


class Loose(object):

    """javascript style objects"""

    def __init__(self, obj=dict()):
        super(Loose, self).__init__()
        self.obj = obj

    def __call__(self):
        return self.__getattr__('default')()

    def __getattr__(self, method_name):
        try:
            return self.obj[method_name]
        except Exception, e:
            raise KeyError('Method [%s] not defined' % (method_name))
