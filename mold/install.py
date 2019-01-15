'''
install defines an api for installing a MOLD_ROOT.
'''

import mold.git as git 
import mold.fs as fs
import mold.system as system
from mold.color import get_color

_red = 'red'
_cyan = 'cyan'
_reset = 'reset'
_green = 'green'
_yellow = 'yellow'
_magenta = 'magenta'

# PRIVATE
BUILD_DIR = __file__.replace('install.py', 'assets')

def _log_success(ctx, extra='.'):
    green = get_color(ctx, _green)
    yellow = get_color(ctx, _yellow)
    reset = get_color(ctx, _reset)
    magenta = get_color(ctx, _magenta)
    print(f'''
{green}SUCCESS{reset}
A MOLD_ROOT has installed to {ctx.MOLD_ROOT}{extra}
{yellow}Follow these IMPORTANT instructions to complete setting up mold.{reset}
First add the follwing two lines to your shell config file (i.e. ~/.bashrc).
    {magenta}export MOLD_ROOT='{ctx.MOLD_ROOT}'
    source $MOLD_ROOT/mold-loader.sh{reset}
Next source your shell config (e.g. "source ~/.bashrc"). 
Then then you will be good to go, {green}Enjoy mold!{reset} :)''')

def _log_warning(ctx, extra='.'):
    red = get_color(ctx, _red)
    green = get_color(ctx, _green)
    yellow = get_color(ctx, _yellow)
    reset = get_color(ctx, _reset)
    magenta = get_color(ctx, _magenta)
    print(f'''
{red}!WARNING!{reset}
{yellow}A MOLD_ROOT directory was installed to {ctx.MOLD_ROOT}{extra}{yellow}
{yellow}If you dont want to re-install, follow these IMPORTANT instructions to complete setting up mold.{reset}
{yellow}First add the follwing two lines to your shell config file (i.e. ~/.bashrc).{reset}
    {magenta}export MOLD_ROOT='{ctx.MOLD_ROOT}'
    source $MOLD_ROOT/mold-loader.sh{reset}
{yellow}Next source your shell config (e.g. "source ~/.bashrc").{reset} 
{yellow}Then then you will be good to go, {green}Enjoy mold!{reset} :)''')

def _log_failure(ctx):
    red = get_color(ctx, _red)
    reset= get_color(ctx, _reset)
    print(f'''{red}Sorry, something went wrong, a MOLD_ROOT was not installed.{reset}
You can create an issue at https://github.com/slugbyte/mold/issues for support.''')

def _cleanup_and_fail(ctx):
    if fs.exists(ctx.MOLD_ROOT):
        fs.rimraf(ctx.MOLD_ROOT)
    _log_failure(ctx )

def _create_mold_root(ctx):
    try:
        if fs.exists(ctx.MOLD_ROOT):
            fs.rimraf(ctx.MOLD_ROOT)
        system.cd(BUILD_DIR)
        tarpath = BUILD_DIR + '/mold-root.tar.gz'
        fs.unpack_tarball(tarpath)
        fs.mv(BUILD_DIR + '/mold-root', ctx.MOLD_ROOT)
        return True
    except: 
        return False

def _setup_git(ctx, remote):
    system.cd(ctx.MOLD_ROOT)
    return git.init(ctx, remote)

# RETURN TRUE FOR CONTINE FALSE FOR EXIT
def _handle_mold_root_exists(ctx):
    red = get_color(ctx, 'red')
    cyan = get_color(ctx, 'cyan')
    reset = get_color(ctx, 'reset')
    if fs.exists(ctx.MOLD_ROOT) and not ctx.check_flag_set('--quick-install'):
        print(f'{red}Hmm,{reset} {ctx.MOLD_ROOT} {red}allready exits.{reset}')
        cancel = 'y' != input(f'{cyan}Do you want to remove it and continue? y/n:{reset} ').strip()
        if cancel: 
            print(f'Ok, MOLD_ROOT installation canceled.')
            return False
    return True

def _handle_mold_root_set_remote(ctx):
    red = get_color(ctx, 'red')
    cyan = get_color(ctx, 'cyan')
    reset = get_color(ctx, 'reset')
    remote = ''
    if ctx.check_set_remote_set():
        remote = ctx.task
    else:
        if not ctx.check_flag_set('--quick-install'):
            cancel = 'y' != input(f'{cyan}Do you want to setup a git remote? y/n:{reset} ').strip()
            if cancel: 
                print(f'Ok, no git remote will be configured.')
                return False
            remote = input(f'{cyan}Enter a git remote uri:{reset} ').strip()
    if not remote:
        _log_success(ctx, f' {red}with out a remote remote repository.{reset}')
        return False 
    if not git.set_remote(ctx, remote).check_ok():
        return _log_warning(ctx, f'''.
{red}However, git failed to add the remote uri "{remote}" 
Run mold help and read the about using "mold --set-remote" to add a remote.{reset}''')
    if not git.push(ctx).check_ok():
        _log_warning(ctx, f'''.
{red}However, git failed to push to the remote uri {remote}
Your remote probbly allready has content in it. If you want to 
overwrite the remote run {cyan}mold sync --force-push{red}, or you can run
{cyan}mold --install{red} again and overwrite the current $MOLD_ROOT.{reset}''')
        return False
    return True

# INTERFACE
def install(ctx):
    # colors
    green = get_color(ctx, _green)
    red = get_color(ctx, _red)
    cyan = get_color(ctx, _cyan)
    magenta = get_color(ctx, _magenta)
    yellow = get_color(ctx, _yellow)
    reset = get_color(ctx, _reset)

    quick = ctx.check_flag_set('--quick-install')
    if not _handle_mold_root_exists(ctx):
        return ctx.OK
    print(f'{green}Installing{reset} a MOLD_ROOT in {ctx.MOLD_ROOT}')
    if not _create_mold_root(ctx):
        return _cleanup_and_fail(ctx)
    if not git.init(ctx).check_ok():
        return _cleanup_and_fail(ctx)
    if not _handle_mold_root_set_remote(ctx):
        return 
    _log_success(ctx, f' with the remote repository {remote}')
