import json
import os
import markdown
from collections import ChainMap

OUTPUT_FOLDER = "docs/"
info = None

BLOG_CATEGORIES = os.listdir('./data/blog')

VOLUNTEERS_DESCS = {
    "event": "Events collaborator/programmer",
    "code": "Website/Projects maintainer",
    "education": "Tutorials/Posts Flask related",
}

# with open("info.json", encoding="utf-8") as f:
#     info = json.load(f)


github_usernames = [m.strip('.md') for m in os.listdir('./data/members')]
profiles = {}
for github_username in github_usernames:
    with open(f'./data/members/{github_username}.md', encoding="utf-8") as f:
        text = f.read() 
        md = markdown.Markdown(extensions=["extra", "smarty", "meta"])
        html = md.convert(text)
        metadata = md.Meta

    metadata['name'] = metadata['name'][0]
    metadata['founder'] = metadata['founder'][0]
    metadata['organiser'] = metadata['organiser'][0]
    ds = [{l.split()[0].strip(":"): l.split()[1]} for l in metadata['links'] if l.strip()]
    metadata['links'] = dict(ChainMap(*ds))

    profiles[github_username] = {'html': html, 'meta': metadata}



events = {
    "sept-2022": {
        'date': 'September 10, 2022',
        'sessions': [
        {
            'title': '',
            'description': '',
            'speaker/s': ['Abdur-RahmaanJ']
        }
        ]
    }
}



info = {
    "head": {
        "description": "Flask Community Workgroup",
        "keywords": "python, Flask, community",
        "author": "Flask Community",
        "theme-color": "#111"
    },
    "profiles": profiles,
    "events": events
}
