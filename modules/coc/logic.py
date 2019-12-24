import os
from shutil import copyfile


def build(info, site_api):
    settings = site_api.get_settings()
    
    site_api.create_file(info, 'codeoc.html', '{}/codeoc.html'.format(settings['output_folder']))