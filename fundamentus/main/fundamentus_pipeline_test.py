#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: fundamentus_pipeline.py
#  Version: 0.0.6
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
from fundamentus.drivers.mocks.companies_list import COMPANIES_LIST_MOCK
from fundamentus.drivers.mocks.html_collector import HTML_COLLECTOR_MOCK
from fundamentus.utilities.config import URL

from .fundamentus_pipeline import FundamentusPipeline


def test_get_all_information(requests_mock) -> None:
    """Test the get_all_information method."""

    # Mock the HTTP GET request to return the predefined HTML
    # content with a 200 status code.
    requests_mock.get(URL,
                      status_code=HTML_COLLECTOR_MOCK['status_code'],
                      text=HTML_COLLECTOR_MOCK['content'])

    # Initialize the pipeline and execute the method under test.
    main_pipeline = FundamentusPipeline('MGLU3')
    response = main_pipeline.get_all_information()

    assert isinstance(response, TransformContract)
    assert isinstance(response.transformed_information, dict)
    assert isinstance(response.transformed_information['price_information'],
                      dict)
    assert isinstance(response.transformed_information['detailed_information'],
                      dict)
    assert isinstance(response.transformed_information['oscillations'], dict)
    assert isinstance(response.transformed_information['valuation_indicators'],
                      dict)
    assert isinstance(
        response.transformed_information['profitability_indicators'], dict)
    assert isinstance(
        response.transformed_information['indebtedness_indicators'], dict)
    assert isinstance(response.transformed_information['balance_sheet'], dict)
    assert isinstance(response.transformed_information['income_statement'],
                      dict)


def test_list_all_companies(requests_mock) -> None:
    """Test the list_all_companies method."""

    # Mock the HTTP GET request to return the predefined HTML
    # content with a 200 status code.
    requests_mock.get(URL,
                      status_code=COMPANIES_LIST_MOCK['status_code'],
                      text=COMPANIES_LIST_MOCK['content'])

    # Initialize the pipeline and execute the method under test.
    main_pipeline = FundamentusPipeline()
    response = main_pipeline.list_all_companies()

    assert isinstance(response, TransformContract)
    assert isinstance(response.transformed_information, list)
    assert isinstance(response.transformed_information[0], dict)


def test_list_all_property_funds(requests_mock) -> None:
    """Test the list_all_companies method."""

    url = 'https://www.fundamentus.com.br/detalhes.php'

    requests_mock.get(url=url,
                      status_code=COMPANIES_LIST_MOCK['status_code'],
                      text=COMPANIES_LIST_MOCK['content'])

    main_pipeline = FundamentusPipeline()
    response = main_pipeline.list_all_property_funds()

    assert isinstance(response, TransformContract)
    assert isinstance(response.transformed_information, list)
    assert isinstance(response.transformed_information[0], dict)
