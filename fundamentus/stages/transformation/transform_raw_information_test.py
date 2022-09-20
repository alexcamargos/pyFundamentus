#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: transform_raw_information_test.py
#  Version: 0.0.3
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

"""Test of transform raw information from the HTTP requester."""

from fundamentus.contracts.mocks.extract_contract import EXTRACT_CONTRACT_MOCK
from fundamentus.contracts.mocks.extract_contract_companies import \
    EXTRACT_CONTRACT_COMPANIES_MOCK
from fundamentus.contracts.mocks.extract_contract_property_funds import \
    EXTRACT_CONTRACT_PROPERTY_FUNDS_MOCK
from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.exceptions.transform_exception import TransformException

from .transform_raw_information import TransformRawInformation


def test_transform_raw_information() -> None:
    """Test of transform raw information from the HTTP requester."""

    transform = TransformRawInformation()
    transformed = transform.transform_information(EXTRACT_CONTRACT_MOCK)

    assert isinstance(transformed, TransformContract)
    assert isinstance(transformed.transformed_information, dict)
    assert len(transformed.transformed_information) == 8


def test_transform_raw_information_keys_results() -> None:
    """Test of transform raw information from the HTTP requester keys results."""

    transform = TransformRawInformation()
    transformed = transform.transform_information(EXTRACT_CONTRACT_MOCK)

    assert isinstance(transformed, TransformContract)
    assert isinstance(transformed.transformed_information, dict)
    assert len(transformed.transformed_information) == 8

    assert [
        'price_information', 'detailed_information', 'oscillations',
        'valuation_indicators', 'profitability_indicators',
        'indebtedness_indicators', 'balance_sheet', 'income_statement'
    ] == list(transformed.transformed_information.keys())


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


def test_transform_raw_information_of_companies() -> None:
    """Test of transform raw information from the HTTP requester."""

    transform = TransformRawInformation()
    transformed = transform.transform_companies(
        EXTRACT_CONTRACT_COMPANIES_MOCK)

    assert isinstance(transformed, TransformContract)
    assert isinstance(transformed.transformed_information, list)
    assert isinstance(transformed.transformed_information[0], dict)

    assert ['code', 'name', 'corporate_name',
            'link'] == list(transformed.transformed_information[0].keys())


def test_transform_raw_information_of_companies_exception() -> None:
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


def test_transform_raw_information_of_property_funds() -> None:
    """Test of transform raw information from the HTTP requester."""

    transform = TransformRawInformation()
    transformed = transform.transform_property_funds(
        EXTRACT_CONTRACT_PROPERTY_FUNDS_MOCK)

    assert isinstance(transformed, TransformContract)
    assert isinstance(transformed.transformed_information, list)
    assert isinstance(transformed.transformed_information[0], dict)

    assert ['code', 'name',
            'link'] == list(transformed.transformed_information[0].keys())


def test_transform_raw_information_of_property_funds_exception() -> None:
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
