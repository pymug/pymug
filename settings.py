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



events = {
    "jan-2023": {
        "title": "Python Meetup Jan 2023",
        "venue": "Developers Institute Cassis",
        'date': 'January 21, 2023',
        'raw_html': '<iframe src="https://docs.google.com/document/d/e/2PACX-1vTDXPLtjIXz8UTGxOgWA5xJ4n3Puv7F5cQnFVBRvLCRoChoiYpuFkmlfK5ktO6qVoXhftOYVc_xYiZv/pub?embedded=true" style="width: 100%; height: 500px;"></iframe>',
        "attendees": {'reg': 13, 'came':12},
        'register': 'https://www.meetup.com/pymauritius/events/290824540/',
        'sessions': [ 
        {
            'title': 'Journey Of A Data Engineer',
            'info': 'The Python journey of a data eng',
            'speaker/s': ['Sid-Bisram'],
            'presented': 1,
            'remote': 0
        }, 
        {
            'title': 'Text Analysis With Spacy',
            'info': 'Introductory session on NLP with Spacy',
            'speaker/s': ['nirmal-k-r'],
            'presented': 1,
            'remote': 0
        }],
    },
    "oct-2022": {
        "title": "Python Meetup Oct 2022",
        "venue": "Nayar Space, Flic-en-flac",
        'date': 'October 8, 2022',
        'raw_html': '<iframe src="https://docs.google.com/document/d/e/2PACX-1vRMMkNHm0jSzmy-C_ijwIpbXxBibbmy_bPiRFpQuEil7hhRgRY3-IBhIfOSd6C0e3PsxKBZPkV-OL_E/pub?embedded=true" style="width: 100%; height: 500px;"></iframe>',
        "attendees": {'reg': None, 'came':None},
        'register': 'https://www.meetup.com/pymauritius/events/288602832/',
        'sessions': [ 
        {
            'title': "Python's Bytecode",
            'info': 'An overview of how Python works behind the scene.',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Performing Explanatory Data Analysis With OpenData Mauritius',
            'info': '---',
            'speaker/s': ['kherin'],
            'presented': 1,
            'remote': 0 
        },
        {
            'title': 'Hands-on OpenSource contributions',
            'info': 'Workshop on the complete lifecycle of contributions',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0 
        }
        ], 
    },
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
    },
    "april-2022": {
        "title": "Python Meetup April 2022",
        "venue": "Online",
        'date': 'April 2, 2022',
        'raw_html': '',
        "attendees": {'reg': 5, 'came':1},
        'register': 'https://www.meetup.com/pymauritius/events/284808363/',
        'sessions': [ 
        {
            'title': 'Customizing objects to the max: The human side of the game',
            'info': 'How objects can be manipulated to create neat library APIs',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 1
        }, 
        ], 
    },
    "jan-2022": {
        "title": "Python Meetup January 2022",
        "venue": "Online",
        'date': 'January 30, 2022',
        'raw_html': '',
        "attendees": {'reg': 4, 'came':2},
        'register': 'https://www.meetup.com/pymauritius/events/283354392/',
        'sessions': [ 
        {
            'title': 'FastAPI: Intro and insights',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 1
        }, 
        ], 
    },
    "sept-2021": {
        "title": "Python Meetup September 20221",
        "venue": "Online",
        'date': 'September 30, 2021',
        'raw_html': '',
        "attendees": {'reg': 19, 'came':9},
        'register': 'https://www.meetup.com/mauritiussoftwarecraftsmanshipcommunity/events/280795927/',
        'sessions': [ 
        {
            'title': 'Programming and Cyber Security',
            'info': '',
            'speaker/s': ['elysiumsecurityltd'],
            'presented': 1,
            'remote': 1
        }, 
        ], 
    },
    "april-2021": {
        "title": "Python Meetup April 2021",
        "venue": "Online",
        'date': 'April 17, 2021',
        'raw_html': '',
        "attendees": {'reg': 17, 'came':10},
        'register': 'https://www.meetup.com/mauritiussoftwarecraftsmanshipcommunity/events/277356021/',
        'sessions': [ 
        {
            'title': 'Machine Learning',
            'info': '',
            'speaker/s': ['ThierDev'],
            'presented': 1,
            'remote': 1
        },
        {
            'title': 'Networking Concepts in Py',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 1
        }, 
        ], 
    },
    "ug-summit-2021": {
        "title": "Your Programming Language is Great, Python is Greater",
        "venue": "Middlesex, Flic-en-Flac",
        'date': 'March 1, 2021',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Your Programming Language is Great, Python is Greater',
            'info': '',
            'speaker/s': ['josiah-nyangaga'],
            'presented': 0,
            'remote': 0
        },
        ], 
    },
    "feb-2021": {
        "title": "Python Meetup Februrary 2021",
        "venue": "La Turbine, Moka",
        'date': 'February 13, 2021',
        'raw_html': '',
        "attendees": {'reg': 21, 'came':13},
        'register': 'https://www.meetup.com/mauritiussoftwarecraftsmanshipcommunity/events/275960024/',
        'sessions': [ 
        {
            'title': 'Web Scraping With Python',
            'info': '',
            'speaker/s': ['ashfaaq77'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Introduction to the FReMP stack',
            'info': '',
            'speaker/s': ['kouul'],
            'presented': 0,
            'remote': 0
        }, 
        {
            'title': 'Python Deployment',
            'info': '',
            'speaker/s': ['nam4dev'],
            'presented': 0,
            'remote': 0
        },
        {
            'title': 'The Web: Taking the Modular Approach A Step Further',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "dec-2020": {
        "title": "Python Meetup December 2020",
        "venue": "La Turbine, Moka",
        'date': 'December 13, 2021',
        'raw_html': '',
        "attendees": {'reg': 25, 'came':13},
        'register': 'https://www.meetup.com/mauritiussoftwarecraftsmanshipcommunity/events/274605998/',
        'sessions': [ 
        {
            'title': 'Automating your workflows with Apache Airflow',
            'info': '',
            'speaker/s': ['marclamberti'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Using ReactJs & Mongo with Flask - Introducing the FReMP stack',
            'info': '',
            'speaker/s': ['kouul'],
            'presented': 0,
            'remote': 0
        }, 
        {
            'title': 'Easily create PDFs with Python!',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "nov-2020": {
        "title": "Python Meetup November 2020",
        "venue": "Paris Sublight California, Moka",
        'date': 'November 7, 2020',
        'raw_html': '',
        "attendees": {'reg': 7, 'came':2},
        'register': 'https://www.meetup.com/mauritiussoftwarecraftsmanshipcommunity/events/274123129/',
        'sessions': [ 
        {
            'title': ' Deriving Asyncio',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "uni-uom-oct-2020": {
        "title": "University of Mauritius Oct 2020",
        "venue": "University of Mauritius",
        'date': 'October 1 2020',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': ' Python basics, turtle and exercises',
            'info': '',
            'speaker/s': ['mjzyaad'],
            'presented': 1,
            'remote': 1
        },
        {
            'title': 'Functions, recursions and files',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 1
        },
        ], 
    },
    "data-sci-covid19": {
        "title": "Intro to Data Science by Tracking Covid-19 Progression using Python.",
        "venue": "University of Mauritius",
        'date': 'June 23, 2020',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Intro to Data Science by Tracking Covid-19 Progression using Python.',
            'info': '',
            'speaker/s': ['dominiquetheodore'],
            'presented': 1,
            'remote': 1
        }
        ], 
    },
    "may-2020": {
        "title": "Python Meetup May 2020",
        "venue": "Online",
        'date': 'May 24, 2020',
        'raw_html': '',
        "attendees": {'reg': 11, 'came':7},
        'register': 'https://www.meetup.com/mauritiussoftwarecraftsmanshipcommunity/events/270599886/',
        'sessions': [ 
        {
            'title': 'Démonstration OSNIT with Python',
            'info': '',
            'speaker/s': ['sebastianadam'],
            'presented': 1,
            'remote': 1
        },
        {
            'title': ' Canvas Theory With Pygame',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 1
        },
        ], 
    },
    "uni-uom-web-scraping": {
        "title": "University of Mauritius - Web Scraping",
        "venue": "Online",
        'date': 'May 3, 2020',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'resources':{
            'video': 'https://www.facebook.com/UOMOracleClub/videos/686768432073371/'
        },
        'sessions': [ 
        {
            'title': 'Movies Collector',
            'info': '',
            'speaker/s': ['satveerbhantoo'],
            'presented': 1,
            'remote': 1
        },
        {
            'title': 'News And Deals',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 1
        },
        ], 
    },
    "uni-uom-web-dev-2": {
        "title": "University of Mauritius - Web Dev 2",
        "venue": "Online",
        'date': 'April 26, 2020',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Learn How To Build Your Own Blog',
            'info': '',
            'speaker/s': ['nam4dev'],
            'presented': 1,
            'remote': 1,
            'resources':{
                'code': 'https://github.com/pymug/django-blog-demonstration'
            }
        },
        ], 
    },
    "uni-uom-web-dev-1": {
        "title": "University of Mauritius - Web Dev 2",
        "venue": "Online",
        'date': 'April 19, 2020',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Python Intermediate Part 2',
            'info': '',
            'speaker/s': ['kherin'],
            'presented': 1,
            'remote': 1,
        },
        {
            'title': 'Web Dev With Flask',
            'info': '',
            'speaker/s': ['RajaAjmal'],
            'presented': 1,
            'remote': 1,
        },
        {
            'title': 'Flask Heroku Deployment',
            'info': '',
            'speaker/s': ['kouul'],
            'presented': 1,
            'remote': 1,
        },
        ], 
    },
    "python-basics": {
        "title": "University of Mauritius - Python Basics",
        "venue": "Online",
        'date': 'April 19, 2020',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Python Intermediate',
            'info': '',
            'speaker/s': ['kherin'],
            'presented': 1,
            'remote': 1,
        },
        {
            'title': 'Python Basics',
            'info': '',
            'speaker/s': ['RajaAjmal'],
            'presented': 1,
            'remote': 1,
        },
        ], 
    },
    "april-2020": {
        "title": "Python Meetup April 2020",
        "venue": "Online",
        'date': 'April 18, 2020',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Build a minimal site with Django',
            'info': '',
            'speaker/s': ['krishnah-soyjaudah'],
            'presented': 1,
            'remote': 1
        },
        {
            'title': 'API integration with Python',
            'info': '',
            'speaker/s': ['mridubhatnagar'],
            'presented': 1,
            'remote': 1
        },
        {
            'title': 'How to be a true faker',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 1
        },
        ], 
    },
    "march-2020": {
        "title": "Python Meetup March 2020",
        "venue": "Online",
        'date': 'March 28, 2020',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Flask From Scratch',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 1
        },
        ], 
    },
    "feb-2020": {
        "title": "Python Meetup Feb 2020",
        "venue": "MCB Digital factory, Port Louis",
        'date': 'Febrary 29, 2020',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'CNNS with TensorFlow',
            'info': '',
            'speaker/s': ['kherin'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Flask & Django: The Key to Grasp Both in Only One Session',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 0,
            'remote': 0
        },
        ], 
    },
    "uni-uom-ai-2019": {
        "title": "University of Mauritius - Ai Crash Course 2019",
        "venue": "University of Mauritius",
        'date': 'December 19, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Image training via an online tool + Scikit and Tensorflow intro',
            'info': '',
            'speaker/s': ['kherin'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Data Visualisations',
            'info': '',
            'speaker/s': ['dominiquetheodore'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Natural language processing',
            'info': '',
            'speaker/s': ['nam4dev'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Intro to Computer Vision',
            'info': '',
            'speaker/s': ['dominiquetheodore'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Numpy and Pandas',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "uni-uom-omri": {
        "title": "University of Mauritius - Intro to machine Learning",
        "venue": "University of Mauritius",
        'date': 'November 19, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Introduction to machine Learning',
            'info': '',
            'speaker/s': ['omrihar'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "py-sratch-4": {
        "title": "Python From Scratch",
        "venue": "Adalabs, Vacoas",
        'date': 'November 21, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Python From Scratch',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "py-sratch-3": {
        "title": "Python From Scratch",
        "venue": "Adalabs, Vacoas",
        'date': 'November 28, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Python From Scratch',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "py-sratch-2": {
        "title": "Python From Scratch",
        "venue": "Adalabs, Vacoas",
        'date': 'December 5, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Python From Scratch',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "py-sratch-1": {
        "title": "Python From Scratch",
        "venue": "Adalabs, Vacoas",
        'date': 'December 12, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Python From Scratch',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "aug-2019": {
        "title": "Python Meetup August 2019",
        "venue": "Maker Space, Vacoas",
        'date': 'August 1, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Practical Session - Scikit & Related Libs',
            'info': '',
            'speaker/s': ['omrihar'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Contributing To The Docs Translations',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "july-2019": {
        "title": "Python Meetup July 2019",
        "venue": "Maker Space, Vacoas",
        'date': 'July 1, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Data Ethics',
            'info': '',
            'speaker/s': ['heman-mohabeer'],
            'presented': 1,
            'remote': 0
        }, 
        {
            'title': 'Displaying Data',
            'info': '',
            'speaker/s': ['satveerbhantoo'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Pandas Introduction',
            'info': '',
            'speaker/s': ['nam4dev'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Boosts From The Standard Library: Itertools',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "june-2019": {
        "title": "Web Scraping Day",
        "venue": "La Trubine, Moka",
        'date': 'June 1, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': ' Basics of BeautifulSoup',
            'info': '',
            'speaker/s': ['kherin'],
            'presented': 1,
            'remote': 0
        }, 
        {
            'title': 'Recon with Requests',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': ' Scraping with Selenium',
            'info': '',
            'speaker/s': ['dominiquetheodore'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': 'Django as Dashboard (while using Scrapy)',
            'info': '',
            'speaker/s': ['nam4dev'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "may-2019": {
        "title": "Python Meetup May 2019",
        "venue": "La Turbine, Moka",
        'date': 'May 1, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Computer Vision demo',
            'info': '',
            'speaker/s': ['kherin'],
            'presented': 1,
            'remote': 0
        }, 
        {
            'title': 'Walkthrough of the Honeybot IRC bot internals',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        {
            'title': ' Django Presentation',
            'info': '',
            'speaker/s': ['dominiquetheodore'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
    "jan-2019": {
        "title": "Python Meetup Jan 2019",
        "venue": "15 Cantons, Vacoas",
        'date': 'January 1, 2019',
        'raw_html': '',
        "attendees": {'reg': None, 'came':None},
        'register': '#',
        'sessions': [ 
        {
            'title': 'Python: The joyful parts',
            'info': '',
            'speaker/s': ['Abdur-RahmaanJ'],
            'presented': 1,
            'remote': 0
        },
        ], 
    },
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
