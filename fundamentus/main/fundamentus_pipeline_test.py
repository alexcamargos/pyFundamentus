#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: fundamentus_pipeline.py
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

"""Test the FundamentusPipeline."""

from fundamentus.contracts.transform_contract import TransformContract

from .fundamentus_pipeline import FundamentusPipeline


def test_get_stock_information() -> None:
    """Test the get_stock_information method."""

    url = 'https://www.fundamentus.com.br/detalhes.php'
    params = {'papel': 'PETR4'}

    main_pipeline = FundamentusPipeline(url=url, params=params)
    response = main_pipeline.get_stock_information()

    assert isinstance(response, TransformContract)
    assert isinstance(response.transformed_information, dict)
    assert isinstance(response.transformed_information['cotacao'], dict)
    assert isinstance(response.transformed_information['informacoes_basicas'],
                      dict)
    assert isinstance(response.transformed_information['oscilacoes'], dict)
    assert isinstance(
        response.transformed_information['indicadores_de_valuation'], dict)
    assert isinstance(
        response.transformed_information['indicadores_de_rentabilidade'], dict)
    assert isinstance(
        response.transformed_information['indicadores_de_endividamento'], dict)
    assert isinstance(response.transformed_information['balanco_patrimonial'],
                      dict)
    assert isinstance(
        response.transformed_information['demonstrativo_de_resultados'], dict)
