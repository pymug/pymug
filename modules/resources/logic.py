import os
from shutil import copyfile


def build(info, site_api):
	settings = site_api.get_settings()
	with site_api.BaseHtmlHook(info['module_name']) as h:
		html_content = site_api.mdtohtml('modules/{}/data/resources.md'.format(info['module_name']))
		site_api.create_file(info, 'resources.html', '{}/resources.html'.format(settings['output_folder']),
			content=html_content)