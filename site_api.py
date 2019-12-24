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
    '''returns html content given filename'''

    with open(mdfile_path, encoding='utf8') as f:
        md_content = f.read()
        
    extensions = ['extra', 'smarty']
    html_content = markdown.markdown(md_content, extensions=extensions, output_format='html5')

    return html_content


def puremdtohtml(md_content):
    '''returns html content given markdown content'''

    extensions = ['extra', 'smarty']
    html_content = markdown.markdown(md_content, extensions=extensions, output_format='html5')

    return html_content


def get_files(dir_path):
    '''returns all files in folder path'''

    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

    return onlyfiles


def get_folders(dir_path):
    '''returns all folders in folder path'''

    onlyfolders = [f for f in listdir(dir_path) if isdir(join(dir_path, f))]

    return onlyfolders


def get_post_data(filepath):
    '''
    given a blog post file path, it typically returns
    {
        'title': 'why erger ger',
        'slug': 'why-erger-ger',
        'author': 'dong',
        'time': '14-08-2019 05:10'
    }
    '''

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
    '''creates folder, ignore if folder exists'''

    try:
        os.mkdir(folder_path)
    except OSError:
        pass


def get_json(filepath):
    '''given file path, returns json content as dictionary'''

    with open(filepath) as f:
        json_data = json.load(f)
    
    return json_data


def get_settings():
    '''relevent settings from the settings file'''

    return {
        'output_folder': settings.OUTPUT_FOLDER
    }


def generate(file_in_templates, outpath, template_dir='templates', assets_path_append='', **kwargs):
    '''not to be used in api, the raw generate function to generate files'''

    file_loader = FileSystemLoader(template_dir)
    env = Environment(loader=file_loader)
    template = env.get_template(file_in_templates)

    build_id = str(uuid.uuid4()) # to be used

    output = template.render(kwargs, year=datetime.datetime.now().year,
        build_id=build_id, assets_path_append=assets_path_append)
    print(output, file=open(outpath, 'w+', encoding="utf8"))


def get_info(module_name):
    '''returns a module's info.json as dictionary'''

    with open('modules/{}/info.json'.format(module_name)) as f:
        info = json.load(f)
    
    return info


class BaseHtmlHook():
    '''
    not to be used as api. used as context manager.
    implements the hack that allows templates files 
    to be in modules while the base file is outside

    it copies the base.html each time to the module's
    templates folder. then remove it after rendering.
    '''

    def __init__(self, module_name):
        self.module_name = module_name
        
    def __enter__(self):
        shutil.copyfile('templates/base.html', 'modules/{}/templates/base.html'.format(self.module_name))
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.remove('modules/{}/templates/base.html'.format(self.module_name))


def build_modules(site_api, target=None):
    '''
    target specifies the module to build, all builds
    all modules.
    '''

    if target == 'all':
        modules = [f for f in get_folders('modules/') if not f.startswith('__')]

        for module in modules:
            m = importlib.import_module('modules.{}.logic'.format(module))
            info = get_info(module)
            info['module_name'] = module
            with site_api.BaseHtmlHook(info['module_name']) as h:
                m.build(info, site_api)
    else:
        m = importlib.import_module('modules.{}.logic'.format(target))
        info = get_info(target)
        info['module_name'] = target
        with site_api.BaseHtmlHook(info['module_name']) as h:
            m.build(info, site_api)



def generate_sections(exclude=[]):
    '''
    goes in each module's info.json then extracts
    icon info. used to build index.html
    '''

    sections = {}
    modules = [f for f in get_folders('modules/') if not f.startswith('__') and f not in exclude]
    for module in modules:
        name = module.replace('_', ' ')
        with open('modules/{}/info.json'.format(module)) as f:
            sections[name] = json.load(f)

    return sections


def create_file(info, file_in_templates, outpath, **kwargs):
    '''used to create file. info is get_info above'''

    generate(file_in_templates, outpath, **kwargs,
            template_dir='modules/{}/templates/'.format(info['module_name']), 
            page_info=info['title'], 
            sections=generate_sections(exclude=['index']))

# TODO: pass an object to build()

# menus on main page
# fa_class is the font awesome class to add
