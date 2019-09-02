import click, os, meta, text

class Config:
	def __init__(self):
		pass

config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@config
def main(config):
	'''
		This script analizes a text file.
		It takes in only one argument, the file on which to
		perform the analysis. It also has multiple composing sub-commands
		with which to specify the desired action.
	'''
	pass

@main.command('meta')
@click.option('-p', '--permissions', is_flag=True, help='Shows permissions of the file')
@click.option('-t', '--type', is_flag=True, help='Shows type of the file')
@click.option('-o', '--owner', is_flag=True, help='Shows owner information of the file')
@click.option('-s', '--size', is_flag=True, help='Shows the size of the file')
@click.argument('file', type=click.Path(exists=True, file_okay=True, readable=True, allow_dash=False), required=True)
@config
def meta_command(config, file, permissions, type, owner, size):
	'''
		Sub-command meta provides the requested meta-information
		of the file passed as an argument. It includes information like
		permissions, owner, etc.
	'''
	executed = False
	if permissions:
		meta.print_permissions(file)
		executed = True
	if type:
		meta.print_type(file)
		executed = True
	if owner:
		meta.print_owner(file)
		executed = True
	if size:
		meta.print_size(file)
		executed = True

	if not executed:
		meta.all(file)

@main.command('text')
@click.option('-w', '--word', type=click.STRING, help='Word to be searched in the given text file')
@click.option('-r', '--regex', type=click.STRING, help='Regex to be applied on the given text file')
@click.option('-c', '--count', is_flag=True, help='Shows the number of appearances in the file')
@click.option('-t', '--top-words', type=int, help='Returns the top INT words after the number of appearances')
@click.argument('file', type=click.File('r'), required=True)
@config
def text_command(config, word, regex, count, top_words, file):
	'''
		Sub-command text provides the requested information
		of the file passed as an argument. It includes features like
		word-searching, top words, etc.
	'''
	executed = False
	content = file.readlines()
	if word is not None:
		text.search_word(content, word)
		executed = True
	if regex is not None:
		text.search_regex(content, regex)
		executed = True
	if count:
		text.count(content)
		executed = True
	if top_words is not None:
		text.top_words(content, top_words)
		executed = True

	if not executed:
		text.overview(content)
