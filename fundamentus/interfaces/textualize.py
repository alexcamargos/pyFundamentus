# #!/usr/bin/env python
# # encoding: utf-8

# # ------------------------------------------------------------------------------
# #  Name: textualize.py
# #  Version: 0.0.1
# #
# #  Summary: Python Fundamentus
# #           Python Fundamentus is a Python API that allows you to quickly
# #           access the main fundamental indicators of the main stocks
# #           in the Brazilian market.
# #
# #  Author: Alexsander Lopes Camargos
# #  Author-email: alcamargos@vivaldi.net
# #
# #  License: MIT
# # ------------------------------------------------------------------------------

from rich.table import Table

from fundamentus.utils.indicator_names import INDICATOR_NAME


#pylint: disable=too-many-locals
def get_tables(information: dict) -> Table:
    """Create tables with the main fundamental indicators.

    :param information (dict): Dictionary with the main fundamental indicators.
    :return: Table with the main fundamental indicators.
    """

    tables = []

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

    table_cotacao = Table(show_header=False)
    for key, value in cotacao.items():
        table_cotacao.add_row(f'{INDICATOR_NAME[key]}', f'{value}')
    tables.append(table_cotacao)

    table_informacoes_basicas = Table(show_header=False)
    for key, value in informacoes_basicas.items():
        table_informacoes_basicas.add_row(f'{INDICATOR_NAME[key]}', f'{value}')
    tables.append(table_informacoes_basicas)

    table_oscilacoes = Table(show_header=False)
    for key, value in oscilacoes.items():
        table_oscilacoes.add_row(f'{INDICATOR_NAME[key]}', f'{value}')
    tables.append(table_oscilacoes)

    table_indicadores_de_valuation = Table(show_header=False)
    for key, value in indicadores_de_valuation.items():
        table_indicadores_de_valuation.add_row(f'{INDICATOR_NAME[key]}',
                                               f'{value}')
    tables.append(table_indicadores_de_valuation)

    table_indicadores_de_rentabilidade = Table(show_header=False)
    for key, value in indicadores_de_rentabilidade.items():
        table_indicadores_de_rentabilidade.add_row(f'{INDICATOR_NAME[key]}',
                                                   f'{value}')
    tables.append(table_indicadores_de_rentabilidade)

    table_indicadores_de_endividamento = Table(show_header=False)
    for key, value in indicadores_de_endividamento.items():
        table_indicadores_de_endividamento.add_row(f'{INDICATOR_NAME[key]}',
                                                   f'{value}')
    tables.append(table_indicadores_de_endividamento)

    table_balanco_patrimonial = Table(show_header=False)
    for key, value in balanco_patrimonial.items():
        table_balanco_patrimonial.add_row(f'{INDICATOR_NAME[key]}', f'{value}')
    tables.append(table_balanco_patrimonial)

    table_demonstrativo_de_resultados_3_meses = Table(show_header=False)
    for key, value in demonstrativo_de_resultados['3_meses'].items():
        table_demonstrativo_de_resultados_3_meses.add_row(
            f'{INDICATOR_NAME[key]}', f'{value}')
    tables.append(table_demonstrativo_de_resultados_3_meses)

    table_demonstrativo_de_resultados_12_meses = Table(show_header=False)
    for key, value in demonstrativo_de_resultados['12_meses'].items():
        table_demonstrativo_de_resultados_12_meses.add_row(
            f'{INDICATOR_NAME[key]}', f'{value}')
    tables.append(table_demonstrativo_de_resultados_12_meses)

    return tables
