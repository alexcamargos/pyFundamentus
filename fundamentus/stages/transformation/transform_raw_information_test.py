#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: transform_raw_information_test.py
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

# pylint: disable=R0801 # Disable warning: Similar lines in 2 files
"""Test of transform raw information from the HTTP requester."""

from fundamentus.contracts.mocks.extract_contract import extract_contract_mock
from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.exceptions.transform_exception import TransformException

from .transform_raw_information import TransformRawInformation


def test_transform_raw_information() -> None:
    """Test of transform raw information from the HTTP requester."""

    transform = TransformRawInformation()
    transformed = transform.transform_information(extract_contract_mock)

    assert isinstance(transformed, TransformContract)
    assert isinstance(transformed.transformed_information, dict)

    assert [
        'cotacao', 'informacoes_basicas', 'oscilacoes',
        'indicadores_de_valuation', 'indicadores_de_rentabilidade',
        'indicadores_de_endividamento', 'balanco_patrimonial',
        'demonstrativo_de_resultados'
    ] == list(transformed.transformed_information.keys())

    assert [
        'cotacao', 'ultima_cotação', 'minino_52_semanas', 'maximo_52_semanas'
    ] == list(transformed.transformed_information['cotacao'].keys())

    assert [
        'ativo', 'empresa', 'tipo', 'setor', 'subsetor', 'valor_de_mercado',
        'valor_da_firma', 'numero_de_acoes', 'data_ultimo_balanço',
        'volume_negociacoes_2_meses'
    ] == list(
        transformed.transformed_information['informacoes_basicas'].keys())

    assert [
        'dia', 'mes', '30_dias', '12_meses', '2022', '2021', '2020', '2019',
        '2018', '2017'
    ] == list(transformed.transformed_information['oscilacoes'].keys())

    assert [
        'preco_sobre_lucro', 'preco_sobre_valor_patrimonial',
        'preco_sobre_ebit', 'preco_sobre_ativos',
        'preco_sobre_ativo_circulante_liquido', 'preco_sobre_capital_giro',
        'lucro_por_acao', 'valor_patrimonial_por_acao', 'price_sales_ratio',
        'dividend_yield', 'enterprise_value_sobre_ebitda',
        'enterprise_value_sobre_ebit'
    ] == list(
        transformed.transformed_information['indicadores_de_valuation'].keys())

    assert [
        'return_invested_capital', 'return_on_equity',
        'ebit_sobre_ativos_totais', 'crescimento_receita_liquida_5_anos',
        'giro_ativos', 'margem_bruta', 'margem_ebit', 'margem_liquida'
    ] == list(transformed.
              transformed_information['indicadores_de_rentabilidade'].keys())

    assert ['liquidez_corrente', 'divida_bruta_total'] == list(
        transformed.transformed_information['indicadores_de_endividamento'].
        keys())

    assert [
        'ativo', 'divida_bruta', 'disponibilidades', 'divida_líquida',
        'ativo_circulante', 'patrimonio_Liquido'
    ] == list(
        transformed.transformed_information['balanco_patrimonial'].keys())

    assert ['12_meses', '3_meses'] == list(
        transformed.transformed_information['demonstrativo_de_resultados'].
        keys())

    assert [
        'receita_liquida_ultimos_12_meses', 'ebit_ultimos_12_meses',
        'lucro_liquido_ultimos_12_meses'
    ] == list(
        transformed.transformed_information['demonstrativo_de_resultados']
        ['12_meses'].keys())

    assert [
        'receita_liquida_ultimos_3_meses', 'ebit_ultimos_3_meses',
        'lucro_liquido_ultimos_3_meses'
    ] == list(
        transformed.transformed_information['demonstrativo_de_resultados']
        ['3_meses'].keys())


def test_transform_raw_information_exception() -> None:
    """Test of transform raw information from the HTTP requester.

    This test should raise an exception because the raw
    information is not a valid.

    :raises: TransformException
    """

    transform = TransformRawInformation()

    try:
        transformed = transform.transform_information([])  # pylint: disable=unused-variable
    except TransformException as exception:
        assert isinstance(exception, TransformException)
