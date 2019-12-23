import os
from shutil import copyfile


def build(info, site_api):
	settings = site_api.get_settings()
	with site_api.BaseHtmlHook(info['module_name']) as h:
		site_api.create_file(info, 'codeoc.html', '{}/codeoc.html'.format(settings['output_folder']))