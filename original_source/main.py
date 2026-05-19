import click

@click.group()
def main():
    """Sovereign Biz Box CLI"""
    pass

@main.group()
@click.option('--alias', is_flag=True, help='Enable alias mode')
def root_group():
    """Root command group"""
    pass

# Nested subcommand example
@root_group.command()
@click.argument('project_name')
def start(project_name):
    """Start a new project"""
    print(f'Starting project: {project_name}')

# Alias example
@root_group.command(name='proj', help='Alias for project commands')
@click.argument('project_name')
def alias_start(project_name):
    """Alias for start command"""
    print(f'Alias started: {project_name}')