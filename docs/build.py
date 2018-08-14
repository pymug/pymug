from jinja2 import Environment, FileSystemLoader
import collections
import datetime
'''
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('test.html')

output = template.render(colors=['red','blue','yellow'])
print(output, file=open('templates/output/test.html', 'w'))
'''


def generate(template_dir, file_in_templates, outpath, 
    **kwargs):
    file_loader = FileSystemLoader(template_dir)
    env = Environment(loader=file_loader)
    template = env.get_template(file_in_templates)

    output = template.render(kwargs)
    print(output, file=open(outpath, 'w'))

sections = {
    'events':{
        'link':'menus/events.html',
        'fa_class':'fa-calendar'
    },
    'news':{
        'link':'menus/news.html',
        'fa_class':'fa-newspaper-o'
    },
    'basic members':{
        'link':'menus/members_basic.html',
        'fa_class':'fa-angle-up'
    },
    'evaluated members':{
        'link':'menus/members_eval.html',
        'fa_class':'fa-angle-double-up'
    },
    'honorary members':{
        'link':'menus/members_hon.html',
        'fa_class':'fa-star'
    },
    'register':{
        'link':'menus/register.html',
        'fa_class':'fa-check'
    },
    'resources':{
        'link':'menus/resources.html',
        'fa_class':'fa-leaf'
    },
    'mauritius py businesses':{
        'link':'menus/business.html',
        'fa_class':'fa-certificate'
    },
    'about':{
        'link':'menus/about.html',
        'fa_class':'fa-info'
    },
    'maintainers':{
        'link':'menus/maintainers.html',
        'fa_class':'fa-anchor'
    },
    'sponsors':{
        'link':'menus/sponsors.html',
        'fa_class':'fa-cc-paypal'
    },
    'py certif standard':{
        'link':'menus/pystandard.html',
        'fa_class':'fa-file-o'
    },
    'blog':{
        'link':'menus/blog.html',
        'fa_class':'fa-pencil'
    },
    'social':{
        'link':'menus/social.html',
        'fa_class':'fa-paper-plane-o'
    },
    'code of conduct':{
        'link':'menus/codeoc.html',
        'fa_class':'fa-handshake-o'
    }
}
def build_main_page():
    #generate('templates', 'index.html', 'index.html',
    #**kwargs)
    generate('templates', 'index.html', 'index.html',
        sections=sections, year=datetime.datetime.now().year)
    print('main page built')

def build_members_basic():
    # basic_members = collections.OrderedDict()
    basic_members = {}
    '''
    {
        'appinv':{
            'name':'...',
            'date':''
        }
    }
    '''
    with open('data/members_basic/members.txt', 'r') as memfile:
        infos = memfile.read().splitlines()
        for i,info in enumerate(infos):
            data = [x.strip() for x in info.split('/')]
            name = data[0]
            uname = data[1]
            date = data[2]
            basic_members[uname] = {
                'index':i+1,
                'name':name,
                'date':date
            }
        # print(basic_members)
    
    # reversed_dict = collections.OrderedDict(reversed(list(basic_members.items())))
    generate('templates', 'menus/members_basic.html', 'menus/members_basic.html',
    basic_members=basic_members, sections=sections, 
    page_info='basic members', year=datetime.datetime.now().year)
    print('menus/members_basic built')

def build_register():
    generate('templates', 'menus/register.html', 'menus/register.html',
        sections=sections, 
        page_info='register', year=datetime.datetime.now().year)
    print('menus/register built')

def build_about():
    generate('templates', 'menus/about.html', 'menus/about.html',
        sections=sections, 
        page_info='about', year=datetime.datetime.now().year)
    print('menus/about built')

def build_pystandard():
    generate('templates', 'menus/pystandard.html', 'menus/pystandard.html',
        sections=sections, 
        page_info='certification standard', year=datetime.datetime.now().year)
    print('menus/pystandard built')

def build_blog():
    generate('templates', 'menus/blog.html', 'menus/blog.html',
        sections=sections, 
        page_info='blog', year=datetime.datetime.now().year)
    print('menus/blog built')

def build_business():
    generate('templates', 'menus/business.html', 'menus/business.html',
        sections=sections, 
        page_info='business', year=datetime.datetime.now().year)
    print('menus/business built')

def build_members_eval():
    generate('templates', 'menus/members_eval.html', 'menus/members_eval.html',
        sections=sections, 
        page_info='evaluated members', year=datetime.datetime.now().year)
    print('menus/members_eval built')

def build_members_hon():
    generate('templates', 'menus/members_hon.html', 'menus/members_hon.html',
        sections=sections, 
        page_info='honorary members', year=datetime.datetime.now().year)
    print('menus/members_hon built')

def build_news():
    generate('templates', 'menus/news.html', 'menus/news.html',
        sections=sections, 
        page_info='news', year=datetime.datetime.now().year)
    print('menus/news built')

def build_social():
    generate('templates', 'menus/social.html', 'menus/social.html',
        sections=sections, 
        page_info='social', year=datetime.datetime.now().year)
    print('menus/social built')

def build_resources():
    generate('templates', 'menus/resources.html', 'menus/resources.html',
        sections=sections, 
        page_info='resources', year=datetime.datetime.now().year)
    print('menus/resources built')

def build_sponsors():
    generate('templates', 'menus/sponsors.html', 'menus/sponsors.html',
        sections=sections, 
        page_info='sponsors', year=datetime.datetime.now().year)
    print('menus/sponsors built')

def build_events():
    generate('templates', 'menus/events.html', 'menus/events.html',
        sections=sections, 
        page_info='events', year=datetime.datetime.now().year)
    print('menus/events built')

def build_maintainers():
    generate('templates', 'menus/maintainers.html', 'menus/maintainers.html',
        sections=sections, 
        page_info='maintainers', year=datetime.datetime.now().year)
    print('menus/maintainers built')

def build_codeoc():
    generate('templates', 'menus/codeoc.html', 'menus/codeoc.html',
        sections=sections, 
        page_info='code of conduct', year=datetime.datetime.now().year)
    print('menus/codeoc built')

def build_all():
    build_main_page()
    build_members_basic()
    build_register()
    build_about()
    build_pystandard()
    build_blog()
    build_business()
    build_members_eval()
    build_members_hon()
    build_news()
    build_social()
    build_resources()
    build_sponsors()
    build_events()
    build_maintainers()
    build_codeoc()

if __name__ == '__main__':
    # build_main_page()
    # build_members_basic()
    # build_register()
    # build_about()
    # build_pystandard()
    build_all()
