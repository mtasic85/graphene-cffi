__all__ = ['graphene', 'Graphene']

from _graphene_cffi import ffi as _graphene_ffi
graphene = _graphene_ffi.dlopen('libgraphene-1.0.so')

class GrapheneClass(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        func_name = 'graphene_{}_{}'.format(self.name, attr)
        func = getattr(graphene, func_name)
        return func

class GrapheneModule(object):
    def __init__(self):
        self.cls_cache = {}

    def __getattr__(self, attr):
        try:
            g_cls = self.cls_cache[attr]
        except KeyError as e:
            g_cls = GrapheneClass(attr)
            self.cls_cache[attr] = g_cls

        return g_cls

Graphene = GrapheneModule()
