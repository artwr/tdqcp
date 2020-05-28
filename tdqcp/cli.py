"""Console script for tdqcp."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for tdqcp."""
    click.echo("Replace this message by putting your code into "
               "tdqcp.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
