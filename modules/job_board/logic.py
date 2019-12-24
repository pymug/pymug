import os
from shutil import copyfile


def build(info, site_api):
    settings = site_api.get_settings()
    
    html = site_api.mdtohtml('modules/{}/data/jobs.md'.format(info['module_name']))
    site_api.create_file(info, 'job_board.html', '{}/job_board.html'.format(settings['output_folder']),
        content=html)