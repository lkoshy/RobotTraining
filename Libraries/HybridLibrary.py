# 2 benefits

# use keyword decorator to mark methods that are used as key words.

class HybridLibrary:
    keywords = ['hybrid_keyword', 'external_hybrid_keyword']

    def __init__(self):
        # reference the ext lib comp class.
        self.ext_comp = ExternalLibComponent()

    # hbrid api has only this mandatory method.
    # lib must have the fn matching this keyword. robot get the refernce
    # using introspection
    def get_keyword_names(self):
        return self.keywords

    def hybrid_keyword(self):
        pass

    # any other method is not considered a kw
    def not_exposed_as_keyword(self):
        pass

    # if there are a lot of ext components, implement this method
    # its called if the lib doent have the attribute xxx xxx
    def __getattr__(self, item):
        if item not in self.keywords:
            raise AttributeError('No atrribute "{}" found'.format(item))
        return getattr(self.ext_comp, item)


class ExternalLibComponent:

    # expose this method as kw without extending the class
    def external_hybrid_keyword(self, arg):
        print('Got arg {}'.format(arg))
