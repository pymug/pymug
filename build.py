import argparse
import warnings
import settings
import site_api


#modules = site_api.get_folders('modules')
#modules.append('all')

modules = settings.included_modules
args_to_check = modules + ['all']

parser = argparse.ArgumentParser()
parser.add_argument("module", help="Choose 'all' or a module from :\n" + ', '.join(modules))
args = parser.parse_args()


if args.module in args_to_check:
    site_api.build_modules(site_api, target=args.module)
else:
    tab = '    '
    available_modules = [m for m in site_api.get_folders('modules') if not m.startswith('__')]

    more_available = set(available_modules) - set(modules)
    available_module_message = ''
    if more_available:
        available_module_message = (
'''
more available modules:
    {}
''').format('\n    '.join(more_available))

    message = ('Module not found.\n\n'
                'included modules: \n'
                '{}\n'
                '{}\n'
                'and "all" to build all modules').format(
                    '    ' + '\n    '.join(modules), 
                    available_module_message)
    warnings.warn(message)


