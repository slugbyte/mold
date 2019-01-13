'''
help defines an api for printing mold help messages.
'''

import re
import markdown
import codecs 
import mold.fs  as fs
from mold.color import *

def help_example():
    conf_help = fs.dirname(__file__ ) + '/../../docs/drop_help.md'
    with codecs.open(conf_help, mode='r', encoding='utf-8') as help_file:
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

    
    # to_print = to_print.split('\n')
    # to_print = to_print.split(' ')
    # to_print = to_print.replace('<h1>', yellow).replace('</h1> ', reset + '\n')
    # to_print = to_print.replace('<h2>', yellow).replace('</h2> ', reset + '\n')
    # print(to_print)
    # to_print = to_print.replace('<p>', '').replace('</p>', reset + '\n')
    # to_print = to_print.replace('\n<code>', green).replace('</code>', reset + '')
    # to_print = to_print.replace('<ul>\n', '').replace('\n</ul>', '')
    # to_print = to_print.replace('<li>\n', '').replace('\n</li>', '')
    # to_print = to_print.replace('<strong>', blue).replace('</strong>', reset)


    # lines = to_print.split('\n')
    # # to_print = ''
    # result = ''
    # for line in lines:
        # if len(line) > 70:
            # line_break_index = line.find(' ', 70)
            # if line_break_index >= 0:
                # line = line[:line_break_index] + '\n\t' + line[line_break_index + 1:]
                # result = result + line + '\n'
            # else:
                # result = result +  line  + '\n'
        # else:
            # result = result + line + '\n'

    # lines = result.split('\n')
    # # to_print = ''
    # result = ''
    # for line in lines:
        # if len(line) > 70:
            # line_break_index = line.find(' ', 70)
            # if line_break_index >= 0:
                # line = line[:line_break_index] + '\n\t' + line[line_break_index + 1:]
                # result = result + line + '\n'
            # else:
                # result = result +  line  + '\n'
        # else:
            # result = result + line + '\n'

    # result = result.replace('.i\n\n', '\n')
        # print(len(line))
        # print(line.find('--'))

    # print(result.strip())


# import mold as _mold
# import mold.colokr as color

# load all the help files
# import mold.help.main_help as main_help 

# # core 
# import mold.help.core.conf_help as conf_help
# import mold.help.core.plug_help as plug_help
# import mold.help.core.exec_help as exec_help
# import mold.help.core.drop_help as drop_help
# import mold.help.core.fold_help as fold_help
# import mold.help.core.core_task_help as core_task_help

# # sync 
# import mold.help.sync.sync_help as sync_help

# # TODO NOW: 1) get the rest of the help text in this file into own files
# # 2) make help text files for sync tasks
# # 3) figure out how you want to really go about compile and color <3

# # TODO: refacter each help to be a string
# # then create a comple fiunction that will choose to colorify base on ctx
# # then make a create_help_handler to generate help defs (functions)

# header_color = color.cyan 
# task_color = color.blue
# command_color = color.magenta
# warning_color = color.red 
# reset = color.reset


# def colorify(str):
    # for header in ['USAGE:', 'ABOUT:', 'INSTALL:', 'CONFIGURATION:', 'HELP:', 'COMMANDS:', 
            # 'TASKS:', 'NOTE:', 'INSTALL FROM REPOSITORY:']:
        # str = str.replace(header, f'{header_color}{header}{reset}')
    # for command in ['conf:', 'plug:', 'exec:', 'drop:', 'fold:', 'sync:']:
        # str = str.replace(command, f'{command_color}{command.replace(":", "")}{reset}')
    # for task in [' list:', ' make:', ' load:', ' edit:', ' dump:', ' nuke:', 
            # ' add:', ' commit:', ' push:', ' merge:', ' auto:', ' log:', ' pull:',
            # ' status:', ' branch:', ' diff:', ' --force-push:', ' --hard-reset:', ' --new-branch:', 
            # ' --delete-branch:', ' --checkout:']:
        # str = str.replace(task, f'{task_color}{task.replace(":", "")}{reset}')
    # for warn in ['WARNING:', 'DANGER:']: 
        # str = str.replace(warn, f'{warning_color}{warn}{reset}')
    # return str

# def color_print(*args):
    # color_args = []
    # for x in args:
        # color_args.append(colorify(x))
    # print(*color_args)

# def compile(ctx, text):
    # green = color.green
    # reset = color.reset
    # mold = _mold
    # return text.format(**locals())

# def main(ctx):
    # color_print(compile(ctx, main_help.text))
# def conf(ctx):
    # color_print(compile(ctx, conf_help.text))
# def plug(ctx):
    # color_print(compile(ctx, conf_plug.text))


