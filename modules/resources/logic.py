import os
from shutil import copyfile


def build(info, site_api):
    settings = site_api.get_settings()
    
    md_path = 'modules/{}/data/resources.md'.format(info['module_name'])
    html_content = site_api.mdtohtml(md_path)
    site_api.create_file(
        info, 
        'resources.html', 
        '{}/resources.html'.format(settings['output_folder']),
        content=html_content)