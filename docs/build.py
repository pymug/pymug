from jinja2 import Environment, FileSystemLoader
import collections
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
    'detailed members':{
        'link':'menus/members_reg.html',
        'fa_class':'fa-angle-double-up'
    },
    'honorary members':{
        'link':'menus/members_hon',
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
    'about us':{
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
    'history':{
        'link':'menus/history.html',
        'fa_class':'fa-book'
    },
    'py certif standard':{
        'link':'menus/pystandard.html',
        'fa_class':'fa-file-o'
    }
}
def build_main_page():
    #generate('templates', 'index.html', 'index.html',
    #**kwargs)
    generate('templates', 'index.html', 'index.html',
        sections=sections)
    print('main page built')

def build_members_basic():
    basic_members = collections.OrderedDict()
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
            print(basic_members)
    reversed_dict = collections.OrderedDict(reversed(list(basic_members.items())))
    generate('templates', 'menus/members_basic.html', 'menus/members_basic.html',
    basic_members=reversed_dict)
    print('menus/members_basic built')

def build_register():
    generate('templates', 'menus/register.html', 'menus/register.html')
    print('menus/register built')

# build_main_page()
# build_members_basic()
build_register()
