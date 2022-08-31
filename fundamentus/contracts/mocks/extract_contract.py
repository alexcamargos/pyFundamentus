#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extract_contract.py
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

from datetime import datetime as dt
from ..extract_contract import ExtractContract

__extraction_date = dt.now().toordinal()

__raw_information = {
    'cotacao': {
        'cotacao': '4,52',
        'ultima_cotação': '29/08/2022',
        'minino_52_semanas': '2,13',
        'maximo_52_semanas': '19,48'
    },
    'informacoes_basicas': {
        'ativo': 'MGLU3',
        'empresa': 'MAGAZ LUIZA ON NM',
        'tipo': 'ON NM',
        'setor': 'Comércio',
        'subsetor': 'Eletrodomésticos',
        'valor_de_mercado': '30.505.200.000',
        'valor_da_firma': '35.429.700.000',
        'numero_de_acoes': '6.748.930.000',
        'data_ultimo_balanço': '30/06/2022',
        'volume_negociacoes_2_meses': '624.925.000'
    },
    'oscilacoes': {
        'dia': '\n-1,31%',
        'mes': '75,19%',
        '30_dias': '75,19%',
        '12_meses': '-76,25%',
        '2022': '-37,40%',
        '2021': '-71,04%',
        '2020': '110,08%',
        '2019': '112,19%',
        '2018': '126,39%',
        '2017': '536,59%'
    },
    'indicadores_de_valuation': {
        'preco_sobre_lucro': '-509,96',
        'preco_sobre_valor_patrimonial': '2,79',
        'preco_sobre_ebit': '\n108,61',
        'preco_sobre_ativos': '\n0,88',
        'preco_sobre_ativo_circulante_liquido': '\n-8,72',
        'preco_sobre_capital_giro': '\n3,91',
        'lucro_por_acao': '-0,01',
        'valor_patrimonial_por_acao': '1,62',
        'price_sales_ratio': '\n0,86',
        'dividend_yield': '0,0%',
        'enterprise_value_sobre_ebitda': '\n28,33',
        'enterprise_value_sobre_ebit': '\n126,14'
    },
    'indicadores_de_rentabilidade': {
        'return_invested_capital': '\n1,1%',
        'return_on_equity': '\n-0,5%',
        'ebit_sobre_ativos_totais': '0,8%',
        'crescimento_receita_liquida_5_anos': '\n30,0%',
        'giro_ativos': '\n1,02',
        'margem_bruta': '\n25,4%',
        'margem_ebit': '\n 0,8%',
        'margem_liquida': '\n-0,2%'
    },
    'indicadores_de_endividamento': {
        'liquidez_corrente': '\n1,64',
        'divida_bruta_total': '\n0,63'
    },
    'balanco_patrimonial': {
        'ativo': '34.501.000.000',
        'divida_bruta': '6.846.580.000',
        'disponibilidades': '1.922.030.000',
        'divida_líquida': '4.924.550.000',
        'ativo_circulante': '20.065.600.000',
        'patrimonio_Liquido': '10.937.800.000'
    },
    'demonstrativo_de_resultados': {
        '12_meses': {
            'receita_liquida_ultimos_12_meses': '35.336.600.000',
            'ebit_ultimos_12_meses': '280.867.000',
            'lucro_liquido_ultimos_12_meses': '-59.819.000'
        },
        '3_meses': {
            'receita_liquida_ultimos_3_meses': '8.562.390.000',
            'ebit_ultimos_3_meses': '274.562.000',
            'lucro_liquido_ultimos_3_meses': '-135.004.000'
        }
    }
}

extract_contract_mock = ExtractContract(__raw_information, __extraction_date)
