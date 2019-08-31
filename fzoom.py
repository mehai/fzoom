import click

class Config:
	def __init__(self):
		self.verbose = False

config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type=click.Path())
@config
def main(config, verbose, home_directory):
	'''
		This script analizes a text file.
		It takes in only one argument, the path to the file on which to
		perform the analysis. It also has multiple composing sub-commands
		with which to specify the desired action.
	'''
	config.verbose = verbose
	if home_directory is None:
		home_directory = '.'
	config.home_directory = home_directory


@main.command()
@click.option('--string', default='World', help='Who to greet')
@click.option('--repeat', default=1, help='How many times to do it')
@click.argument('input', type=click.File('r'), default='-', required=False)
@config
def say(config, string, repeat, input):
	'''
		This command greets somebody.
	'''
	if config.verbose:
		click.echo('We are in verbose mode')

	click.echo('Home directory is {config.home_directory}')

	click.echo(f'file to read from is {input}')
	for x in range(repeat):
		click.echo(f'Hello, {string}!')
