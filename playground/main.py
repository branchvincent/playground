import click


@click.group()
def cli():
    """Main entrypoint."""


@cli.command()
@click.option("-d", "--debug", help="Include debug output.")
def build(debug):
    """Build production assets."""


if __name__ == "__main__":
    cli()
