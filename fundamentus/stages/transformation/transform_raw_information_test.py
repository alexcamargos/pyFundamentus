#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: transform_raw_information_test.py
#  Version: 0.0.11
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

from fundamentus.contracts.information_contract import InformationItem

from .transform_raw_information import TransformRawInformation


# pylint: disable=attribute-defined-outside-init
class TestTransformRawInformation:

    def setup_class(self) -> None:
        """Setup class."""

        self.transform = TransformRawInformation()
        self.transformed = self.transform.transform_all_information(
            EXTRACT_CONTRACT_MOCK)

    def test_transform_raw_information(self) -> None:
        """Test of transform raw information from the HTTP requester."""

        assert isinstance(self.transformed, TransformContract)
        assert isinstance(self.transformed.transformed_information, dict)
        assert len(self.transformed.transformed_information) == 10

    def test_transform_raw_information_exception(self) -> None:
        """Test of transform raw information from the HTTP requester.

        This test should raise an exception because the raw
        information is not a valid.

        :raises: TransformException
        """

        try:
            transformed = self.transform.transform_all_information([])  # pylint: disable=unused-variable
        except TransformException as exception:
            assert isinstance(exception, TransformException)

    def test_transform_raw_information_keys_results(self) -> None:
        """Test of transform raw information from the HTTP requester keys results."""

        assert isinstance(self.transformed, TransformContract)
        assert isinstance(self.transformed.transformed_information, dict)
        assert len(self.transformed.transformed_information) == 10

        assert [
            'stock_identification', 'financial_summary', 'price_information',
            'detailed_information', 'oscillations', 'valuation_indicators',
            'profitability_indicators', 'indebtedness_indicators',
            'balance_sheet', 'income_statement'
        ] == list(self.transformed.transformed_information.keys())

    def test_transformation_of_stock_identification(self) -> None:
        """Test of transform stock identification information from the HTTP requester."""

        information = self.transformed.transformed_information['stock_identification']
        assert isinstance(information, dict)
        assert isinstance(information['name'], InformationItem)
        assert isinstance(information['ticker'], InformationItem)

    def test_transformation_of_financial_summary(self) -> None:
        """Test of transform financial summary from the HTTP requester."""

        information = self.transformed.transformed_information['financial_summary']

        assert isinstance(information, dict)
        assert isinstance(information['market_valuation'], InformationItem)
        assert isinstance(information['enterprise_valuation'], InformationItem)
        assert isinstance(information['number_of_shares'], InformationItem)
        assert isinstance(
            information['last_financial_statement'], InformationItem)
        assert isinstance(information['sector'], InformationItem)
        assert isinstance(information['subsector'], InformationItem)

    def test_transform_price_information(self) -> None:
        """Test of transform price information from the HTTP requester."""

        information = self.transformed.transformed_information[
            'price_information']

        assert isinstance(information, dict)
        assert isinstance(information['price'], InformationItem)
        assert isinstance(information['date'], InformationItem)

    def test_transform_detailed_information(self) -> None:
        """Test of transform detailed information from the HTTP requester."""

        information = self.transformed.transformed_information[
            'detailed_information']

        assert isinstance(information, dict)
        assert isinstance(information['stock_type'], InformationItem)
        assert isinstance(information['traded_volume_per_day'],
                          InformationItem)
        assert isinstance(information['equity_value_per_share'],
                          InformationItem)
        assert isinstance(information['earnings_per_share'], InformationItem)
        assert isinstance(information['variation_52_weeks'], dict)
        assert isinstance(information['variation_52_weeks']['lowest_value'],
                          InformationItem)
        assert isinstance(information['variation_52_weeks']['highest_value'],
                          InformationItem)

    def test_transform_oscillations(self) -> None:
        """Test of transform oscillations from the HTTP requester."""

        information = self.transformed.transformed_information['oscillations']

        assert isinstance(information, dict)
        assert isinstance(information['variation_day'], InformationItem)
        assert isinstance(information['variation_month'], InformationItem)
        assert isinstance(information['variation_30_days'], InformationItem)
        assert isinstance(information['variation_12_months'], InformationItem)
        assert isinstance(information['variation_2022'], InformationItem)
        assert isinstance(information['variation_2021'], InformationItem)
        assert isinstance(information['variation_2020'], InformationItem)
        assert isinstance(information['variation_2019'], InformationItem)
        assert isinstance(information['variation_2018'], InformationItem)
        assert isinstance(information['variation_2017'], InformationItem)

    def test_transform_valuation_indicators(self) -> None:
        """Test of transform valuation indicators from the HTTP requester."""

        information = self.transformed.transformed_information[
            'valuation_indicators']

        assert isinstance(information, dict)
        assert isinstance(information['price_divided_by_profit_title'],
                          InformationItem)
        assert isinstance(information['price_divided_by_asset_value'],
                          InformationItem)
        assert isinstance(information['price_divided_by_ebit'],
                          InformationItem)
        assert isinstance(information['price_divided_by_net_revenue'],
                          InformationItem)
        assert isinstance(information['price_divided_by_total_assets'],
                          InformationItem)
        assert isinstance(information['price_divided_by_net_current_assets'],
                          InformationItem)
        assert isinstance(information['dividend_yield'], InformationItem)
        assert isinstance(information['enterprise_value_by_ebitda'],
                          InformationItem)
        assert isinstance(information['enterprise_value_by_ebit'],
                          InformationItem)
        assert isinstance(information['price_by_working_capital'],
                          InformationItem)

    def test_transformation_of_profitability_indicators(self) -> None:
        """Test of transform profitability indicators from the HTTP requester."""

        information = self.transformed.transformed_information[
            'profitability_indicators']

        assert isinstance(information, dict)
        assert isinstance(information['return_on_equity'], InformationItem)
        assert isinstance(information['return_on_invested_capital'],
                          InformationItem)
        assert isinstance(information['ebit_divided_by_total_assets'],
                          InformationItem)
        assert isinstance(information['net_revenue_growth_last_5_years'],
                          InformationItem)
        assert isinstance(information['net_revenue_divided_by_total_assets'],
                          InformationItem)
        assert isinstance(information['gross_profit_divided_by_net_revenue'],
                          InformationItem)
        assert isinstance(information['ebit_divided_by_net_revenue'],
                          InformationItem)
        assert isinstance(information['net_income_divided_by_net_revenue'],
                          InformationItem)

    def test_transformation_of_indebtedness_indicators(self) -> None:
        """Test of transform indebtedness indicators from the HTTP requester."""

        information = self.transformed.transformed_information[
            'indebtedness_indicators']

        assert isinstance(information, dict)
        assert isinstance(information['current_liquidity'], InformationItem)
        assert isinstance(information['gross_debt_by_equity'], InformationItem)
        assert isinstance(information['net_debt_by_equity'], InformationItem)
        assert isinstance(information['net_debt_by_ebitda'], InformationItem)
        assert isinstance(information['equity_by_total_assets'],
                          InformationItem)

    def test_transformation_of_balance_sheet(self) -> None:
        """Test of transform balance sheet from the HTTP requester."""

        information = self.transformed.transformed_information['balance_sheet']

        assert isinstance(information, dict)
        assert isinstance(information['total_assets'], InformationItem)
        assert isinstance(information['current_assets'], InformationItem)
        assert isinstance(information['cash'], InformationItem)
        assert isinstance(information['gross_debt'], InformationItem)
        assert isinstance(information['net_debt'], InformationItem)
        assert isinstance(information['equity'], InformationItem)

    def test_transformation_of_income_statement(self) -> None:
        """Test of transform income statement from the HTTP requester."""

        information_three_months = self.transformed.transformed_information[
            'income_statement']['three_months']
        information_twelve_months = self.transformed.transformed_information[
            'income_statement']['twelve_months']

        assert isinstance(information_three_months, dict)
        assert isinstance(information_three_months['revenue'], InformationItem)
        assert isinstance(information_three_months['ebit'], InformationItem)
        assert isinstance(information_three_months['net_income'],
                          InformationItem)

        assert isinstance(information_twelve_months, dict)
        assert isinstance(information_twelve_months['revenue'],
                          InformationItem)
        assert isinstance(information_twelve_months['ebit'], InformationItem)
        assert isinstance(information_twelve_months['net_income'],
                          InformationItem)


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
        transformed = transform.transform_companies([])  # pylint: disable=unused-variable
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
        transformed = transform.transform_property_funds([])  # pylint: disable=unused-variable
    except TransformException as exception:
        assert isinstance(exception, TransformException)
