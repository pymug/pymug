from jinja2 import Environment, FileSystemLoader
import collections
import datetime
import os
import json
import random


def generate(template_dir, file_in_templates, outpath, **kwargs):
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

    output = template.render(kwargs)
    print(output, file=open(outpath, 'w'))


# menus on main page
# fa_class is the font awesome class to add
sections = {
    'events': {
        'link': 'menus/events.html',
        'fa_class': 'fa-calendar'
    },
    'news': {
        'link': 'menus/news.html',
        'fa_class': 'fa-newspaper-o'
    },
    'members': {
        'link': 'menus/members_basic.html',
        'fa_class': 'fa-angle-up'
    },
    'honorary members': {
        'link': 'menus/members_hon.html',
        'fa_class': 'fa-star'
    },
    'register': {
        'link': 'menus/register.html',
        'fa_class': 'fa-check'
    },
    'resources': {
        'link': 'menus/resources.html',
        'fa_class': 'fa-leaf'
    },
    'mauritius py businesses': {
        'link': 'menus/business.html',
        'fa_class': 'fa-certificate'
    },
    'about': {
        'link': 'menus/about.html',
        'fa_class': 'fa-info'
    },
    'maintainers': {
        'link': 'menus/maintainers.html',
        'fa_class': 'fa-anchor'
    },
    'sponsors': {
        'link': 'menus/sponsors.html',
        'fa_class': 'fa-cc-paypal'
    },
    'py certif standard': {
        'link': 'menus/pystandard.html',
        'fa_class': 'fa-file-o'
    },
    'blog': {
        'link': 'menus/blog.html',
        'fa_class': 'fa-pencil'
    },
    'social': {
        'link': 'menus/social.html',
        'fa_class': 'fa-paper-plane-o'
    },
    'code of conduct': {
        'link': 'menus/codeoc.html',
        'fa_class': 'fa-handshake-o'
    }
}


def build_main_page():
    '''
    builds index.html

    -> None
    '''
    generate(
        'templates', 'index.html', 'index.html', sections=sections,
        year=datetime.datetime.now().year)
    print('main page built')


def build_members_basic():
    '''
    builds members page with link

    converts members.txt to
    {
        'appinv':{
            'name':'...',
            'date':''
        }
    }

    -> None
    '''
    basic_members = {}
    with open('data/members_basic/members.txt', encoding="utf-8") as memfile:
        infos = [m for m in memfile.read().splitlines() if m]
        random.shuffle(infos)
        for i, info in enumerate(infos):
            data = [x.strip() for x in info.split('/')]
            name = data[0]
            uname = data[1]
            date = data[2]
            print(name)
            basic_members[uname] = {
                'index': i+1,
                'name': name,
                'date': date
            }
        # print(basic_members)
    # reversed_dict = collections.OrderedDict(reversed(list(basic_members.items())))
    generate(
        'templates', 'menus/members_basic.html', 'menus/members_basic.html',
        basic_members=basic_members, sections=sections,
        page_info='basic members', year=datetime.datetime.now().year)
    print('menus/members_basic built')


def build_register():
    '''
    builds register info page

    -> None
    '''
    generate(
        'templates', 'menus/register.html', 'menus/register.html',
        sections=sections,
        page_info='register', year=datetime.datetime.now().year)
    print('menus/register built')


def build_about():
    '''
    builds about page

    -> None
    '''
    generate(
        'templates', 'menus/about.html', 'menus/about.html',
        sections=sections,
        page_info='about', year=datetime.datetime.now().year)
    print('menus/about built')


def build_pystandard():
    '''
    builds py standard

    -> None
    '''
    files = ['core_basics']
    read_files = {}
    for file in files:
        with open('data/standard/{}.txt'.format(file), 'r') as stdfile:
            read_file = stdfile.read()
            print(read_file.count('\n'))
            read_file = '' + read_file.replace('\n', '<hr>')
            read_files[file] = read_file
    generate(
        'templates', 'menus/pystandard.html', 'menus/pystandard.html',
        sections=sections, read_files=read_files,
        page_info='certification standard', year=datetime.datetime.now().year)
    print('menus/pystandard built')


def build_blog():
    '''
    builds blog page

    -> None
    '''
    generate(
        'templates', 'menus/blog.html', 'menus/blog.html',
        sections=sections,
        page_info='blog', year=datetime.datetime.now().year)
    print('menus/blog built')


