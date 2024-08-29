#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: html_collector_test.py
#  Version: 0.0.9
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

"""Html Collector Test"""

from .html_collector import HtmlCollector
from .mocks.companies_list import COMPANIES_LIST_MOCK
from .mocks.html_collector import HTML_COLLECTOR_MOCK


def test_collect_all_information() -> None:
    """Test collect all information."""

    collector = HtmlCollector()
    collect_information = collector.collect_all_information(
        HTML_COLLECTOR_MOCK['content'])

    assert isinstance(collect_information, dict)
    assert len(collect_information) == 10


def test_collect_all_information_keys_results() -> None:
    """Test collect all information keys results."""

    collector = HtmlCollector()
    collect_information = collector.collect_all_information(
        HTML_COLLECTOR_MOCK['content'])

    assert [
        'identification', 'financial_summary', 'price', 'detailed_information',
        'oscillations', 'valuation_indicators', 'profitability_indicators',
        'indebtedness_indicators', 'balance_sheet', 'income_statement'
    ] == list(collect_information.keys())


def test_collect_list_of_companies() -> None:
    """Test collect list of companies."""

    collector = HtmlCollector()
    collect_list_of_companies = collector.collect_list_of_companies(
        COMPANIES_LIST_MOCK['content'])

    assert isinstance(collect_list_of_companies, list)
    assert isinstance(collect_list_of_companies[0], dict)


def test_collect_list_of_property_funds() -> None:
    """Test collect list of property funds."""

    collector = HtmlCollector()
    collect_list_of_property_funds = collector.collect_list_of_property_funds(
        COMPANIES_LIST_MOCK['content'])

    assert isinstance(collect_list_of_property_funds, list)
    assert isinstance(collect_list_of_property_funds[0], dict)
