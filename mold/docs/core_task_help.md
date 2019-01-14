def _one_arg_help(description):
    return 'USAGE: mold {ctx.command} {ctx.task} <filename>\n' + description)

def _two_arg_help(description):
    return 'USAGE: mold {ctx.command} {ctx.task} <filename> [optional <new-filename>]\n' + description)

# one arg 
make_text = _one_arg_help('Make a new {ctx.command} with your text editor.')
edit_text = _one_arg_help('Edit an existing {ctx.command}.')
nuke_default_text = _one_arg_help('Delete a {ctx.command} from your config repo.')
nuke_conf_text = _one_arg_help('Delete a {ctx.command} from your config repo.\nIt will not delete the file fom your $HOME directoy.')

# two arg 
load_text = _two_arg_help('Load a {ctx.command} into your config repo.')
dump_text = _two_arg_help( 'load', 'Copy a {ctx.command} from your config repo into your current directory.')

# no args
list_text = 'USAGE: mold {ctx.command} list\nList the {ctx.command} in your config repo.'
