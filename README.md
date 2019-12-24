# pymug
website source of pymug.com - python mauritius user group

NOTE: As noted on fb and linked-in, joining our groups on social media adds you as a member on our website. Joining our groups is about commitment to Python. A personal page is created for you with your skills listed. It shows at the very least the path to learn py.

# Website
https://pymug.github.io/pymug/ or http://www.pymug.com

# Structure
the site's structure is dictated by github pages' specifications and handling rather than good standards.

an index.html in every folder, path or lib, is a brillant idea of github (really). See tutorial section below

# Activating Vitual env (Optional)

**Windows:**

Activate (from pymug/):

```
cd pymug-web/scripts/ & activate & cd ..\..
```

or just type

```
win_vactivate
```

Deactivate:

```
cd pymug-web/scripts/ & deactivate & cd ..\..
```

or just type

```
win_vdeactivate
```

# Installing dependencies (If not using venv)

```
pip install -r requirements.txt
```

# Quick start

```
python build.py all
```

to build all

else choose what section to build from: the modules folder

e.g `python build.py blog`

# Add yourself as a member

open an issue with your name,username,date in the format

name / username / date

or open a Pull Request and add your name to the bottom of the file [here](https://github.com/pymug/pymug/blob/master/docs/data/members_basic/members.txt)

# Python version 

3.7

# Tutorial


### Settings

- Output Folder
```
OUTPUT_FOLDER = 'docs'
```

The default output folder remains docs/ as github pages build as from this folder

- Included Modules

```
included_modules = [
    'blog',
    'coc',
    'events',
    'job_board',
    'index',
    'job_board',
    'members',
    'partners',
    'pystandard',
    'resources'
]
```

In `modules/` there can be as many modules as you like but they won't all be built. Only those defined in this list will be built

### Modules development

A module has the following structure. Let's take the events module:

```
events/
    data/
        events.md
    templates/
        events.html
    __init__.py
    info.json
    logic.py
```

- `data/` is used to store data files.

- `templates/` used to store templates

- `info.json` is used to hold infomations such as 

```
{
    "title": "events",
    "fa_class": "fa-calendar",
    "link": "events.html"
}
```

`fa_class` is the font awesome7 class used in the index.html to define this section

`link` is the link in index.html

- `logic.py` is used to render and write the pages.

- 'templates/events.html'

The events.html is a simple file


```
{% extends "base.html" %}

{% block content %}

    {{content}}

{% endblock %}
```


which extends base.html in our root directory

- `templates/events.md` contains what we'll render `` above

- `logic.py`

```python
def build(info, site_api):
    settings = site_api.get_settings()
    
    html = site_api.mdtohtml('modules/{}/data/events.md'.format(info['module_name']))
    site_api.create_file(info, 'events.html', '{}/events.html'.format(settings['output_folder']),
        content=html)
```

## Logic.py

As seen above, the function

```
def build(info, site_api):
```

is mandatory. info contains 

```
{
    "title": "events",
    "fa_class": "fa-calendar",
    "link": "events.html",
    "module_name": "events"
}
```

and site_api is just the site_api module

```
settings = site_api.get_settings()
```

gets the settings we defined in settings.py

```
    html = site_api.mdtohtml('modules/{}/data/events.md'.format(info['module_name']))
    site_api.create_file(info, 'events.html', '{}/events.html'.format(settings['output_folder']),
        content=html)
```

First we get the events.md file in html format

then we create a file, replacing the content in the template by the generated html

### API

`site_api` provides general utilities as well as module-info and page rendering utilities.


**build_modules(FullArgSpec(args=['site_api', 'target'], varargs=None, varkw=None, defaults=(None,), kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```

    target specifies the module to build, all builds
    all modules.
    
```

**create_file(FullArgSpec(args=['info', 'file_in_templates', 'outpath'], varargs=None, varkw='kwargs', defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
used to create file. info is get_info above
```

**create_folder(FullArgSpec(args=['folder_path'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
creates folder, ignore if folder exists
```

**generate(FullArgSpec(args=['file_in_templates', 'outpath', 'template_dir', 'assets_path_append'], varargs=None, varkw='kwargs', defaults=('templates', ''), kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
not to be used in api, the raw generate function to generate files
```

**generate_sections(FullArgSpec(args=['exclude'], varargs=None, varkw=None, defaults=([],), kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```

    goes in each module's info.json then extracts
    icon info. used to build index.html
    
```

**get_files(FullArgSpec(args=['dir_path'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
returns all files in folder path
```

**get_folders(FullArgSpec(args=['dir_path'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
returns all folders in folder path
```

**get_info(FullArgSpec(args=['module_name'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
returns a module's info.json as dictionary
```

**get_json(FullArgSpec(args=['filepath'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
given file path, returns json content as dictionary
```

**get_post_data(FullArgSpec(args=['filepath'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```

    given a blog post file path, it typically returns
    {
        'title': 'why erger ger',
        'slug': 'why-erger-ger',
        'author': 'dong',
        'time': '14-08-2019 05:10'
    }
    
```

**get_settings(FullArgSpec(args=[], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
relevent settings from the settings file
```

**isfile(FullArgSpec(args=['path'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
Test whether a path is a regular file
```

**join(FullArgSpec(args=['path'], varargs='paths', varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
None
```

**mdtohtml(FullArgSpec(args=['mdfile_path'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
returns html content given filename
```

**puremdtohtml(FullArgSpec(args=['md_content'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}))**

```
returns html content given markdown content
```






