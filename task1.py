import os
import csv

import click
import requests

DEFAULT_TIMEOUT = 3
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def url_check(url):
    try:
        r = requests.get(url, timeout=DEFAULT_TIMEOUT)
        return r
    except requests.exceptions.ReadTimeout as err:
        return f"Skipping {url}"


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-i', '--filename', type=click.File('r'))
def main(filename):
    """Url status code checker"""

    csv_obj = csv.reader(filename, delimiter="|")
    for co in csv_obj:
        url_name, url = co
        res = url_check(url)
        if isinstance(res, str) or not isinstance(res, requests.models.Response):
            print(res)
            continue
        response_time = res.elapsed.total_seconds()
        print(f"{repr(url_name)}, HTTP {res.status_code}, time {response_time:.2f} seconds")


if __name__ == "__main__":
    main()
