#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: run.py
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

"""
Python Fundamentus is a Python API that allows you to quickly access the main
fundamental indicators of the main stocks in the Brazilian market.
"""

import fundamentus

TITLES = [
    'Cotações', 'Informações Básicas', 'Oscilações',
    'Indicadores de Valuation', 'Indicadores de Rentabilidade',
    'Indicadores de Endividamento', 'Balanço Patrimonial',
    'Demonstrativo de Resultados'
]

# pylint: disable=line-too-long
if __name__ == '__main__':
    URL = 'https://www.fundamentus.com.br/detalhes.php'
    PAYLOAD = {'papel': 'VALE3', 'interface': 'mobile'}

    main_pipeline = fundamentus.Pipeline(url=URL, params=PAYLOAD)
    response = main_pipeline.get_stock_information()

    # Extract the information from the response.
    price_information = response.transformed_information['price_information']
    detailed_information = response.transformed_information[
        'detailed_information']
    oscillations = response.transformed_information['oscillations']
    valuation_indicators = response.transformed_information[
        'valuation_indicators']
    profitability_indicators = response.transformed_information[
        'profitability_indicators']
    indebtedness_indicators = response.transformed_information[
        'indebtedness_indicators']
    balance_sheet = response.transformed_information['balance_sheet']
    income_statement = response.transformed_information['income_statement']

    print(TITLES[0])
    print('-' * len(TITLES[0]))
    for information in price_information:
        print(
            f'{price_information[information].title}: {price_information[information].value}'
        )

    print(f'\n{TITLES[1]}')
    print('-' * len(TITLES[1]))
    for information in detailed_information:
        if information != 'variation_52_weeks':
            print(
                f'{detailed_information[information].title}: {detailed_information[information].value}'
            )
        else:
            for sub_information in detailed_information[information]:
                print(
                    f'{detailed_information[information][sub_information].title}: {detailed_information[information][sub_information].value}'
                )

    print(f'\n{TITLES[2]}')
    print('-' * len(TITLES[2]))
    for information in oscillations:
        print(
            f'{oscillations[information].title}: {oscillations[information].value}'
        )

    print(f'\n{TITLES[3]}')
    print('-' * len(TITLES[3]))
    for information in valuation_indicators:
        print(
            f'{valuation_indicators[information].title}: {valuation_indicators[information].value}'
        )

    print(f'\n{TITLES[4]}')
    print('-' * len(TITLES[4]))
    for information in profitability_indicators:
        print(
            f'{profitability_indicators[information].title}: {profitability_indicators[information].value}'
        )

    print(f'\n{TITLES[5]}')
    print('-' * len(TITLES[5]))
    for information in indebtedness_indicators:
        print(
            f'{indebtedness_indicators[information].title}: {indebtedness_indicators[information].value}'
        )

    print(f'\n{TITLES[6]}')
    print('-' * len(TITLES[6]))
    for information in balance_sheet:
        print(
            f'{balance_sheet[information].title}: {balance_sheet[information].value}'
        )

    print(f'\n{TITLES[7]}')
    print('-' * len(TITLES[7]))
    print('Últimos 03 meses')
    for information in income_statement['three_months']:
        print(
            f"\t{income_statement['three_months'][information].title}: {income_statement['three_months'][information].value}"
        )
    print('Últimos 12 meses')
    for information in income_statement['twelve_months']:
        print(
            f"\t{income_statement['twelve_months'][information].title}: {income_statement['twelve_months'][information].value}"
        )
