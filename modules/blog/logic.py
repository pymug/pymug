import os
from shutil import copyfile


def build(info, site_api):
    settings = site_api.get_settings()
    print(info, info['module_name'])
    html_content = ''
    
    site_api.create_folder('{}/blog'.format(settings['output_folder']))
    # blog menu page
    mdcontent = ('| title | author | time |\n'
                 '|:---|:---|:---|\n')
    posts_path = 'modules/{}/blog_posts'.format(info['module_name'])
    post_files = site_api.get_files(posts_path)

    for file in post_files:
        post_info = site_api.get_post_data('{}/{}'.format(posts_path, file))
        mdcontent += '| [{}]({}) | {} | {} |\n'.format(
            post_info['title'],
            post_info['slug'],
            post_info['author'],
            post_info['time']
            )

        # individual posts
        individual_post_html_content = ''
        site_api.create_folder('{}/blog/{}'.format(settings['output_folder'], post_info['slug']))
        individual_post_html_content = site_api.puremdtohtml(
            ('# {}\n'
            '_by {}_\n'
            '{}').format(post_info['title'], post_info['author'], post_info['mdcontent']))
        site_api.create_file(
            info, 
            'blog_post.html', 
            '{}/blog/{}/index.html'.format(settings['output_folder'], post_info['slug']),
            content=individual_post_html_content,
            assets_path_append='../../')
        
    # main blog page rendering
    html_content += site_api.puremdtohtml(mdcontent)
    site_api.create_file(info, 'blog.html', '{}/blog/index.html'.format(settings['output_folder']),
        content=html_content,
        assets_path_append='../')