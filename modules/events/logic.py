

def build(info, site_api):
    settings = site_api.get_settings()
    
    html = site_api.mdtohtml('modules/{}/data/events.md'.format(info['module_name']))
    site_api.create_file(info, 'events.html', '{}/events.html'.format(settings['output_folder']),
        content=html)