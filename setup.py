from setuptools import setup

setup(
	name='fzoom',
	version='0.1',
	py_modules=['fzoom'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		fzoom=fzoom:main
	''',
)