import os
from shutil import copyfile


def build(info, site_api):
    settings = site_api.get_settings()
    
    partners_json = site_api.get_json('modules/{}/data/partners.json'.format(info['module_name']))
    site_api.create_file(info, 'partners.html', '{}/partners.html'.format(settings['output_folder']),
        partners=partners_json)