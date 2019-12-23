import os
from shutil import copyfile


def build(info, site_api):
	settings = site_api.get_settings()
	with site_api.BaseHtmlHook(info['module_name']) as h:
		html = site_api.mdtohtml('modules/{}/data/events.md'.format(info['module_name']))
		site_api.create_file(info, 'events.html', '{}/events.html'.format(settings['output_folder']),
			content=html)