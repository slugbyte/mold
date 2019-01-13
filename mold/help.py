'''
help defines an api for printing mold help messages.
'''

import re
import markdown
import codecs 
import mold.fs  as fs
from mold.color import *

def read_help_file(help_file):
    with codecs.open(help_file, mode='r', encoding='utf-8') as help_file:
        help_text = help_file.read()
        return markdown.markdown(help_text)

def replace_non_header_tags(html):
    html = html.replace('</h1>', reset + '</h1>\n')
    html = html.replace('</h2>', reset +'</h2>\n')
    html = html.replace('<blockquote>', '').replace('</blockquote>',  '\n')
    html = html.replace('<blockquote> <p>', '').replace('</p> </blockquote>',  '\n')
    html = html.replace('<p>', '').replace('</p>',  '\n')

    html = re.sub('<br />', '\n', html)
    html = html.replace('<em>', '').replace('</em>', '')
    html = html.replace('<strong>', blue + '').replace('</strong>', reset + '')
    html = re.sub('<a.*?>', blue, html)
    html = html.replace('</a>', reset)
    html = html.replace('<code>',  green + '').replace('</code>', reset + '') # green must appear before '    ' because of strip below
    html = html.replace('<ul>', '').replace('</ul>', '')
    html = html.replace('<li>', '').replace('</li>','' )
    return html.strip()

def force_text_wrap(text, max_width=80):
    lines = text.split('\n')
    text = ''
    max_width = 80
    for line in lines:
        if len(line) < max_width:
            text += line + '\n'
        else:
            while len(line) > max_width:
                space_index = line.find(' ', max_width)
                text +=  line[:space_index] + '\n'
                line = line[space_index:]
            text += line + '\n'
    return text.strip()

def indent_non_headers(text):
    lines = text.split('\n')
    text = ''
    for line in lines:
        line = re.sub('\s+', ' ', line).strip()  + '\n' # strip whitespace
        if len(line.strip()) == 0:
            continue
        if line.startswith('<') and not line.startswith('<span'):
            text += line 
        else: 
            text += '    ' + line 
    return text.strip()

def replace_header_tags(text):
    text = text.replace('<h1>', yellow).replace('<h2>', yellow)
    text = text.replace('<h3>', red).replace('<h4>', '    ')
    text = re.sub('</h.*>', reset, text)
    text = text.replace('<span/>', '    ')
    text = text.replace('<span />', '    ')
    text = text.replace("<span classname='newline'/>", '')
    return text.strip()

def print_help(ctx, help_file):
    help_file = ctx.MOLD_DOCS + '/' + help_file
    help_text = read_help_file(help_file)
    help_text = replace_non_header_tags(help_text)
    help_text = force_text_wrap(help_text, 80)
    help_text = indent_non_headers(help_text)
    help_text = replace_header_tags(help_text)
    print(help_text)

# # TODO NOW: 1) get the rest of the help text in this file into own files
# # 2) make help text files for sync tasks
# # 3) figure out how you want to really go about compile and color <3

# # TODO: refacter each help to be a string
# # then create a comple fiunction that will choose to colorify base on ctx
# # then make a create_help_handler to generate help defs (functions)
# def print_help(ctx, help_file):
    # print('gnna print ', ctx.MOLD_DOCS + '/' + help_file)

def handle_help(ctx):
    if ctx.command:
        help_file = ctx.command 
        if ctx.task:
            help_file += '_' + ctx.task
        help_file += '_help.md'
        print_help(ctx, help_file)
    else:
        print_help(ctx, 'README.md')
    # print(f'hit handle help cmd:{ctx.command}, task:{ctx.task}')
