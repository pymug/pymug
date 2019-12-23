import argparse
import warnings

import site_api


modules = site_api.get_folders('modules')
modules.append('all')

parser = argparse.ArgumentParser()
parser.add_argument("module", help="Choose 'all' or a module from :\n" + ', '.join(modules))
args = parser.parse_args()


if args.module in modules:
    site_api.build_modules(site_api, target=args.module)
else:
    warnings.warn('module not found')


