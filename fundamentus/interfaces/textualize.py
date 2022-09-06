# #!/usr/bin/env python
# # encoding: utf-8

# # ------------------------------------------------------------------------------
# #  Name: textualize.py
# #  Version: 0.0.
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

from rich.panel import Panel

from fundamentus.utils.indicator_names import INDICATOR_NAME


#pylint: disable=too-many-locals
def get_panels(information: dict) -> list:
    """Get panels with the main fundamental indicators.

    :param information (dict): Dictionary with the main fundamental indicators.
    :return: List with the main fundamental indicators.
    """

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

    panels = []

    for key, value in cotacao.items():
        panels.append(Panel(f'{value}', title=INDICATOR_NAME[key],
                            expand=True))

    for key, value in informacoes_basicas.items():
        panels.append(Panel(f'{value}', title=INDICATOR_NAME[key],
                            expand=True))

    for key, value in oscilacoes.items():
        panels.append(Panel(f'{value}', title=INDICATOR_NAME[key],
                            expand=True))

    for key, value in indicadores_de_valuation.items():
        panels.append(Panel(f'{value}', title=INDICATOR_NAME[key],
                            expand=True))

    for key, value in indicadores_de_rentabilidade.items():
        panels.append(Panel(f'{value}', title=INDICATOR_NAME[key],
                            expand=True))

    for key, value in indicadores_de_endividamento.items():
        panels.append(Panel(f'{value}', title=INDICATOR_NAME[key],
                            expand=True))

    for key, value in balanco_patrimonial.items():
        panels.append(Panel(f'{value}', title=INDICATOR_NAME[key],
                            expand=True))

    for key, value in demonstrativo_de_resultados['3_meses'].items():
        panels.append(Panel(f'{value}', title=INDICATOR_NAME[key],
                            expand=True))

    for key, value in demonstrativo_de_resultados['12_meses'].items():
        panels.append(Panel(f'{value}', title=INDICATOR_NAME[key],
                            expand=True))

    return panels
