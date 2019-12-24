import os
from shutil import copyfile


def build(info, site_api):
    settings = site_api.get_settings()
    
    site_api.create_file(info, 'business.html', '{}/business.html'.format(settings['output_folder']))