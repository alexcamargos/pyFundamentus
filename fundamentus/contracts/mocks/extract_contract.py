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

# pylint: disable=line-too-long

from datetime import datetime as dt
from ..extract_contract import ExtractContract

__extraction_date = dt.now().toordinal()

__raw_information = {
    'price': {
        'price': [
            'Cotação ?', 'Cotação de fechamento da ação no último pregão.',
            'R$4,56'
        ],
        'date': [
            'Última cotação ?',
            'Data do último pregão em  que o ativo foi negociado.',
            '\n19/09/2022\n'
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
            'R$ 691.968.000'
        ],
        'equity_value_per_share': [
            'VPA ?',
            'Valor Patrimonial por Ação: Valor do Patrimônio Líquido dividido pelo número total de ações.',
            '1,62'
        ],
        'earnings_per_share': ['LPA ?', 'Lucro por Ação.', '-0,01'],
        'variation_52_weeks': {
            'lowest_value':
            ['Menor cotação da ação nos últimos 12 meses.', 'R$ 2,13'],
            'highest_value':
            ['Maior cotação da ação nos últimos 12 meses.', 'R$ 16,39']
        }
    },
    'oscillations': {
        'variation_day': '\n2,24 %',
        'variation_month': '6,79 %',
        'variation_30_days': '20,63 %',
        'variation_12_months': '-72,48 %',
        'variation_2022': '-36,84 %',
        'variation_2021': '-71,04 %',
        'variation_2020': '110,08 %',
        'variation_2019': '112,19 %',
        'variation_2018': '126,39 %',
        'variation_2017': '536,59 %'
    },
    'valuation_indicators': {
        'price_divided_by_profit_title': [
            'P/L ?',
            'Preço da ação dividido pelo lucro por ação. O P/L é o número de anos que se levaria para reaver o capital aplicado na compra de uma ação, através do recebimento do lucro gerado pela empresa, considerando que esses lucros permaneçam constantes.',
            '-514,47'
        ],
        'price_divided_by_asset_value': [
            'P/VP ?',
            'Preço da ação dividido pelo Valor Patrimonial por ação. Informa quanto o mercado está disposto a pagar sobre o Patrimônio Líquido da empresa.',
            '2,81'
        ],
        'price_divided_by_ebit': [
            'P/EBIT ?',
            'Preço da ação dividido pelo EBIT por ação. EBIT é o Lucro antes dos Impostos e Despesas Financeiras. É uma boa aproximação do lucro operacional da empresa.',
            '109,57'
        ],
        'price_divided_by_net_revenue': [
            'PSR ?',
            'Price Sales Ratio: Preço da ação dividido pela Receita Líquida por ação.',
            '0,87'
        ],
        'price_divided_by_total_assets': [
            'Preço/Ativos ?',
            'Preço da ação dividido pelos Ativos totais por ação.', '0,89'
        ],
        'price_divided_by_net_current_assets': [
            'Preço/Ativ circ liq ?',
            'Preço da ação dividido pelos Ativos Circulantes Líquidos por ação. Ativo Circ. Líq. é obtido subtraindo os ativos circulantes pelas dívidas de curto e longo prazo, ou seja, após o pagamento de todas as dívidas, quanto sobraria dos ativos mais líquidos da empresa (caixa, estoque, etc).',
            '-8,80'
        ],
        'dividend_yield': [
            'Dividend Yield ?',
            'Dividendo pago por ação dividido pelo preço da ação. É o rendimento gerado para o dono da ação pelo pagamento de dividendos.',
            '0,0 %'
        ],
        'enterprise_value_by_ebitda': [
            'EV/EBITDA ?',
            'Valor da Firma (Enterprise Value dividido pelo EBITDA.', '28,54'
        ],
        'enterprise_value_by_ebit': [
            'EV/EBIT ?',
            'Valor da Firma (Enterprise Value dividido pelo EBIT.', '127,11'
        ],
        'price_by_working_capital': [
            'Preço/Capital de giro ?',
            'Preço da ação dividido pelo capital de giro por ação. Capital de giro é o Ativo Circulante menos Passivo Circulante.',
            '3,94'
        ]
    },
    'profitability_indicators': {
        'return_on_equity': [
            'ROE ?',
            'Retorno sobre o Patrimônio Líquido: Lucro líquido dividido pelo Patrimônio Líquido.',
            '-0,5%'
        ],
        'return_on_invested_capital': [
            'ROIC ?',
            'Retorno sobre o Capital Investido: Calculado dividindo-se o EBIT por (Ativos - Fornecedores - Caixa). Informa o retorno que a empresa consegue sobre o capital total aplicado.',
            '1,1 %'
        ],
        'ebit_divided_by_total_assets':
        ['EBIT/Ativo ?', 'EBIT dividido por Ativos totais.', '0,8'],
        'net_revenue_growth_last_5_years': [
            'Crescimento receita ?',
            'Crescimento da Receita Líquida nos últimos 5 anos.', '30,0 %'
        ],
        'net_revenue_divided_by_total_assets': [
            'Giro ativos ?',
            'Receita Líquida dividido por Ativos Totais. Indica a eficiência com a qual a empresa usa seus ativos para gerar vendas.',
            '1,02 '
        ],
        'gross_profit_divided_by_net_revenue': [
            'Margem bruta ?',
            'Lucro Bruto dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o custo dos produtos/serviços vendidos.',
            '25,4 %'
        ],
        'ebit_divided_by_net_revenue': [
            'Margem EBIT ?',
            'EBIT dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o pagamento dos custos dos produtos/serviços vendidos, das despesas com vendas, gerais e administrativas.',
            '0,8 %'
        ],
        'net_income_divided_by_net_revenue': [
            'Margem líquida ?', 'Lucro Líquido dividido pela Receita Líquida.',
            '-0,2 %'
        ]
    },
    'indebtedness_indicators': {
        'current_liquidity': [
            'Liquidez corrente ?',
            'Ativo Circulante dividido pelo Passivo Circulante: Reflete a capacidade de pagamento da empresa no curto prazo.',
            '1,64'
        ],
        'gross_debt_by_equity': [
            'Dívida bruta/Patrim ?',
            'Dívida Bruta total (Dívida+Debêntures) dividido pelo Patrimônio Líquido.',
            '0,63'
        ],
        'net_debt_by_equity': [
            'Dívida líquida/Patrim ?',
            'Dívida Bruta total (Dívida+Debêntures) menos caixa dividido pelo Patrimônio Líquido.',
            '0,45'
        ],
        'net_debt_by_ebitda': [
            'Dívida líquida/EBITDA ?',
            'Dívida Bruta total (Dívida+Debêntures) menos caixa dividido pelo EBITDA.',
            '3,94'
        ],
        'equity_by_total_assets':
        ['PL/Ativos ?', 'Patrimônio Líquido sobre Ativos', '0,32']
    },
    'balance_sheet': {
        'total_assets': [
            'Ativo ?',
            'Todos os bens, direitos e valores a receber de uma entidade.',
            'R$ 34.501.000.000'
        ],
        'current_assets': [
            'Ativo circulante ?',
            'Bens ou direitos que podem ser convertido em dinheiro em curto prazo.',
            'R$ 20.065.600.000'
        ],
        'cash': [
            'Disponibilidades ?',
            'Contas que representam bens numerários (Dinheiro).',
            'R$ 1.922.030.000'
        ],
        'gross_debt': [
            'Dívida bruta ?',
            'Dívida Bruta é obtida somando-se as dívidas de curto e longo prazo mais as debêntures de curto e longo prazo.',
            'R$ 6.846.580.000'
        ],
        'net_debt': [
            'Dívida líquida ?',
            'Dívida Bruta menos Disponibilidades. Se este valor é negativo, significa que a empresa possui caixa líquido positivo.',
            'R$ 4.924.550.000'
        ],
        'equity': [
            'Patrimônio líquido ?',
            'O patrimônio líquido representa os valores que os sócios ou acionistas têm na empresa em um determinado momento. No balanço patrimonial, a diferença entre o valor dos ativos e dos passivos e resultado de exercícios futuros representa o PL (Patrimônio Líquido), que é o valor contábil devido pela pessoa jurídica aos sócios ou acionistas.',
            'R$ 10.937.800.000'
        ]
    },
    'income_statement': {
        'twelve_months': {
            'revenue': [
                'Receita líquida ?',
                'Receita Líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos.',
                'R$ 35.336.600.000'
            ],
            'ebit': [
                'EBIT ?',
                'Earnings Before Interest and Taxes - Lucro antes dos impostos e juros: Uma aproximação do lucro operacional da empresa. Fórmula utilizada: Lucro bruto - desp de vendas - desp administrativas',
                'R$ 280.867.000'
            ],
            'net_income': [
                'Lucro líquido ?',
                'O que sobra das vendas após a dedução de todas as despesas.',
                'R$ -59.819.000'
            ]
        },
        'three_months': {
            'revenue': [
                'Receita líquida ?',
                'Receita Líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos.',
                'R$ 8.562.390.000'
            ],
            'ebit': [
                'EBIT ?',
                'Earnings Before Interest and Taxes - Lucro antes dos impostos e juros: Uma aproximação do lucro operacional da empresa. Fórmula utilizada: Lucro bruto - desp de vendas - desp administrativas',
                'R$ 274.562.000'
            ],
            'net_income': [
                'Lucro líquido ?',
                'O que sobra das vendas após a dedução de todas as despesas.',
                'R$ -135.004.000'
            ]
        }
    }
}

EXTRACT_CONTRACT_MOCK = ExtractContract(__raw_information, __extraction_date)
