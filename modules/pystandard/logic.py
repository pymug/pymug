import os
from shutil import copyfile


def build(info, site_api):
    settings = site_api.get_settings()
    
    core_basics_html = site_api.mdtohtml('modules/{}/data/core_basics.md'.format(info['module_name']))
    site_api.create_file(
        info, 
        'pystandard.html', 
        '{}/pystandard.html'.format(settings['output_folder']),
        core_basics=core_basics_html)