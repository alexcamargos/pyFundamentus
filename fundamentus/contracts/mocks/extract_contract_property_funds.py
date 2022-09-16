#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extract_contract_property_funds.py
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

__EXTRACTION_DATE = dt.now().toordinal()

__RAW_INFORMATION = [{
    'code': 'ABCP11',
    'name': 'FII GRAND PLAZA SHOPPING',
    'link': 'detalhes.php?papel=ABCP11'
}, {
    'code': 'AEFI11',
    'name': 'FII RIO BRAVO RENDA EDUCACIONAL- FII',
    'link': 'detalhes.php?papel=AEFI11'
}, {
    'code': 'AFCR11',
    'name': 'CARTESIA RECEBÍVEIS IMOBILIÁRIOS - FII',
    'link': 'detalhes.php?papel=AFCR11'
}, {
    'code': 'AFHI11',
    'name': 'AF INVEST CRI FII - RECEBÍVEIS IMOBILIÁRIOS',
    'link': 'detalhes.php?papel=AFHI11'
}, {
    'code': 'AFOF11',
    'name': 'ALIANZA MULTIESTRATÉGIA FII',
    'link': 'detalhes.php?papel=AFOF11'
}, {
    'code': 'AGCX11',
    'name': 'FII RIO BRAVO RENDA VAREJO - FII',
    'link': 'detalhes.php?papel=AGCX11'
}, {
    'code': 'AGRX11',
    'name':
    'FUNDO DE INVESTIMENTO NAS CADEIAS PRODUTIVAS AGROINDUSTRIAIS'
    'EXES ARAGUAIA - FIAGRO - IMOBILIÁRIO',
    'link': 'detalhes.php?papel=AGRX11'
}, {
    'code': 'AIEC11',
    'name': 'AUTONOMY EDIFÍCIOS CORPORATIVOS FII',
    'link': 'detalhes.php?papel=AIEC11'
}, {
    'code': 'ALMI11',
    'name': 'FII TORRE ALMIRANTE',
    'link': 'detalhes.php?papel=ALMI11'
}, {
    'code': 'ALZR11',
    'name': 'ALIANZA TRUST RENDA IMOBILIARIA - FII',
    'link': 'detalhes.php?papel=ALZR11'
}, {
    'code': 'ALZR12',
    'name': 'ALIANZA TRUST RENDA IMOBILIARIA - FII',
    'link': 'detalhes.php?papel=ALZR12'
}, {
    'code': 'ANCR11',
    'name': 'FII ANCAR IC',
    'link': 'detalhes.php?papel=ANCR11'
}, {
    'code': 'APTO11',
    'name': 'NAVI RESIDENCIAL FII',
    'link': 'detalhes.php?papel=APTO11'
}, {
    'code': 'ARCT11',
    'name': 'RIZA ARCTIUM REAL ESTATE FII',
    'link': 'detalhes.php?papel=ARCT11'
}, {
    'code': 'ARRI11',
    'name': 'FUNDO DE INVESTIMENTO ÁTRIO REIT RECEBÍVEIS IMOBILIÁRIOS',
    'link': 'detalhes.php?papel=ARRI11'
}]

EXTRACT_CONTRACT_PROPERTY_FUNDS_MOCK = ExtractContract(__RAW_INFORMATION,
                                                       __EXTRACTION_DATE)
