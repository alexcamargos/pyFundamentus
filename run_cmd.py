#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: run_cmd.py
#  Version: 0.0.2
#
#  Summary: Python Fundamentus
#           Python Fundamentus is a Python API that allows you to quickly
#           access the main fundamental indicators of the main stocks
#           in the Brazilian market.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
# ------------------------------------------------------------------------------

"""Fundamentus Command line interface."""

import argparse

from rich.console import Console

from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.interfaces.textualize import get_tables
from fundamentus.main.fundamentus_pipeline import \
    FundamentusPipeline as Fundamentus


def main(ticker: str) -> TransformContract:
    """Main function.

    :param ticker (string): Stock ticker.
    :return: Dictionary with the main fundamental indicators.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    params = {'papel': ticker}

    main_pipeline = Fundamentus(url=url, params=params)
    response = main_pipeline.get_stock_information()

    return response


if __name__ == '__main__':

    # Parse the arguments.
    parser = argparse.ArgumentParser(
        description=
        'Python Fundamentus is a Python API that allows you to quickly '
        'access the main fundamental indicators of the main stocks in the Brazilian market.'
    )

    # Add the arguments options.
    parser.add_argument('ticker', help='Ticker of the stock', type=str)
    args = parser.parse_args()

    # Get the stock information.
    information = main(ticker=args.ticker)

    # Initialize the console.
    console = Console()

    # Get the tables.
    tables = get_tables(information)

    # Print the tables.
    for table in tables:
        console.print(table)
