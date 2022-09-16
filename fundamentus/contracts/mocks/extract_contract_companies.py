#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extract_contract_companies.py
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
    'code': 'AALR3 ',
    'name': 'ALLIAR',
    'corporate_name': 'CENTRO DE IMAGEM DIAGNOSTICOS S.A.',
    'link': 'detalhes.php?papel=AALR3 '
}, {
    'code': 'ABCB3',
    'name': 'ABC Brasil',
    'corporate_name': 'BANCO ABC BRASIL S/A',
    'link': 'detalhes.php?papel=ABCB3'
}, {
    'code': 'ABCB4',
    'name': 'ABC Brasil',
    'corporate_name': 'BANCO ABC BRASIL S/A',
    'link': 'detalhes.php?papel=ABCB4'
}, {
    'code': 'ABEV3',
    'name': 'AMBEV S/A',
    'corporate_name': 'AMBEV S.A.',
    'link': 'detalhes.php?papel=ABEV3'
}, {
    'code': 'ABRE3',
    'name': 'SOMOS EDUCA',
    'corporate_name': 'SOMOS EDUCAÇÃO S.A.',
    'link': 'detalhes.php?papel=ABRE3'
}, {
    'code': 'ABYA3',
    'name': 'ABYARA',
    'corporate_name': 'ABYARA PLANEJAMENTO IMOBILIARIO S.A.',
    'link': 'detalhes.php?papel=ABYA3'
}, {
    'code': 'ACES3',
    'name': 'ARCELORMITTAL INOX BRASIL',
    'corporate_name': 'ARCELORMITTAL INOX BRASIL S.A.',
    'link': 'detalhes.php?papel=ACES3'
}, {
    'code': 'ACES4',
    'name': 'ARCELORMITTAL INOX BRASIL',
    'corporate_name': 'ARCELORMITTAL INOX BRASIL S.A.',
    'link': 'detalhes.php?papel=ACES4'
}, {
    'code': 'ADHM3',
    'name': 'ADVANCED-DH',
    'corporate_name': 'ADVANCED DIGITAL HEALTH MEDICINA PREVENTIVA S.A.',
    'link': 'detalhes.php?papel=ADHM3'
}, {
    'code': 'AEDU11',
    'name': 'ANHANGUERA EDUCACIONAL PARTICIPAÇÕES SA',
    'corporate_name': 'ANHANGUERA EDUCACIONAL PARTICIPAÇÕES S.A',
    'link': 'detalhes.php?papel=AEDU11'
}, {
    'code': 'AEDU3',
    'name': 'ANHANGUERA EDUCACIONAL PARTICIPAÇÕES SA',
    'corporate_name': 'ANHANGUERA EDUCACIONAL PARTICIPAÇÕES S.A',
    'link': 'detalhes.php?papel=AEDU3'
}, {
    'code': 'AELP3',
    'name': 'AES ELPA',
    'corporate_name': 'AES ELPA SA',
    'link': 'detalhes.php?papel=AELP3'
}, {
    'code': 'AERI3',
    'name': 'AERIS',
    'corporate_name': 'AERIS IND. E COM. DE EQUIP. GERACAO DE ENERGIA S/A',
    'link': 'detalhes.php?papel=AERI3'
}, {
    'code': 'AESB3',
    'name': 'AES BRASIL',
    'corporate_name': 'AES BRASIL ENERGIA S.A.',
    'link': 'detalhes.php?papel=AESB3'
}, {
    'code': 'AESL3',
    'name': 'AES SUL DISTRIB. GAÚCHA DE ENERGIA S.A.',
    'corporate_name': 'AES SUL DISTRIB. GAÚCHA DE ENERGIA S.A.',
    'link': 'detalhes.php?papel=AESL3'
}]

EXTRACT_CONTRACT_COMPANIES_MOCK = ExtractContract(__RAW_INFORMATION,
                                                  __EXTRACTION_DATE)
