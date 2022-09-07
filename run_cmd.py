#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: run_cmd.py
#  Version: 0.0.4
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

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel

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

    titles = [f"{information.transformed_information['informacoes_basicas']['empresa']} "
         f"- {information.transformed_information['informacoes_basicas']['trading_code']}",
              'Informações Básicas',
              'Oscilações',
              'Indicadores de Valuation',
              'Indicadores de Rentabilidade',
              'Indicadores de Endividamento',
              'Balanço Patrimonial',
              'Demonstrativo de Resultados']

    # # Print the panels.
    with console.pager(styles=True) as screen:
        console.print('Python Fundamentus')

        for panel, title in zip(panels, titles):
            console.print(Panel(title=title,
                                renderable=Columns(panel, expand=True),
                                box=box.HEAVY_EDGE,
                                expand=True))

        console.print(
            'Created by Alexsander Lopes Camargos - https://github.com/alexcamargos/pyFundamentus'
        )
