import os, click, magic
from pwd import getpwuid
from grp import getgrgid

def print_permissions(file):
    click.echo('=====PERMISSIONS=====')
    actions = [('READ', os.R_OK), ('WRITE', os.W_OK), ('EXECUTE', os.X_OK)]
    permissions = [(action[0], os.access(file, action[1])) for action in actions]
    for permission in permissions:
        click.echo(f'{permission[0]:10}={permission[1]:10d}')

def print_type(file):
    click.echo('=====FILE-TYPE=======')
    click.echo(magic.from_file(file))

def print_owner(file):
    click.echo('=====OWNER===========')
    click.echo(f'{"OWNER":10}={getpwuid(os.stat(file).st_uid).pw_name.rjust(10)}')
    click.echo(f'{"GROUP":10}={getgrgid(os.stat(file).st_gid).gr_name.rjust(10)}')

def print_size(file):
    click.echo('=====SIZE============')
    size = os.stat(file).st_size.__float__()
    if size < 1024:
        size = (size, 'B')
    elif size >= 1024 and size < 1024**2:
        size = (size / 1024, 'KB')
    elif size >=1024**2 and size < 1024**3:
        size = (size / 1024**2, 'MB')
    else:
        size = (size / 1024**3, 'GB')
    click.echo(f'{"SIZE":10}={f"{size[0]:.3f}{size[1]}".rjust(10)}')

def all(file):
    print_permissions(file)
    print_type(file)
    print_owner(file)
    print_size(file)
