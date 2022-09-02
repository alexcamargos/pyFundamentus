#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: command_line_interface.py
#  Version: 0.0.1
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

from rich import print as rprint

from fundamentus.main.fundamentus_pipeline import \
    FundamentusPipeline as Fundamentus
from fundamentus.utils.indicator_names import INDICATOR_NAME


def main(ticker: str) -> dict:
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

    parser = argparse.ArgumentParser(
        description=
        'Python Fundamentus is a Python API that allows you to quickly '
        'access the main fundamental indicators of the main stocks in the Brazilian market.'
    )
    parser.add_argument('ticker',
                        help='Ticker of the stock',
                        type=str,
                        nargs=1,
                        metavar='TICKER',
                        default='MGLU3')
    args = parser.parse_args()

    information = main(ticker=args.ticker)

    # Extract the information from the response.
    cotacao = information.transformed_information['cotacao']
    informacoes_basicas = information.transformed_information[
        'informacoes_basicas']
    oscilacoes = information.transformed_information['oscilacoes']
    indicadores_de_valuation = information.transformed_information[
        'indicadores_de_valuation']
    indicadores_de_rentabilidade = information.transformed_information[
        'indicadores_de_rentabilidade']
    indicadores_de_endividamento = information.transformed_information[
        'indicadores_de_endividamento']
    balanco_patrimonial = information.transformed_information[
        'balanco_patrimonial']
    demonstrativo_de_resultados = information.transformed_information[
        'demonstrativo_de_resultados']

    # Print the information.
    rprint('[bold blue]Cotação[/bold blue]')
    for key, value in cotacao.items():
        rprint(f'\t{INDICATOR_NAME[key]}: {value}')

    rprint('\n[bold blue]Informações Básicas[/bold blue]')
    for key, value in informacoes_basicas.items():
        rprint(f'\t{INDICATOR_NAME[key]}: {value}')

    rprint('\n[bold blue]Oscilações[/bold blue]')
    for key, value in oscilacoes.items():
        rprint(f'\t{INDICATOR_NAME[key]}: {value}')

    rprint('\n[bold blue]Indicadores de Valuation[/bold blue]')
    for key, value in indicadores_de_valuation.items():
        rprint(f'\t{INDICATOR_NAME[key]}: {value}')

    rprint('\n[bold blue]Indicadores de Rentabilidade[/bold blue]')
    for key, value in indicadores_de_rentabilidade.items():
        rprint(f'\t{INDICATOR_NAME[key]}: {value}')

    rprint('\n[bold blue]Indicadores de Endividamento[/bold blue]')
    for key, value in indicadores_de_endividamento.items():
        rprint(f'\t{INDICATOR_NAME[key]}: {value}')

    rprint('[bold blue]Balanço Patrimonial[/bold blue]')
    for key, value in balanco_patrimonial.items():
        rprint(f'\t{INDICATOR_NAME[key]}: {value}')

    rprint('\n[bold blue]Demonstrativo de Resultados[/bold blue]')
    rprint('\t[bold blue]Últimos 03 meses[/bold blue]')
    for key, value in demonstrativo_de_resultados['3_meses'].items():
        rprint(f'\t{INDICATOR_NAME[key]}: {value}')

    rprint('\b[bold blue]Demonstrativo de Resultados[/bold blue]')
    rprint('\t[bold blue]Últimos 12 meses[/bold blue]')
    for key, value in demonstrativo_de_resultados['12_meses'].items():
        rprint(f'\t{INDICATOR_NAME[key]}: {value}')
