import collections
import datetime
import os
import json
import random
import uuid
import logging
from os import listdir
from os.path import isfile, isdir, join
import argparse
import shutil
import importlib

from jinja2 import Environment, FileSystemLoader
import markdown
import settings

def mdtohtml(mdfile_path):
    with open(mdfile_path, encoding='utf8') as f:
        md_content = f.read()
        
    extensions = ['extra', 'smarty']
    html_content = markdown.markdown(md_content, extensions=extensions, output_format='html5')

    return html_content


def puremdtohtml(md_content):
    extensions = ['extra', 'smarty']
    html_content = markdown.markdown(md_content, extensions=extensions, output_format='html5')

    return html_content


def get_files(dir_path):
    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

    return onlyfiles


def get_folders(dir_path):
    onlyfolders = [f for f in listdir(dir_path) if isdir(join(dir_path, f))]

    return onlyfolders


def get_post_data(filepath):
    with open(filepath) as p:
        post_source = p.read()
        raw = post_source.split('++++')
        raw_info = raw[0]
        #print(raw_info)
        infos = {'mdcontent': raw[1]}
        for line in [i for i in raw_info.split('\n') if i]:
            #print(line)
            parts = line.strip().split('=')
            attr = parts[0].strip()
            value = parts[1].strip()
            infos[attr] = value
    
    return infos


def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
    except OSError:
        pass


def get_json(filepath):
    with open(filepath) as f:
        json_data = json.load(f)
    
    return json_data


def get_settings():
    
    return {
        'output_folder': settings.OUTPUT_FOLDER
    }


def generate(file_in_templates, outpath, template_dir='templates', assets_path_append='', **kwargs):
    '''
    function to render any page, given the right parameters

    template_dir - str: the templates directory
    file_in_templates - str: the file we are rendering
    outpath - str: where to write file

    -> None
    '''
    file_loader = FileSystemLoader(template_dir)
    env = Environment(loader=file_loader)
    template = env.get_template(file_in_templates)

    build_id = str(uuid.uuid4()) # to be used

    output = template.render(kwargs, year=datetime.datetime.now().year,
        build_id=build_id, assets_path_append=assets_path_append)
    print(output, file=open(outpath, 'w', encoding="utf8"))


class BaseHtmlHook():
    def __init__(self, module_name):
        self.module_name = module_name
        
    def __enter__(self):
        shutil.copyfile('templates/base.html', 'modules/{}/templates/base.html'.format(self.module_name))
    
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.remove('modules/{}/templates/base.html'.format(self.module_name))
            
    #def add_two(self):
    #    self.init_var += 2


def get_info(module_name):
    with open('modules/{}/info.json'.format(module_name)) as f:
        info = json.load(f)
    return info


def build_modules(site_api, target=None):

    if target == 'all':
        modules = [f for f in get_folders('modules/') if not f.startswith('__')]

        for module in modules:
            m = importlib.import_module('modules.{}.logic'.format(module))
            info = get_info(module)
            info['module_name'] = module
            m.build(info, site_api)
    else:
        m = importlib.import_module('modules.{}.logic'.format(target))
        info = get_info(target)
        info['module_name'] = target
        m.build(info, site_api)



def generate_sections(exclude=[]):
    sections = {}
    modules = [f for f in get_folders('modules/') if not f.startswith('__') and f not in exclude]
    for module in modules:
        name = module.replace('_', ' ')
        with open('modules/{}/info.json'.format(module)) as f:
            sections[name] = json.load(f)

    return sections


def create_file(info, file_in_templates, outpath, **kwargs):
    #(file_in_templates, outpath, template_dir='templates',
    generate(file_in_templates, outpath, **kwargs,
            template_dir='modules/{}/templates/'.format(info['module_name']), 
            page_info=info['title'], 
            sections=generate_sections(exclude=['index']))

# TODO: pass an object to build()

# menus on main page
# fa_class is the font awesome class to add
'''
sections = {
    'events': {
        'link': 'events.html',
        'fa_class': 'fa-calendar'
    },
    'blog': {
        'link': 'blog/',
        'fa_class': 'fa-pencil'
    },
    'news': {
        'link': 'news.html',
        'fa_class': 'fa-newspaper-o'
    },
    'members': {
        'link': 'members_basic.html',
        'fa_class': 'fa-angle-up'
    },
    'honorary members': {
        'link': 'members_hon.html',
        'fa_class': 'fa-star'
    },
    'register': {
        'link': 'register.html',
        'fa_class': 'fa-check'
    },
    'resources': {
        'link': 'resources.html',
        'fa_class': 'fa-leaf'
    },
    'mauritius py businesses': {
        'link': 'business.html',
        'fa_class': 'fa-certificate'
    },
    'about': {
        'link': 'about.html',
        'fa_class': 'fa-info'
    },
    'maintainers': {
        'link': 'maintainers.html',
        'fa_class': 'fa-anchor'
    },
    'partners': {
        'link': 'partners.html',
        'fa_class': 'fa-cc-paypal'
    },
    'py certif standard': {
        'link': 'pystandard.html',
        'fa_class': 'fa-file-o'
    },
    'social': {
        'link': 'social.html',
        'fa_class': 'fa-paper-plane-o'
    },
    'code of conduct': {
        'link': 'codeoc.html',
        'fa_class': 'fa-handshake-o'
    },
    'job board': {
        'link': 'job_board.html',
        'fa_class': 'fa-th-list'
    }
}
'''