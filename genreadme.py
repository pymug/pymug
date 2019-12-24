import site_api

import inspect
from inspect import getmembers, isfunction

functions_list = [o for o in getmembers(site_api) if isfunction(o[1])]

docs = ''
for f in functions_list:
    doc = '''
**{}({})**

```
{}
```
'''.format(
    f[0], 
    inspect.getfullargspec(f[1]),
    f[1].__doc__
    )
    docs += doc

site_api.generate('README.template', 'README.md', template_dir='.',
    api=docs)