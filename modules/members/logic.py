import os
from shutil import copyfile
import random

def build(info, site_api):
    settings = site_api.get_settings()
    
    pymug_members = {}
    data_file_path = 'modules/{}/data/members.txt'.format(info['module_name'])
    
    with open(data_file_path, encoding="utf-8") as memfile:
        infos = [m for m in memfile.read().splitlines() if m]
        random.shuffle(infos)
        for i, member_info in enumerate(infos):
            data = [x.strip() for x in member_info.split('/')]

            name = data[0].strip()
            uname = data[1].strip()
            date = data[2]
            pymug_members[uname] = {
                'index': i+1,
                'name': name,
                'date': date
            }
            site_api.create_folder('{}/members/{}'.format(
                settings['output_folder'], uname))

            # create member json file
            site_api.create_file(
                info, 
                'member.json', 
                '{0}/members/{1}/{1}.json'.format(settings['output_folder'], uname),
                user_info={'name':name, 'uname':uname, 'date':date})

            # create member page based on json
            meminfo = site_api.get_json('{out_folder}/members/{uname}/{uname}.json'.format(out_folder=settings['output_folder'], uname=uname))
            site_api.create_file(
                info, 
                'member_page.html', 
                '{0}/members/{1}/index.html'.format(settings['output_folder'], uname),
                meminfo=meminfo,
                assets_path_append='../../')

    site_api.create_folder('{}/members'.format(settings['output_folder']))
    site_api.create_file(info, 
        'members.html', 
        '{}/members/index.html'.format(settings['output_folder']),
        members=pymug_members,
        assets_path_append='../')