#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: textualize.py
#  Version: 0.0.6
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

from decimal import Decimal

from rich.panel import Panel
from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.main.fundamentus_pipeline import \
    FundamentusPipeline as Fundamentus
from fundamentus.utils.indicator_names import INDICATOR_NAME


def get_information(ticker: str) -> TransformContract:
    """Main function.

    :param ticker (string): Stock ticker.
    :return: Dictionary with the main fundamental indicators.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    params = {'papel': ticker}

    main_pipeline = Fundamentus(url=url, params=params)
    response = main_pipeline.get_stock_information()

    return response


#pylint: disable=too-many-locals
#pylint: disable=too-many-branches
#pylint: disable=too-many-statements
def create_panels(ticker: str) -> list:
    """Get panels with the main fundamental indicators.

    :param ticker (string): Stock ticker.
    :return: List of panels.
    """

    # Get the stock information.
    information = get_information(ticker)

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

    # Create the panels with the main fundamental indicators.

    # Panel with the main information.
    panel_main_information = []
    for key, value in cotacao.items():
        if isinstance(value, Decimal) and value.is_signed():
            value = f'[red]{value:,}[/red]'
        elif isinstance(value, Decimal):
            value = f'[green]{value:,}[/green]'

        if key in ['cotacao', 'minino_52_semanas', 'maximo_52_semanas']:
            value = f'R${value}'

        panel_main_information.append(
            Panel(f'{value}',
                  title=INDICATOR_NAME[key],
                  title_align='left',
                  expand=True))

    # Panel with the basic information.
    panel_basic_information = []
    for key, value in informacoes_basicas.items():
        if isinstance(value, Decimal) and value.is_signed():
            value = f'[red]{value:,}[/red]'
        elif isinstance(value, Decimal):
            value = f'[green]{value:,}[/green]'

        if key in ['valor_de_mercado', 'valor_da_firma']:
            value = f'R${value}'

        panel_basic_information.append(
            Panel(f'{value}',
                  title=INDICATOR_NAME[key],
                  title_align='left',
                  expand=True))

    # Panel with the oscillations.
    panel_oscillations = []
    for key, value in oscilacoes.items():
        if isinstance(value, Decimal) and value.is_signed():
            value = f'[red]{value * 100:.2f}%[/red]'
        elif isinstance(value, Decimal):
            value = f'[green]{value * 100:.2f}%[/green]'

        panel_oscillations.append(
            Panel(f'{value}',
                  title=INDICATOR_NAME[key],
                  title_align='left',
                  expand=True))

    # Panel with the valuation indicators.
    panel_valuation_indicators = []
    for key, value in indicadores_de_valuation.items():
        if isinstance(value, Decimal) and value.is_signed():
            value = f'[red]{value:,}[/red]'
        elif isinstance(value, Decimal):
            value = f'[green]{value:,}[/green]'

        panel_valuation_indicators.append(
            Panel(f'{value}',
                  title=INDICATOR_NAME[key],
                  title_align='left',
                  expand=True))

    # Panel with the profitability indicators.
    panel_profitability_indicators = []
    for key, value in indicadores_de_rentabilidade.items():
        if key in [
                'margem_bruta', 'margem_ebit', 'margem_liquida',
                'crescimento_receita_liquida_5_anos'
        ]:
            value = f'{value * 100:.2f}%'

        if isinstance(value, Decimal) and value.is_signed():
            value = f'[red]{value:,}[/red]'
        elif isinstance(value, Decimal):
            value = f'[green]{value:,}[/green]'

        panel_profitability_indicators.append(
            Panel(f'{value}',
                  title=INDICATOR_NAME[key],
                  title_align='left',
                  expand=True))

    # Panel with the debt indicators.
    panel_debt_indicators = []
    for key, value in indicadores_de_endividamento.items():
        if isinstance(value, Decimal) and value.is_signed():
            value = f'[red]{value:,}[/red]'
        elif isinstance(value, Decimal):
            value = f'[green]{value:,}[/green]'

        panel_debt_indicators.append(
            Panel(f'{value}',
                  title=INDICATOR_NAME[key],
                  title_align='left',
                  expand=True))

    # Panel with the balance sheet.
    panel_balance_sheet = []
    for key, value in balanco_patrimonial.items():
        if isinstance(value, Decimal) and value.is_signed():
            value = f'R$[red]{value:,}[/red]'
        elif isinstance(value, Decimal):
            value = f'R$[green]{value:,}[/green]'

        panel_balance_sheet.append(
            Panel(f'{value}',
                  title=INDICATOR_NAME[key],
                  title_align='left',
                  expand=True))

    # Panel with the income statement 03 months.
    panel_income_statement_03_months = []
    for key, value in demonstrativo_de_resultados['3_meses'].items():
        if isinstance(value, Decimal) and value.is_signed():
            value = f'R$[red]{value:,}[/red]'
        elif isinstance(value, Decimal):
            value = f'R$[green]{value:,}[/green]'

        panel_income_statement_03_months.append(
            Panel(f'{value}',
                  title=INDICATOR_NAME[key],
                  title_align='left',
                  expand=True))

    # Panel with the income statement 12 months.
    panel_income_statement_12_months = []
    for key, value in demonstrativo_de_resultados['12_meses'].items():
        if isinstance(value, Decimal) and value.is_signed():
            value = f'R$[red]{value:,}[/red]'
        elif isinstance(value, Decimal):
            value = f'R$[green]{value:,}[/green]'

        panel_income_statement_12_months.append(
            Panel(f'{value}',
                  title=INDICATOR_NAME[key],
                  title_align='left',
                  expand=True))

    return [
        panel_main_information,
        panel_basic_information,
        panel_oscillations,
        panel_valuation_indicators,
        panel_profitability_indicators,
        panel_debt_indicators,
        panel_balance_sheet,
        panel_income_statement_03_months,
        panel_income_statement_12_months
    ]
