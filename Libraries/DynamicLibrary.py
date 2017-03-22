class DynamicLibrary:

    # mandatory method1 of dynamic APIs
    # it returns a list of robot kws
    def get_keyword_names(self):
        return ['Dynamic keyword', 'Keyword with arguments']

    # mandatory method2 of dynamic APIs. this method is run when the kw is called.
    # name : name of the kw
    def run_keyword(self, name, args):
        print('Executing keyword {} with arguments {}'.format(name, args))

    # optional method in the dynamic api
    def get_keyword_arguments(self, name):
        # called by robot
        return ['arg1', 'arg2=default', 'arg3=default 2'] if name == 'Keyword with arguments' else []

    # optional method in dy api. just to create valid libdoc documents. doesnt affect test execution
    def get_keyword_documentation(self, name):
        return 'Documentation of keyword "{}".'.format(name)


