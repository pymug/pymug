
from jinja2 import Environment, FileSystemLoader

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
    'registered members':{
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
        'link':'menus/certifstandard.html',
        'fa_class':'fa-file-o'
    }
}
def run_main_page(**kwargs):
    generate('templates', 'index.html', 'index.html',
    **kwargs)

run_main_page(sections=sections)
