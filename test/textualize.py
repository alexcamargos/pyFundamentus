#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: textualize.py
#  Version: 0.0.11
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
"""Rich's Fundamentus Command line interface."""

import sys

from decimal import Decimal

from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table

from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.exceptions.extract_exception import ExtractException
from fundamentus import Pipeline as Fundamentus


def list_all_companies() -> Table:
    """List all companies.

    :return: Table with all companies.
    """

    main_pipeline = Fundamentus()
    response = main_pipeline.list_all_companies()

    # Table with information of all companies.
    table = Table(title='Todas as Empresas Disponíveis', show_header=True, expand=True)
    table.add_column('Código', style='cyan', vertical='middle', no_wrap=True)
    table.add_column('Nome', style='cyan', vertical='middle', no_wrap=True)
    table.add_column('Razão Social',
                     style='cyan',
                     vertical='middle',
                     no_wrap=True)

    for company in response[0]:
        table.add_row(company['code'], company['name'],
                      company['corporate_name'])

    return table


def list_all_property_funds() -> Table:
    """List all companies.

    :return: Table with all property funds.
    """

    main_pipeline = Fundamentus()
    response = main_pipeline.list_all_property_funds()

    # Table with information of all companies.
    table = Table(title='Todos os Fundos Imobiliários', show_header=True, expand=True)
    table.add_column('Código', style='cyan', vertical='middle', no_wrap=True)
    table.add_column('Nome', style='cyan', vertical='middle', no_wrap=True)

    for company in response[0]:
        table.add_row(company['code'], company['name'])

    return table


def get_all_information(ticker: str) -> TransformContract:
    """Main function.

    :param ticker (string): Stock ticker.
    :return: Dictionary with the main fundamental indicators.
    """

    main_pipeline = Fundamentus(ticker)

    try:
        response = main_pipeline.get_all_information()
    except ExtractException:
        print('Python Fundamentus\n')
        print(
            f"O código '{ticker}' não corresponde a nenhuma ação conhecida no mercado brasileiro.\n")
        print('Por favor, verifique o código e tente novamente.\n')
        sys.exit(0)

    return response


# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
def list_all_fundamental_indicators(ticker: str) -> list:
    """Get panels with the main fundamental indicators.

    :param ticker (string): Stock ticker.
    :return: List of panels.
    """

    # Get the stock information.
    information = get_all_information(ticker)

    # Extract the information from the response.
    stock_identification = information.transformed_information[
        'stock_identification']
    price_information = information.transformed_information[
        'price_information']
    financial_summary = information.transformed_information[
        'financial_summary']
    detailed_information = information.transformed_information[
        'detailed_information']
    oscillations = information.transformed_information['oscillations']
    valuation_indicators = information.transformed_information[
        'valuation_indicators']
    profitability_indicators = information.transformed_information[
        'profitability_indicators']
    indebtedness_indicators = information.transformed_information[
        'indebtedness_indicators']
    balance_sheet = information.transformed_information['balance_sheet']
    income_statement = information.transformed_information['income_statement']

    # Create the panels with the main fundamental indicators.

    # Panel with the main information.
    panel_main_information = []
    for key in stock_identification.keys():

        if stock_identification[key].title == 'Código':
            value = f'[blue]{stock_identification[key].value}[/blue]'
        else:
            value = stock_identification[key].value

        panel_main_information.append(
            Panel(value,
                  title=stock_identification[key].title,
                  title_align='left',
                  expand=True))

    for key in price_information.keys():

        if isinstance(price_information[key].value,
                      Decimal) and price_information[key].value.is_signed():
            value = f'[red]R${price_information[key].value:,}[/red]'
        elif isinstance(price_information[key].value, Decimal):
            value = f'[green]R${price_information[key].value:,}[/green]'
        else:
            value = price_information[key].value

        panel_main_information.append(
            Panel(f'{value}',
                  title=price_information[key].title,
                  title_align='left',
                  expand=True))

    # Panel with the financial summary information.
    panel_financial_summary = []
    for key in financial_summary.keys():

        if isinstance(financial_summary[key].value, Decimal):
            value = f'{financial_summary[key].value:,}'
        else:
            value = financial_summary[key].value

        panel_financial_summary.append(
            Panel(f'{value}',
                  title=financial_summary[key].title,
                  title_align='left',
                  expand=True))

    # Panel with the basic information.
    panel_basic_information = []
    for key in detailed_information.keys():

        if key != 'variation_52_weeks':
            if isinstance(
                    detailed_information[key].value,
                    Decimal) and detailed_information[key].value.is_signed():
                value = f'[red]{detailed_information[key].value:,}[/red]'
            elif isinstance(detailed_information[key].value, Decimal):
                value = f'[green]{detailed_information[key].value:,}[/green]'
            else:
                value = detailed_information[key].value

            panel_basic_information.append(
                Panel(f'{value}',
                      title=detailed_information[key].title,
                      title_align='left',
                      expand=True))
        else:
            for sub_key in detailed_information[key]:
                if isinstance(
                        detailed_information[key][sub_key].value, Decimal
                ) and detailed_information[key][sub_key].value.is_signed():
                    value = f'[red]{detailed_information[key][sub_key].value:,}[/red]'
                elif isinstance(detailed_information[key][sub_key].value,
                                Decimal):
                    value = f'[green]{detailed_information[key][sub_key].value:,}[/green]'
                else:
                    value = detailed_information[key][sub_key].value

                panel_basic_information.append(
                    Panel(f'{value}',
                          title=detailed_information[key][sub_key].title,
                          title_align='left',
                          expand=True))

    # Panel with the oscillations.
    panel_oscillations = []
    for key in oscillations.keys():
        if isinstance(oscillations[key].value,
                      Decimal) and oscillations[key].value.is_signed():
            value = f'[red]{oscillations[key].value * 100:.2f}%[/red]'
        else:
            value = f'[green]{oscillations[key].value * 100:.2f}%[/green]'

        panel_oscillations.append(
            Panel(f'{value}',
                  title=oscillations[key].title,
                  title_align='left',
                  expand=True))

    # Panel with the valuation indicators.
    panel_valuation_indicators = []
    for key in valuation_indicators.keys():
        if isinstance(valuation_indicators[key].value,
                      Decimal) and valuation_indicators[key].value.is_signed():
            value = f'[red]{valuation_indicators[key].value:,}[/red]'
        elif isinstance(valuation_indicators[key].value, Decimal):
            value = f'[green]{valuation_indicators[key].value:,}[/green]'
        else:
            value = valuation_indicators[key].value

        panel_valuation_indicators.append(
            Panel(f'{value}',
                  title=valuation_indicators[key].title,
                  title_align='left',
                  expand=True))

    # Panel with the profitability indicators.
    panel_profitability_indicators = []
    for key in profitability_indicators.keys():
        if key not in [
                'ebit_divided_by_total_assets',
                'net_revenue_divided_by_total_assets'
        ]:
            value = f'{profitability_indicators[key].value * 100:.2f}%'
        else:
            value = f'{profitability_indicators[key].value:.2f}'

        if isinstance(
                profitability_indicators[key].value,
                Decimal) and profitability_indicators[key].value.is_signed():
            value = f'[red]{value}[/red]'
        elif isinstance(profitability_indicators[key].value, Decimal):
            value = f'[green]{value}[/green]'

        panel_profitability_indicators.append(
            Panel(f'{value}',
                  title=profitability_indicators[key].title,
                  title_align='left',
                  expand=True))

    # Panel with the debt indicators.
    panel_debt_indicators = []
    for key in indebtedness_indicators.keys():
        if isinstance(
                indebtedness_indicators[key].value,
                Decimal) and indebtedness_indicators[key].value.is_signed():
            value = f'[red]{indebtedness_indicators[key].value:,}[/red]'
        elif isinstance(indebtedness_indicators[key].value, Decimal):
            value = f'[green]{indebtedness_indicators[key].value:,}[/green]'
        else:
            value = indebtedness_indicators[key].value

        panel_debt_indicators.append(
            Panel(f'{value}',
                  title=indebtedness_indicators[key].title,
                  title_align='left',
                  expand=True))

    # Panel with the balance sheet.
    panel_balance_sheet = []
    for key in balance_sheet.keys():
        if isinstance(balance_sheet[key].value,
                      Decimal) and balance_sheet[key].value.is_signed():
            value = f'[red]R${balance_sheet[key].value:,}[/red]'
        elif isinstance(balance_sheet[key].value, Decimal):
            value = f'[green]R${balance_sheet[key].value:,}[/green]'
        else:
            value = balance_sheet[key].value

        panel_balance_sheet.append(
            Panel(f'{value}',
                  title=balance_sheet[key].title,
                  title_align='left',
                  expand=True))

    # Panel with the income statement 03 months.
    panel_income_statement_03_months = []
    for key in income_statement['three_months'].keys():
        if isinstance(
                income_statement['three_months'][key].value, Decimal
        ) and income_statement['three_months'][key].value.is_signed():
            value = f"[red]R${income_statement['three_months'][key].value:,}[/red]"
        elif isinstance(income_statement['three_months'][key].value, Decimal):
            value = f"[green]R${income_statement['three_months'][key].value:,}[/green]"
        else:
            value = income_statement['three_months'][key].value

        panel_income_statement_03_months.append(
            Panel(f'{value}',
                  title=income_statement['three_months'][key].title,
                  title_align='left',
                  expand=True))

    # Panel with the income statement 12 months.
    panel_income_statement_12_months = []
    for key in income_statement['twelve_months'].keys():
        if isinstance(
                income_statement['twelve_months'][key].value, Decimal
        ) and income_statement['twelve_months'][key].value.is_signed():
            value = f"[red]R${income_statement['twelve_months'][key].value:,}[/red]"
        elif isinstance(income_statement['twelve_months'][key].value, Decimal):
            value = f"[green]R${income_statement['twelve_months'][key].value:,}[/green]"
        else:
            value = income_statement['twelve_months'][key].value

        panel_income_statement_12_months.append(
            Panel(f'{value}',
                  title=income_statement['twelve_months'][key].title,
                  title_align='left',
                  expand=True))

    # Join Panel panel_income_statement_03_months and panel_income_statement_12_months.
    panel_income_statement = [
        Panel(renderable=Columns(panel_income_statement_03_months),
              title='Últimos 03 meses',
              title_align='left',
              expand=True),
        Panel(renderable=Columns(panel_income_statement_12_months),
              title='Últimos 12 meses',
              title_align='left',
              expand=True)
    ]

    return [
        panel_main_information, panel_financial_summary, panel_basic_information,
        panel_oscillations, panel_valuation_indicators, panel_profitability_indicators,
        panel_debt_indicators, panel_balance_sheet, panel_income_statement
    ]
