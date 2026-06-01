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
    is_speaker = False
    for event_slug in events:
        data = {'slug': event_slug, 'sessions': []}
        for session in events[event_slug]['sessions']:
            if username in session['speaker/s']:
                is_speaker = True
                data['sessions'].append(session)
        user_sessions.append(data)
    return user_sessions, is_speaker


def parse_skill(skill):
    s = skill.split(':')
    level = s[1]
    skill = s[0]

    level_map = {
        '0': 'used it once',
        '1': 'usage proficiency',
        '2': 'professional experience',
        '3': 'expert'
    }

    return skill, level_map[level]

github_usernames = [m[:-3] for m in os.listdir('./data/members')]
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

    try:
        metadata['skills'] = [s for s in metadata['skills'] if s.strip()]
    except KeyError:
        metadata['skills'] = []
    profiles[github_username] = {'html': html, 'meta': metadata}


events = {}
with open("data/events/events.json", "r", encoding="utf-8") as f:
    events = json.load(f)

SPONSORS = {}
with open("data/sponsors/sponsors.json", "r", encoding="utf-8") as f:
    SPONSORS = json.load(f)

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