def build_business():
    '''
    builds business using py page

    -> None
    '''
    generate(
        'templates', 'menus/business.html', 'menus/business.html',
        sections=sections,
        page_info='business', year=datetime.datetime.now().year)
    print('menus/business built')


def build_members_hon():
    '''
    builds honorary members page

    -> None
    '''
    generate(
        'templates', 'menus/members_hon.html', 'menus/members_hon.html',
        sections=sections,
        page_info='honorary members', year=datetime.datetime.now().year)
    print('menus/members_hon built')


def build_news():
    '''
    build news page

    -> None
    '''
    generate(
        'templates', 'menus/news.html', 'menus/news.html',
        sections=sections,
        page_info='news', year=datetime.datetime.now().year)
    print('menus/news built')


def build_social():
    '''
    builds social media page

    -> None
    '''
    generate(
        'templates', 'menus/social.html', 'menus/social.html',
        sections=sections,
        page_info='social', year=datetime.datetime.now().year)
    print('menus/social built')


def build_resources():
    '''
    builds python resources pages

    -> None
    '''
    generate(
        'templates', 'menus/resources.html', 'menus/resources.html',
        sections=sections,
        page_info='resources', year=datetime.datetime.now().year)
    print('menus/resources built')


def build_sponsors():
    '''
    builds sponsors page

    -> None
    '''
    generate(
        'templates', 'menus/sponsors.html', 'menus/sponsors.html',
        sections=sections,
        page_info='sponsors', year=datetime.datetime.now().year)
    print('menus/sponsors built')


def build_events():
    '''
    builds events page

    -> None
    '''
    generate(
        'templates', 'menus/events.html', 'menus/events.html',
        sections=sections,
        page_info='events', year=datetime.datetime.now().year)
    print('menus/events built')


def build_maintainers():
    '''
    build maintainers/organisers page

    -> None
    '''
    generate(
        'templates', 'menus/maintainers.html', 'menus/maintainers.html',
        sections=sections,
        page_info='maintainers', year=datetime.datetime.now().year)
    print('menus/maintainers built')


def build_codeoc():
    '''
    builds code of conduct page

    -> None
    '''
    generate(
        'templates', 'menus/codeoc.html', 'menus/codeoc.html',
        sections=sections,
        page_info='code of conduct', year=datetime.datetime.now().year)
    print('menus/codeoc built')


def build_all_members():
    '''
    builds all personal members pages

    -> None
    '''
    def build_member_page(uname, meminfo):
        '''
        builds a single member page

        uname - str: username
        meminfo - str: member info
        -> None
        '''
        levels = {
            0: 'beginner',
            1: 'initiate',
            2: 'path cruiser',
            3: 'sage',
            4: 'master'
        }
        generate(
            'templates', 'members/member_page.html', 'members/{}/index.html'.format(uname),
            sections=sections, meminfo=meminfo, levels=levels,
            page_info=uname, year=datetime.datetime.now().year)
        print('members/{} built'.format(uname))

    meminfo = {}

    with open('data/members_basic/members.txt', encoding="utf-8") as memfile:
        infos = [m for m in memfile.read().splitlines() if m]
        for i, info in enumerate(infos):
            data = [x.strip() for x in info.split('/')]
            name = data[0]
            uname = data[1]
            date = data[2]
            # ensures folder existence
            try:  # nice piece taken from flask source code
                os.makedirs('members/'+uname)
            except OSError:
                pass
            # create data file in folder
            fpath = 'members/{uname}/{uname}.json'.format(uname=uname)
            if os.path.isfile(fpath):
                pass
            else:
                generate(
                    'templates', 'members.json',
                    'members/{uname}/{uname}.json'.format(uname=uname),
                    sections=sections,
                    info={'name': name, 'date': date, 'uname': uname})
            # use data file to generate member page
            with open('members/{uname}/{uname}.json'.format(uname=uname)) as data_file:
                meminfo = json.load(data_file)
            build_member_page(uname, meminfo)
            # reset
            meminfo = {}
    print('all members built')


def build_all():
    build_main_page()
    build_members_basic()
    build_register()
    build_about()
    build_pystandard()
    build_blog()
    build_business()
    build_members_hon()
    build_news()
    build_social()
    build_resources()
    build_sponsors()
    build_events()
    build_maintainers()
    build_codeoc()
    build_all_members()


if __name__ == '__main__':
    # build_main_page()
    # build_members_basic()
    # build_register()
    # build_about()
    # build_pystandard()
    build_all()
