# -*- coding: utf-8 -*-

"""Console script for example_package_github_pixel3."""
import sys
import click


@click.group()
@click.option('--verbose_for_main', is_flag=True)
def main(verbose_for_main):
    """Docstring for cli.py in package (also the entry point for cli)"""
    if verbose_for_main:
        click.echo("Main is only ran when subcommand is ran")
    click.echo("Code in package.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


@main.command()
@click.option('--hello', default='Hello World!',
              help='Just a variable called "Hello"')
@click.argument('repeat', type=int)
def say_hello(hello, repeat):
    """Docstring for subcommand in cli.py in package)
       :param repeat: How many times function prints the "hello" variable
    """
    for _ in range(repeat):
        click.echo('Function is printing: %s ' % hello)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
