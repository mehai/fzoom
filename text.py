import click, re

def search_word(content, word):
    click.echo('=====WORD-SEARCHING=====')
    click.echo(f'WORD: {word}')
    count = 0
    for i, line in enumerate(content):
        printed = False
        for token in re.split(r'[?><:!/;,."\(\)\'\[\]\n\t\s]\s*', line):
            if token is not None and word == token.lower():
                count += 1
                if not printed:
                    click.echo(f'{str(i):5}{line}')
                    printed = True
    click.echo(f'TOTAL NUMBER OF APPEARANCES: {count}')

def search_regex(content, regex):
    click.echo('=====PATTERN-MATCHING===')
    click.echo(f'REGEX: {regex}')
    count = 0
    for i, line in enumerate(content):
        if re.search(regex, line) is not None:
            click.echo(f'{str(i):5}{line}')
            count += 1
    click.echo(f'TOTAL NUMBER OF APPEARANCES: {count}')

def top_words(content, limit):
    occurrences = {}
    click.echo('=====TOP-WORDS==========')
    click.echo(f'LIMIT: {limit}')
    for i, line in enumerate(content):
        for token in re.split(r'[?><:!/;,."\(\)\'\[\]\n\t\s]\s*', line):
            if token != "":
                if token in occurrences:
                    occurrences[token] += 1
                else:
                    occurrences[token] = 1
    tokens = sorted(occurrences.items(), reverse=True, key=lambda elem: elem[1])
    for i, elem in enumerate(tokens):
        if i == limit:
            break
        click.echo(f'{str(i+1):5}"{elem[0]}" with {elem[1]} occurrences')

def count(content):
    click.echo('=====COUNTING===========')
    count_lines = len(content)
    count_words = 0
    for i, line in enumerate(content):
        count_words += len(line.split())

    click.echo(f'WORDS: {count_words}')
    click.echo(f'LINES: {count_lines}')

def overview(content):
    count(content)
    top_words(content, 5)
