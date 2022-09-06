#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: run_cmd.py
#  Version: 0.0.3
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

from rich.columns import Columns
from rich.console import Console

from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.interfaces.textualize import get_panels
from fundamentus.main.fundamentus_pipeline import \
    FundamentusPipeline as Fundamentus


def get_arguments() -> argparse.Namespace:
    """Argument parser.

    :return: Argument parser.
    """

    # Create the parser.
    parser = argparse.ArgumentParser(
        description='Python Fundamentus is a Python API that allows you to '
        'quickly access the main fundamental indicators of the '
        'main stocks in the Brazilian market.')

    # Add the arguments.
    parser.add_argument('ticker', type=str, help='Stock ticker.')

    return parser.parse_args()


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

    # Get the arguments.
    args = get_arguments()

    # Get the stock information.
    information = main(ticker=args.ticker)

    # Initialize the console.
    console = Console()

    # Clean the console.
    console.clear()

    # Get the tables.
    panels = get_panels(information)

    # Print the panels.
    console.print(Columns(panels, expand=True))
