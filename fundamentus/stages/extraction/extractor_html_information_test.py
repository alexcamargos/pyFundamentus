#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extractor_html_information_test.py
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

"""Test of extractor HTML Information."""

from fundamentus.contracts.extract_contract import ExtractContract
from fundamentus.drivers.html_collector import HtmlCollector
from fundamentus.drivers.http_requester import HttpRequester
from fundamentus.drivers.mocks.html_collector import HTML_COLLECTOR_MOCK
from fundamentus.stages.extraction.extractor_html_information import \
    ExtractorHtmlInformation


def test_extract_html_information(requests_mock) -> None:
    """Test extractor html information.

    :param requests_mock (Mock): Mock requests.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'papel': 'MGLU3'}

    requests_mock.get(url=url,
                      status_code=HTML_COLLECTOR_MOCK['status_code'],
                      text=HTML_COLLECTOR_MOCK['content'])

    requester = HttpRequester(url=url, params=payload)
    collector = HtmlCollector()

    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    response = extractor.extract()

    assert isinstance(response, ExtractContract)
    assert isinstance(response.extraction_date, int)
    assert isinstance(response.raw_information, dict)

    assert [
        'cotacao', 'informacoes_basicas', 'oscilacoes',
        'indicadores_de_valuation', 'indicadores_de_rentabilidade',
        'indicadores_de_endividamento', 'balanco_patrimonial',
        'demonstrativo_de_resultados'
    ] == list(response.raw_information.keys())

    assert [
        'cotacao', 'ultima_cotação', 'minino_52_semanas', 'maximo_52_semanas'
    ] == list(response.raw_information['cotacao'].keys())

    assert [
        'trading_code', 'empresa', 'tipo', 'setor', 'subsetor', 'valor_de_mercado',
        'valor_da_firma', 'numero_de_acoes', 'data_ultimo_balanço',
        'volume_negociacoes_2_meses'
    ] == list(response.raw_information['informacoes_basicas'].keys())

    assert [
        'dia', 'mes', '30_dias', '12_meses', '2022', '2021', '2020', '2019',
        '2018', '2017'
    ] == list(response.raw_information['oscilacoes'].keys())

    assert [
        'preco_sobre_lucro', 'preco_sobre_valor_patrimonial',
        'preco_sobre_ebit', 'preco_sobre_ativos',
        'preco_sobre_ativo_circulante_liquido', 'preco_sobre_capital_giro',
        'lucro_por_acao', 'valor_patrimonial_por_acao', 'price_sales_ratio',
        'dividend_yield', 'enterprise_value_sobre_ebitda',
        'enterprise_value_sobre_ebit'
    ] == list(response.raw_information['indicadores_de_valuation'].keys())

    assert [
        'return_invested_capital', 'return_on_equity',
        'ebit_sobre_ativos_totais', 'crescimento_receita_liquida_5_anos',
        'giro_ativos', 'margem_bruta', 'margem_ebit', 'margem_liquida'
    ] == list(response.raw_information['indicadores_de_rentabilidade'].keys())

    assert ['liquidez_corrente', 'divida_bruta_total'] == list(
        response.raw_information['indicadores_de_endividamento'].keys())

    assert [
        'ativo', 'divida_bruta', 'disponibilidades', 'divida_líquida',
        'ativo_circulante', 'patrimonio_Liquido'
    ] == list(response.raw_information['balanco_patrimonial'].keys())

    assert ['12_meses', '3_meses'] == list(
        response.raw_information['demonstrativo_de_resultados'].keys())

    assert [
        'receita_liquida_ultimos_12_meses', 'ebit_ultimos_12_meses',
        'lucro_liquido_ultimos_12_meses'
    ] == list(response.raw_information['demonstrativo_de_resultados']
              ['12_meses'].keys())

    assert [
        'receita_liquida_ultimos_3_meses', 'ebit_ultimos_3_meses',
        'lucro_liquido_ultimos_3_meses'
    ] == list(response.raw_information['demonstrativo_de_resultados']
              ['3_meses'].keys())
