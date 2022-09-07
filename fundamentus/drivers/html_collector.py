#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: http_requester.py
#  Version: 0.0.2
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

"""HTTP Collector.

This module is responsible for collecting the HTML information from the response.

"""

from bs4 import BeautifulSoup as bs

from .interfaces.html_collector import HtmlCollectorInterface


# pylint: disable=too-few-public-methods
class HtmlCollector(HtmlCollectorInterface):
    """Represents a HTML collector."""

    # pylint: disable=too-many-locals
    # pylint: disable=too-many-statements
    def collect_information(self, html: str) -> dict:
        """Collect information from the html.

        param: html (str): HTML content.

        :return: dict: Dictionary with the collected information.
        """

        soup = bs(html, 'html.parser')

        tables = soup.find_all('table', {'class': 'w728'})

        # 0 - Informações básicas
        # 1 - Valor de mercado
        # 2 - Indicadores fundamentalistas
        # 3 - Balanço Patrimonial
        # 4 - Demonstrativos de resultados
        stocks_information, market_value, fundamentalist_indicators, \
            balance_sheet, demonstrative_results = tables

        # Extraindo as informações básicas a ação.
        stocks_information_data = stocks_information.find_all(
            'span', {'class': 'txt'})
        trading_code = stocks_information_data[1].text
        cotacao = stocks_information_data[3].text
        tipo = stocks_information_data[5].text
        data_ultima_cotacao = stocks_information_data[7].text
        empresa = stocks_information_data[9].text
        minino_52_semanas = stocks_information_data[11].text
        setor = stocks_information_data[13].text
        maximo_52_semanas = stocks_information_data[15].text
        subsetor = stocks_information_data[17].text
        volume_negociacoes_2_meses = stocks_information_data[19].text

        # Extraindo as informações de valor de mercado.
        market_value_data = market_value.find_all('span', {'class': 'txt'})
        valor_mercado = market_value_data[1].text
        data_ultimo_balanco_processado = market_value_data[3].text
        valor_firma = market_value_data[5].text
        numero_acoes = market_value_data[7].text

        # Extraindo as informações das oscilações da contação da ação.
        oscilacoes_indicators_data = fundamentalist_indicators.find_all(
            'span', {'class': 'oscil'})
        oscilacao_cotacao_dia = oscilacoes_indicators_data[0].text
        oscilacao_cotacao_mes = oscilacoes_indicators_data[1].text
        oscilacao_cotacao_30_dias = oscilacoes_indicators_data[2].text
        oscilacao_cotacao_12_meses = oscilacoes_indicators_data[3].text
        oscilacao_cotacao_2022 = oscilacoes_indicators_data[4].text
        oscilacao_cotacao_2021 = oscilacoes_indicators_data[5].text
        oscilacao_cotacao_2020 = oscilacoes_indicators_data[6].text
        oscilacao_cotacao_2019 = oscilacoes_indicators_data[7].text
        oscilacao_cotacao_2018 = oscilacoes_indicators_data[8].text
        oscilacao_cotacao_2017 = oscilacoes_indicators_data[9].text

        # Extraindo as informações dos indicadores fundamentalistas.
        fundamental_indicators_data = fundamentalist_indicators.find_all(
            'span', {'class': 'txt'})
        preco_sobre_lucro = fundamental_indicators_data[4].text
        lucro_por_acao = fundamental_indicators_data[6].text
        preco_sobre_valor_patrimonial = fundamental_indicators_data[9].text
        valor_patrimonial_por_acao = fundamental_indicators_data[11].text
        preco_sobre_ebit = fundamental_indicators_data[14].text
        margem_bruta = fundamental_indicators_data[16].text
        price_sales_ratio = fundamental_indicators_data[19].text
        margem_ebit = fundamental_indicators_data[21].text
        preco_sobre_ativos = fundamental_indicators_data[24].text
        margem_liquida = fundamental_indicators_data[26].text
        preco_sobre_capital_giro = fundamental_indicators_data[29].text
        ebit_sobre_ativos_totais = fundamental_indicators_data[31].text
        preco_sobre_ativo_circulante_liquido = fundamental_indicators_data[
            34].text
        return_invested_capital = fundamental_indicators_data[36].text
        dividend_yield = fundamental_indicators_data[39].text
        return_on_equity = fundamental_indicators_data[41].text
        enterprise_value_sobre_ebitda = fundamental_indicators_data[44].text
        liquidez_corrente = fundamental_indicators_data[46].text
        enterprise_value_sobre_ebit = fundamental_indicators_data[49].text
        divida_bruta_total = fundamental_indicators_data[51].text
        crescimento_receita_liquida_5_anos = fundamental_indicators_data[
            54].text
        giro_ativos = fundamental_indicators_data[56].text

        # Extraindo as informações do balanço patrimonial.
        balance_sheet_data = balance_sheet.find_all('span', {'class': 'txt'})
        ativo = balance_sheet_data[2].text
        divida_bruta = balance_sheet_data[4].text
        disponibilidades = balance_sheet_data[6].text
        divida_liquida = balance_sheet_data[8].text
        ativo_circulante = balance_sheet_data[10].text
        patrimonio_liquido = balance_sheet_data[12].text

        # Extraindo as informações dos demonstrativos de resultados.
        demonstrative_results_data = demonstrative_results.find_all(
            'span', {'class': 'txt'})
        # Últimos 12 meses.
        receita_liquida_ultimos_12_meses = demonstrative_results_data[4].text
        ebit_ultimos_12_meses = demonstrative_results_data[8].text
        lucro_liquido_ultimos_12_meses = demonstrative_results_data[12].text

        # Últimos 3 meses.
        receita_liquida_ultimos_3_meses = demonstrative_results_data[6].text
        ebit_ultimos_3_meses = demonstrative_results_data[10].text
        lucro_liquido_ultimos_3_meses = demonstrative_results_data[14].text

        cotacao = {
            'cotacao': cotacao,
            'ultima_cotação': data_ultima_cotacao,
            'minino_52_semanas': minino_52_semanas,
            'maximo_52_semanas': maximo_52_semanas,
        }

        informacoes_basicas = {
            'trading_code': trading_code,
            'empresa': empresa,
            'tipo': tipo,
            'setor': setor,
            'subsetor': subsetor,
            'valor_de_mercado': valor_mercado,
            'valor_da_firma': valor_firma,
            'numero_de_acoes': numero_acoes,
            'data_ultimo_balanço': data_ultimo_balanco_processado,
            'volume_negociacoes_2_meses': volume_negociacoes_2_meses,
        }

        oscilacoes = {
            'dia': oscilacao_cotacao_dia,
            'mes': oscilacao_cotacao_mes,
            '30_dias': oscilacao_cotacao_30_dias,
            '12_meses': oscilacao_cotacao_12_meses,
            '2022': oscilacao_cotacao_2022,
            '2021': oscilacao_cotacao_2021,
            '2020': oscilacao_cotacao_2020,
            '2019': oscilacao_cotacao_2019,
            '2018': oscilacao_cotacao_2018,
            '2017': oscilacao_cotacao_2017
        }

        indicadores_de_valuation = {
            'preco_sobre_lucro': preco_sobre_lucro,
            'preco_sobre_valor_patrimonial': preco_sobre_valor_patrimonial,
            'preco_sobre_ebit': preco_sobre_ebit,
            'price_sales_ratio': price_sales_ratio,
            'preco_sobre_ativos': preco_sobre_ativos,
            'preco_sobre_ativo_circulante_liquido':preco_sobre_ativo_circulante_liquido,
            'dividend_yield': dividend_yield,
            'enterprise_value_sobre_ebitda': enterprise_value_sobre_ebitda,
            'enterprise_value_sobre_ebit': enterprise_value_sobre_ebit,
            'preco_sobre_capital_giro': preco_sobre_capital_giro,
            'lucro_por_acao': lucro_por_acao,
            'valor_patrimonial_por_acao': valor_patrimonial_por_acao,
        }

        indicadores_de_rentabilidade = {
            'return_on_equity': return_on_equity,
            'return_invested_capital': return_invested_capital,
            'ebit_sobre_ativos_totais': ebit_sobre_ativos_totais,
            'crescimento_receita_liquida_5_anos':crescimento_receita_liquida_5_anos,
            'giro_ativos': giro_ativos,
            'margem_bruta': margem_bruta,
            'margem_ebit': margem_ebit,
            'margem_liquida': margem_liquida,
        }

        indicadores_de_endividamento = {
            'liquidez_corrente': liquidez_corrente,
            'divida_bruta_total': divida_bruta_total,
        }

        balanco_patrimonial = {
            'ativo': ativo,
            'ativo_circulante': ativo_circulante,
            'disponibilidades': disponibilidades,
            'divida_bruta': divida_bruta,
            'divida_líquida': divida_liquida,
            'patrimonio_Liquido': patrimonio_liquido,
        }

        demonstrativo_de_resultados = {
            '12_meses': {
                'receita_liquida_ultimos_12_meses': receita_liquida_ultimos_12_meses,
                'ebit_ultimos_12_meses': ebit_ultimos_12_meses,
                'lucro_liquido_ultimos_12_meses': lucro_liquido_ultimos_12_meses
            },
            '3_meses': {
                'receita_liquida_ultimos_3_meses':receita_liquida_ultimos_3_meses,
                'ebit_ultimos_3_meses': ebit_ultimos_3_meses,
                'lucro_liquido_ultimos_3_meses': lucro_liquido_ultimos_3_meses
            }
        }

        return {
            'cotacao': cotacao,
            'informacoes_basicas': informacoes_basicas,
            'oscilacoes': oscilacoes,
            'indicadores_de_valuation': indicadores_de_valuation,
            'indicadores_de_rentabilidade': indicadores_de_rentabilidade,
            'indicadores_de_endividamento': indicadores_de_endividamento,
            'balanco_patrimonial': balanco_patrimonial,
            'demonstrativo_de_resultados': demonstrativo_de_resultados
        }
