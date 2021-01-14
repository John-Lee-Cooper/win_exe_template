#!/usr/bin/env python

""" Simple search script """

from datetime import datetime
from pathlib import Path
from sys import argv, version

import click


def search(input_dir: Path, regx: str, out_path: Path):
    """ Write all files in input_dir that match regular expression regx to out_path """

    with open(out_path, "w") as output:
        output.write(f"Search {input_dir} for {regx}:\n\n")
        for filename in input_dir.rglob(regx):
            output.write(f"{filename}\n")


def main():
    """ Get input and call search """

    # Get input directory from command line
    if len(argv) != 2:
        script = Path(argv[0]).name
        click.echo(f"Python {version}")
        click.echo(f"Useage ERROR: Drag a folder on top of {script} icon to run")
        click.echo("Hit any key to exit")
        click.getchar()
        return
    input_dir = Path(argv[1])

    # Prompt user for regular expression
    default = "*"
    text = f"Search for what regx (default='{default}')"
    regx = click.prompt(text, default=default)

    # create a safe filename with current date
    tstamp = str(datetime.now())
    for character in "- :":
        tstamp = tstamp.replace(character, "_")
    out_path = Path(".") / f"search_{tstamp}.txt"

    try:
        search(input_dir, regx, out_path)

    except Exception as error:  # pylint: disable=broad-except
        error_log = open("search_error.txt", "w")
        error_log.write(str(error))


if __name__ == "__main__":
    main()
