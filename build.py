import collections
import datetime
import os
import json
import random
import uuid
import logging


from jinja2 import Environment, FileSystemLoader
import markdown


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger('pymug-website')
build_id = str(uuid.uuid4()) # to be used


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
    print(output, file=open(outpath, 'w', encoding="utf8"))


# menus on main page
# fa_class is the font awesome class to add
sections = {
    'events': {
        'link': 'events.html',
        'fa_class': 'fa-calendar'
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
    'blog': {
        'link': 'blog.html',
        'fa_class': 'fa-pencil'
    },
    'social': {
        'link': 'social.html',
        'fa_class': 'fa-paper-plane-o'
    },
    'code of conduct': {
        'link': 'codeoc.html',
        'fa_class': 'fa-handshake-o'
    }
}


def build_main_page():
    '''
    builds index.html

    -> None
    '''
    generate(
        'templates', 'index.html', 'docs/index.html', sections=sections,
        year=datetime.datetime.now().year)
    logger.info('main page built')


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
    with open('docs/data/members_basic/members.txt', encoding="utf-8") as memfile:
        infos = [m for m in memfile.read().splitlines() if m]
        random.shuffle(infos)
        for i, info in enumerate(infos):
            data = [x.strip() for x in info.split('/')]
            name = data[0]
            uname = data[1]
            date = data[2]
            logger.info(name)
            basic_members[uname] = {
                'index': i+1,
                'name': name,
                'date': date
            }
        # logger.info(basic_members)
    # reversed_dict = collections.OrderedDict(reversed(list(basic_members.items())))
    generate(
        'templates', 'menus/members_basic.html', 'docs/members_basic.html',
        basic_members=basic_members, sections=sections,
        page_info='basic members', year=datetime.datetime.now().year)
    logger.info('menus/members_basic built')


def build_register():
    '''
    builds register info page

    -> None
    '''
    generate(
        'templates', 'menus/register.html', 'docs/register.html',
        sections=sections,
        page_info='register', year=datetime.datetime.now().year)
    logger.info('menus/register built')


def build_about():
    '''
    builds about page

    -> None
    '''
    generate(
        'templates', 'menus/about.html', 'docs/about.html',
        sections=sections,
        page_info='about', year=datetime.datetime.now().year)
    logger.info('menus/about built')


def build_pystandard():
    '''
    builds py standard

    -> None
    '''
    files = ['core_basics']
    read_files = {}
    for file in files:
        with open('docs/data/standard/{}.txt'.format(file), 'r') as stdfile:
            read_file = stdfile.read()
            logger.info(read_file.count('\n'))
            read_file = '' + read_file.replace('\n', '<hr>')
            read_files[file] = read_file
    generate(
        'templates', 'menus/pystandard.html', 'docs/pystandard.html',
        sections=sections, read_files=read_files,
        page_info='certification standard', year=datetime.datetime.now().year)
    logger.info('menus/pystandard built')


def build_blog():
    '''
    builds blog page

    -> None
    '''
    generate(
        'templates', 'menus/blog.html', 'docs/blog.html',
        sections=sections,
        page_info='blog', year=datetime.datetime.now().year)
    logger.info('menus/blog built')


def build_business():
    '''
    builds business using py page

    -> None
    '''
    generate(
        'templates', 'menus/business.html', 'docs/business.html',
        sections=sections,
        page_info='business', year=datetime.datetime.now().year)
    logger.info('menus/business built')


def build_members_hon():
    '''
    builds honorary members page

    -> None
    '''
    generate(
        'templates', 'menus/members_hon.html', 'docs/members_hon.html',
        sections=sections,
        page_info='honorary members', year=datetime.datetime.now().year)
    logger.info('menus/members_hon built')


def build_news():
    '''
    build news page

    -> None
    '''
    generate(
        'templates', 'menus/news.html', 'docs/news.html',
        sections=sections,
        page_info='news', year=datetime.datetime.now().year)
    logger.info('menus/news built')


def build_social():
    '''
    builds social media page

    -> None
    '''
    generate(
        'templates', 'menus/social.html', 'docs/social.html',
        sections=sections,
        page_info='social', year=datetime.datetime.now().year)
    logger.info('menus/social built')


def build_resources():
    '''
    builds python resources pages

    -> None
    '''
    resources_md = None
    with open('docs/data/resources.md', encoding='utf8') as f:
        resources_md = f.read()
    extensions = ['extra', 'smarty']
    resources_html = markdown.markdown(resources_md, extensions=extensions, output_format='html5')
    generate(
        'templates', 'menus/resources.html', 'docs/resources.html',
        sections=sections,
        page_info='resources', year=datetime.datetime.now().year, resources=resources_html)
    logger.info('menus/resources built')


def build_partners():
    '''
    builds partners page

    -> None
    '''
    with open('docs/data/partners/partners.json') as partnersFile:
        partners = json.load(partnersFile)
    generate(
        'templates', 'menus/partners.html', 'docs/partners.html',
        sections=sections, partners = partners['partners'],
        page_info='partners', year=datetime.datetime.now().year)
    logger.info('menus/partners built')


def build_events():
    '''
    builds events page

    -> None
    '''
    events_md = None
    with open('docs/data/events.md', encoding='utf8') as f:
        events_md = f.read()
    extensions = ['extra', 'smarty']
    events_html = markdown.markdown(events_md, extensions=extensions, output_format='html5')
    generate(
        'templates', 'menus/events.html', 'docs/events.html',
        sections=sections,
        page_info='events', year=datetime.datetime.now().year, events=events_html)
    logger.info('menus/events built')


def build_maintainers():
    '''
    build maintainers/organisers page

    -> None
    '''
    generate(
        'templates', 'menus/maintainers.html', 'docs/maintainers.html',
        sections=sections,
        page_info='maintainers', year=datetime.datetime.now().year)
    logger.info('menus/maintainers built')


def build_codeoc():
    '''
    builds code of conduct page

    -> None
    '''
    generate(
        'templates', 'menus/codeoc.html', 'docs/codeoc.html',
        sections=sections,
        page_info='code of conduct', year=datetime.datetime.now().year)
    logger.info('menus/codeoc built')


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
            'templates', 'members/member_page.html', 'docs/members/{}/index.html'.format(uname),
            sections=sections, meminfo=meminfo, levels=levels,
            page_info=uname, year=datetime.datetime.now().year)
        logger.info('members/{} built'.format(uname))

    meminfo = {}

    with open('docs/data/members_basic/members.txt', encoding="utf-8") as memfile:
        infos = [m for m in memfile.read().splitlines() if m]
        for i, info in enumerate(infos):
            data = [x.strip() for x in info.split('/')]
            name = data[0]
            uname = data[1]
            date = data[2]
            # ensures folder existence
            try:  # nice piece taken from flask source code
                os.makedirs('docs/members/'+uname)
            except OSError:
                pass
            # create data file in folder
            fpath = 'docs/members/{uname}/{uname}.json'.format(uname=uname)
            if os.path.isfile(fpath):
                pass
            else:
                generate(
                    'templates', 'members.json',
                    'docs/members/{uname}/{uname}.json'.format(uname=uname),
                    sections=sections,
                    info={'name': name, 'date': date, 'uname': uname})
            # use data file to generate member page
            with open('docs/members/{uname}/{uname}.json'.format(uname=uname)) as data_file:
                meminfo = json.load(data_file)
            build_member_page(uname, meminfo)
            # reset
            meminfo = {}
    logger.info('all members built')


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
    build_partners()
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
