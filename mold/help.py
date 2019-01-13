'''
help defines an api for printing mold help messages.
'''

import re
import markdown
import codecs 
import mold.fs  as fs
from mold.color import *

def print_help(ctx, help_file):
    help_file = ctx.MOLD_DOCS + '/' + help_file
    # help_file = fs.dirname(__file__ ) + '/../../docs/plug_help.md'
    with codecs.open(help_file, mode='r', encoding='utf-8') as help_file:
        help_text = help_file.read()
        to_print = markdown.markdown(help_text)

    # to_print = re.sub('\s+', ' ', to_print).strip() # strip whitespace
    to_print = to_print.replace('</h1>', reset + '</h1>\n')
    to_print = to_print.replace('</h2>', reset +'</h2>\n')
        # help_text=help_file.read().replace('\n', '')
    # to_print = markdown(help_text)
    to_print = to_print.replace('<blockquote>', '').replace('</blockquote>',  '\n')
    to_print = to_print.replace('<blockquote> <p>', '').replace('</p> </blockquote>',  '\n')
    to_print = to_print.replace('<p>', '').replace('</p>',  '\n')

    to_print = re.sub('<br />', '\n', to_print)
    to_print = to_print.replace('<em>', '').replace('</em>', '')
    to_print = to_print.replace('<strong>', blue + '').replace('</strong>', reset + '')
    to_print = re.sub('<a.*?>', blue, to_print)
    to_print = to_print.replace('</a>', reset)
    to_print = to_print.replace('<code>',  green + '').replace('</code>', reset + '') # green must appear before '    ' because of strip below
    to_print = to_print.replace('<ul>', '').replace('</ul>', '')
    to_print = to_print.replace('<li>', '').replace('</li>','' )

    to_print = to_print.replace('&lt;', '<')

    # trim to 70with 
    lines = to_print.split('\n')
    to_print = ''
    max_width = 80
    for line in lines:
        if len(line) < max_width:
            to_print += line + '\n'
        else:
            while len(line) > max_width:
                space_index = line.find(' ', max_width)
                to_print +=  line[:space_index] + '\n'
                line = line[space_index:]
            to_print += line + '\n'

    # make nice indentation 
    lines = to_print.split('\n')
    to_print = ''
    for line in lines:
        line = re.sub('\s+', ' ', line).strip()  + '\n' # strip whitespace
        if len(line.strip()) == 0:
            continue
        if line.startswith('<') and not line.startswith('<span'):
            to_print += line 
        else: 
            to_print += '    ' + line 

    # add color to headers
    to_print = to_print.replace('<h1>', yellow).replace('<h2>', yellow)
    to_print = to_print.replace('<h3>', red).replace('<h4>', '    ')

    to_print = re.sub('</h.*>', reset, to_print)
    to_print = to_print.replace('<span/>', '    ')
    to_print = to_print.replace('<span />', '    ')
    to_print = to_print.replace("<span classname='newline'/>", '')

    to_print = to_print.strip()
    print(to_print)

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
    print(f'hit handle help cmd:{ctx.command}, task:{ctx.task}')
