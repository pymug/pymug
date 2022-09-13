import json
import os
import markdown
from collections import ChainMap

OUTPUT_FOLDER = "docs/"
info = None

BLOG_CATEGORIES = os.listdir('./data/blog')

VOLUNTEERS_DESCS = {

}

# with open("info.json", encoding="utf-8") as f:
#     info = json.load(f)

def user_sessions(events, username):
    user_sessions = []
    for event_slug in events:
        data = {'slug': event_slug, 'sessions': []}
        for session in events[event_slug]['sessions']:
            if username in session['speaker/s']:
                data['sessions'].append(session)
        user_sessions.append(data)
    return user_sessions


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
    metadata['honorary'] = metadata['honorary'][0]
    ds = [{l.split()[0].strip(":"): l.split()[1]} for l in metadata['links'] if l.strip()]
    metadata['links'] = dict(ChainMap(*ds))

    profiles[github_username] = {'html': html, 'meta': metadata}



events = {
    "sept-2022": {
        "title": "Python Meetup Sept 2022",
        "venue": "MakerSpace, Vacoas",
        'date': 'September 10, 2022',
        'raw_html': '<iframe src="https://docs.google.com/document/d/e/2PACX-1vQOVrBNTE3_B1nXySeUT4fxUSumldjmjadp5Zd0mq5JuuBTPN5sJ3YQ6qSbeMSyxvE4c963iJxx1GBl/pub?embedded=true" style="width: 100%; height: 500px;"></iframe>',
        "attendees": {'reg': 18, 'came':11},
        'register': 'https://www.meetup.com/pymauritius/events/287733145/',
        'sessions': [ 
        {
            'title': 'Create Machine Learning projects/demos with Python',
            'info': 'Show how to create simple ML projects/demos using open-source models on HuggingFace and Gradio as interface.',
            'speaker/s': ['azezezaaa'],
            'presented': 1,
            'remote': 0
        }, 
        {
            'title': 'Generating Unique & Distinct Sortable IDs for Your Use',
            'info': 'With this, one can generate unique sortable integer ID. These IDs will not clash once the conditions are right. Learn how to achieve same.',
            'speaker/s': ['ichux'],
            'presented': 1,
            'remote': 1
        },
        {
            'title': 'Maths via Creative Coding with Python',
            'info': 'I tutor kids in maths via creative coding, using Python and drawing libraries, and I would like to share about it in a short talk.',
            'speaker/s': ['AkashaRojee'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Deep Regex With Python',
            'info': 'Extracts from my regex engine works',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Useful GUIs',
            'info': 'How Gui dev can help',
            'speaker/s': ['nam4dev'],
            'presented': 0,
            'remote': 0 
        }
        ], 
    }
}



info = {
    "head": {
        "description": "Python events in Mauritius",
        "keywords": "python, mauritius, community",
        "author": "Python Community",
        "theme-color": "#111"
    },
    "profiles": profiles,
    "events": events
}
