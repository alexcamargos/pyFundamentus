#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extract_contract.py
#  Version: 0.0.4
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

# pylint: disable=line-too-long

from datetime import datetime as dt
from ..extract_contract import ExtractContract

__extraction_date = dt.now().toordinal()

__raw_information = {
    'identification': {
        'symbol': ['VALE3'],
        'name': ['VALE']
    },
    'financial_summary': {
        'market_valuation': ['Valor de mercado ?',
                             'Valor de mercado da empresa, calculado multiplicando o preço da ação pelo número total de ações.',
                             'R$ 269.481.000.000'],
        'enterprise_valuation': ['Valor da firma ?',
                                 'Valor da firma (Enterprise Value) é calculado somando o valor de mercado da empresa a sua dívida líquida.',
                                 'R$ 317.236.000.000 '],
        'number_of_shares': ['Nº de ações ?',
                             'Número total de ações, somadas todas as espécies: ON, PN, etc.',
                             '4.539.010.000'],
        'last_financial_statement': ['Último balanço ?',
                                     'Data do último balanço divulgado pela empresa que consta no nosso banco de dados. Todos os indicadores são calculados considerando os últimos 12 meses finalizados na data deste balanço.',
                                     '30/06/2024'],
        'sector': ['Setor ?',
                   'Classificação setorial.',
                   'Mineração'],
        'subsector': ['Subsetor ?',
                      'Classificação por segmento de atuação.',
                      'Minerais Metálicos']
    },
    'price': {
        'price': [
            'Cotação ?', 'Cotação de fechamento da ação no último pregão.',
            'R$68,45'
        ],
        'date': [
            'Última cotação ?',
            'Data do último pregão em  que o ativo foi negociado.',
            '\n21/09/2022\n'
        ]
    },
    'detailed_information': {
        'stock_type': [
            'Tipo ?',
            'ON = Ordinária, PN = Preferencial, PNA = Pref. tipo A, etc.',
            'ON NM'
        ],
        'traded_volume_per_day': [
            'Volume negociado por dia ?',
            'Valor médio de negociação diária da ação, considerando os últimos 2 meses (R$).',
            'R$ 2.299.160.000'
        ],
        'equity_value_per_share': [
            'VPA ?',
            'Valor Patrimonial por Ação: Valor do Patrimônio Líquido dividido pelo número total de ações.',
            '38,91'
        ],
        'earnings_per_share': ['LPA ?', 'Lucro por Ação.', '21,69'],
        'variation_52_weeks': {
            'lowest_value':
            ['Menor cotação da ação nos últimos 12 meses.', 'R$ 57,25'],
            'highest_value':
            ['Maior cotação da ação nos últimos 12 meses.', 'R$ 96,51']
        }
    },
    'oscillations': {
        'variation_day': ['dia', '\n-1,44 %'],
        'variation_month': ['mês', '6,12 %'],
        'variation_30_days': ['30 dias', '2,23 %'],
        'variation_12_months': ['12 meses', '-2,21 %'],
        'variation_2022': ['2022', '-4,41 %'],
        'variation_2021': ['2021', '4,73 %'],
        'variation_2020': ['2020', '70,47 %'],
        'variation_2019': ['2019', '6,85 %'],
        'variation_2018': ['2018', '31,11 %'],
        'variation_2017': ['2017', '66,67 %']
    },
    'valuation_indicators': {
        'price_divided_by_profit_title': [
            'P/L ?',
            'Preço da ação dividido pelo lucro por ação. O P/L é o número de anos que se levaria para reaver o capital aplicado na compra de uma ação, através do recebimento do lucro gerado pela empresa, considerando que esses lucros permaneçam constantes.',
            '3,16'
        ],
        'price_divided_by_asset_value': [
            'P/VP ?',
            'Preço da ação dividido pelo Valor Patrimonial por ação. Informa quanto o mercado está disposto a pagar sobre o Patrimônio Líquido da empresa.',
            '1,76'
        ],
        'price_divided_by_ebit': [
            'P/EBIT ?',
            'Preço da ação dividido pelo EBIT por ação. EBIT é o Lucro antes dos Impostos e Despesas Financeiras. É uma boa aproximação do lucro operacional da empresa.',
            '2,50'
        ],
        'price_divided_by_net_revenue': [
            'PSR ?',
            'Price Sales Ratio: Preço da ação dividido pela Receita Líquida por ação.',
            '1,32'
        ],
        'price_divided_by_total_assets': [
            'Preço/Ativos ?',
            'Preço da ação dividido pelos Ativos totais por ação.', '0,74'
        ],
        'price_divided_by_net_current_assets': [
            'Preço/Ativ circ liq ?',
            'Preço da ação dividido pelos Ativos Circulantes Líquidos por ação. Ativo Circ. Líq. é obtido subtraindo os ativos circulantes pelas dívidas de curto e longo prazo, ou seja, após o pagamento de todas as dívidas, quanto sobraria dos ativos mais líquidos da empresa (caixa, estoque, etc).',
            '-1,99'
        ],
        'dividend_yield': [
            'Dividend Yield ?',
            'Dividendo pago por ação dividido pelo preço da ação. É o rendimento gerado para o dono da ação pelo pagamento de dividendos.',
            '24,3 %'
        ],
        'enterprise_value_by_ebitda': [
            'EV/EBITDA ?',
            'Valor da Firma (Enterprise Value dividido pelo EBITDA.', '2,43'
        ],
        'enterprise_value_by_ebit': [
            'EV/EBIT ?',
            'Valor da Firma (Enterprise Value dividido pelo EBIT.', '2,72'
        ],
        'price_by_working_capital': [
            'Preço/Capital de giro ?',
            'Preço da ação dividido pelo capital de giro por ação. Capital de giro é o Ativo Circulante menos Passivo Circulante.',
            '15,99'
        ]
    },
    'profitability_indicators': {
        'return_on_equity': [
            'ROE ?',
            'Retorno sobre o Patrimônio Líquido: Lucro líquido dividido pelo Patrimônio Líquido.',
            '55,7%'
        ],
        'return_on_invested_capital': [
            'ROIC ?',
            'Retorno sobre o Capital Investido: Calculado dividindo-se o EBIT por (Ativos - Fornecedores - Caixa). Informa o retorno que a empresa consegue sobre o capital total aplicado.',
            '34,0 %'
        ],
        'ebit_divided_by_total_assets':
        ['EBIT/Ativo ?', 'EBIT dividido por Ativos totais.', '29,6'],
        'net_revenue_growth_last_5_years': [
            'Crescimento receita ?',
            'Crescimento da Receita Líquida nos últimos 5 anos.', '24,8 %'
        ],
        'net_revenue_divided_by_total_assets': [
            'Giro ativos ?',
            'Receita Líquida dividido por Ativos Totais. Indica a eficiência com a qual a empresa usa seus ativos para gerar vendas.',
            '0,56 '
        ],
        'gross_profit_divided_by_net_revenue': [
            'Margem bruta ?',
            'Lucro Bruto dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o custo dos produtos/serviços vendidos.',
            '53,7 %'
        ],
        'ebit_divided_by_net_revenue': [
            'Margem EBIT ?',
            'EBIT dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o pagamento dos custos dos produtos/serviços vendidos, das despesas com vendas, gerais e administrativas.',
            '52,7 %'
        ],
        'net_income_divided_by_net_revenue': [
            'Margem líquida ?', 'Lucro Líquido dividido pela Receita Líquida.',
            '42,2 %'
        ]
    },
    'indebtedness_indicators': {
        'current_liquidity': [
            'Liquidez corrente ?',
            'Ativo Circulante dividido pelo Passivo Circulante: Reflete a capacidade de pagamento da empresa no curto prazo.',
            '1,32'
        ],
        'gross_debt_by_equity': [
            'Dívida bruta/Patrim ?',
            'Dívida Bruta total (Dívida+Debêntures) dividido pelo Patrimônio Líquido.',
            '0,36'
        ],
        'net_debt_by_equity': [
            'Dívida líquida/Patrim ?',
            'Dívida Bruta total (Dívida+Debêntures) menos caixa dividido pelo Patrimônio Líquido.',
            '0,15'
        ],
        'net_debt_by_ebitda': [
            'Dívida líquida/EBITDA ?',
            'Dívida Bruta total (Dívida+Debêntures) menos caixa dividido pelo EBITDA.',
            '0,19'
        ],
        'equity_by_total_assets':
        ['PL/Ativos ?', 'Patrimônio Líquido sobre Ativos', '0,42']
    },
    'balance_sheet': {
        'total_assets': [
            'Ativo ?',
            'Todos os bens, direitos e valores a receber de uma entidade.',
            'R$ 441.867.000.000'
        ],
        'current_assets': [
            'Ativo circulante ?',
            'Bens ou direitos que podem ser convertido em dinheiro em curto prazo.',
            'R$ 83.924.000.000'
        ],
        'cash': [
            'Disponibilidades ?',
            'Contas que representam bens numerários (Dinheiro).',
            'R$ 37.886.000.000'
        ],
        'gross_debt': [
            'Dívida bruta ?',
            'Dívida Bruta é obtida somando-se as dívidas de curto e longo prazo mais as debêntures de curto e longo prazo.',
            'R$ 66.042.000.000'
        ],
        'net_debt': [
            'Dívida líquida ?',
            'Dívida Bruta menos Disponibilidades. Se este valor é negativo, significa que a empresa possui caixa líquido positivo.',
            'R$ 28.156.000.000'
        ],
        'equity': [
            'Patrimônio líquido ?',
            'O patrimônio líquido representa os valores que os sócios ou acionistas têm na empresa em um determinado momento. No balanço patrimonial, a diferença entre o valor dos ativos e dos passivos e resultado de exercícios futuros representa o PL (Patrimônio Líquido), que é o valor contábil devido pela pessoa jurídica aos sócios ou acionistas.',
            'R$ 185.951.000.000'
        ]
    },
    'income_statement': {
        'twelve_months': {
            'revenue': [
                'Receita líquida ?',
                'Receita Líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos.',
                'R$ 248.069.000.000'
            ],
            'ebit': [
                'EBIT ?',
                'Earnings Before Interest and Taxes - Lucro antes dos impostos e juros: Uma aproximação do lucro operacional da empresa. Fórmula utilizada: Lucro bruto - desp de vendas - desp administrativas',
                'R$ 130.654.000.000'
            ],
            'net_income': [
                'Lucro líquido ?',
                'O que sobra das vendas após a dedução de todas as despesas.',
                'R$ 103.648.000.000'
            ]
        },
        'three_months': {
            'revenue': [
                'Receita líquida ?',
                'Receita Líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos.',
                'R$ 54.974.000.000'
            ],
            'ebit': [
                'EBIT ?',
                'Earnings Before Interest and Taxes - Lucro antes dos impostos e juros: Uma aproximação do lucro operacional da empresa. Fórmula utilizada: Lucro bruto - desp de vendas - desp administrativas',
                'R$ 24.972.000.000'
            ],
            'net_income': [
                'Lucro líquido ?',
                'O que sobra das vendas após a dedução de todas as despesas.',
                'R$ 30.033.000.000'
            ]
        }
    }
}

EXTRACT_CONTRACT_MOCK = ExtractContract(__raw_information, __extraction_date)
