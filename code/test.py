#mydict.py
class Dict(object):
    """docstring for Dict"""
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except Exception, e:
            raise AttributeError(r"'Dict object has no attributeError '%s'" % key
    def __setattr__(self, key, value):
        self[key] = value
