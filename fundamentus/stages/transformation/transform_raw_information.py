#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: transform_raw_information.py
#  Version: 0.1.3
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

"""
This module defines the TransformRawInformation class, responsible for transforming raw data
extracted from the Fundamentus website into structured and usable financial information.
It processes various types of financial data, including price information, detailed stock
information, oscillations, valuation indicators, profitability indicators, indebtedness
indicators, balance sheets, and income statements, making it ready for analysis or storage.

The transformation is crucial for preparing the data for further financial analysis or
for feeding into financial models.
"""

from decimal import Decimal
from typing import Dict, List

from fundamentus.contracts.extract_contract import ExtractContract
from fundamentus.contracts.information_contract import InformationItem
from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.exceptions.transform_exception import TransformException


# pylint: disable=too-few-public-methods
# pylint: disable=too-many-statements
# pylint: disable=duplicate-code
class TransformRawInformation:
    """
    A class to transform raw financial data into structured financial information.

    This class provides methods to clean and transform raw data into a more
    structured form, using predefined contracts for various financial metrics.
    It handles data such as stock price information, detailed stock metrics,
    market oscillations, valuation and profitability indicators, indebtedness
    metrics, balance sheet details, and income statements.

    Methods are provided to process individual components of the financial data,
    as well as to transform comprehensive datasets for complete analysis.
    """

    @staticmethod
    def __remove_new_lines(string: str) -> str:
        """
        Remove all newline characters from a given string.

        Args:
            string (str): The input string from which newline
                          characters will be removed.

        Returns:
            str: A new string with all newline characters removed.
        """

        return string.replace('\n', '')

    @staticmethod
    def __remove_all_spaces(string: str) -> str:
        """
        Remove all space characters from the input string.

        Args:
            string (str): The input string from which space
                          characters will be removed.

        Returns:
            str: A new string with all space characters removed.
        """

        return string.replace(' ', '')

    def __string_processing(self, string: str) -> str:
        """
        Processes a string by removing newlines, question marks,
        and trimming spaces.

        This method is a composite string cleaner that prepares
        strings for further processing.

        Args:
            string (str): The string to process.

        Returns:
            str: The cleaned and processed string.
        """

        # Remove all \n from the string.
        if '\n' in string:
            string = self.__remove_new_lines(string)

        # Remove question mark from the string.
        if '?' in string:
            string = string.replace('?', '')

        return string.strip()

    @staticmethod
    def __remove_dot(string: str) -> str:
        """
        Removes all period (dot) characters from a given string.

        This static method is used for cleaning strings by removing all
        occurrences of the period character. It's particularly useful
        in preprocessing numerical strings where dots may be used as
        thousand separators or are otherwise present but not desired
        in the final numerical representation.

        Args:
            string (str): The input string from which dots will be removed.

        Returns:
            str: A new string with all period characters removed.
        """

        return string.replace('.', '')

    @staticmethod
    def __change_comma_to_dot(string: str) -> str:
        """
        Replaces all comma characters with period (dot)
        characters in a given string.

        This method is essential for processing numerical strings
        where commas are used as decimal separators, converting
        them to a format that is compatible with the decimal
        point notation used in Python. It ensures that numerical
        strings can be correctly converted to float or Decimal types.

        Args:
            string (str): The input string in which commas will be
            replaced with dots.

        Returns:
            str: The modified string with commas replaced by dots,
            ready for numerical conversion.
        """

        return string.replace(',', '.')

    @staticmethod
    def __to_decimal(value: str) -> Decimal:
        """
        Convert a string to a Decimal, handling percentage values.

        Converts string representations of numbers, including those
        ending in '%', to Decimal. Percentage values are converted to
        their decimal equivalent (e.g., "50%" becomes 0.5).

        Args:
            value (str): The string representing a number or
                         percentage to convert.

        Returns:
            Decimal: The Decimal representation of the input string.
        """

        strip_value = value.strip()

        if '-' == strip_value:
            return Decimal(0)

        if strip_value.endswith('%'):
            strip_value = strip_value[:-1].strip()

            if '-' == strip_value.strip():
                return Decimal(0)

            return Decimal(strip_value) / 100

        return Decimal(strip_value) if strip_value is not None else None

    @staticmethod
    def __remove_currency_symbol(number: str) -> str:
        """
        Removes currency symbols from a given string.

        This static method is designed to strip common currency symbols
        (e.g., the dollar sign '$', the euro sign '€', or the Brazilian real 'R$')
        from the input string, preparing it for numerical conversion or
        further processing. While primarily focused on the Brazilian real symbol,
        it can be extended to remove other currency symbols as needed.

        Args:
            number (str): The input string from which currency symbols are to be removed.

        Returns:
            str: The input string with currency symbols removed, ready for further processing.
        """

        return number.replace('R$', '')

    def __number_processing(self, number: str) -> Decimal:
        """
        Processes a raw string representing a number and converts it into a Decimal.

        This method applies a series of cleaning steps to the input string, including removing currency
        symbols, replacing commas with dots for decimal representation, and removing unnecessary spaces
        or newline characters. The cleaned string is then converted into a Decimal for accurate financial
        calculations.

        Args:
            number (str): The raw string representation of a number, potentially including currency symbols,
            commas as decimal separators, and whitespace.

        Returns:
            Decimal: The cleaned and converted Decimal object representing the input number.
        """

        return self.__to_decimal(
            self.__remove_currency_symbol(
                self.__change_comma_to_dot(
                    self.__remove_dot(self.__remove_new_lines(number)))))

    def __transformation_of_stock_identification(self,
                                                 stock_identification: Dict) -> Dict:
        """
        Transform raw stock identification information into structured data.

        This method processes raw stock identification information, including the stock's
        name and ticker symbol it into a dictionary with InformationItem instances. It
        handles cleaning and formatting of the raw data to ensure it is ready for further
        financial analysis or storage.

        Args:
            stock_identification (Dict): A dictionary containing the raw stock identification
            information with keys 'name' and 'ticker', each associated with a list of raw data values.

        Returns:
            Dict: A dictionary with keys 'name' and 'ticker', where each key is associated with an
            InformationItem instance containing cleaned and structured data.
        """

        name = InformationItem(
            title='Código',
            tooltip='Código da ação.',
            value=self.__string_processing(stock_identification['symbol'][0]))

        ticker = InformationItem(
            title='Empresa',
            tooltip='Nome comercial da empresa.',
            value=self.__string_processing(stock_identification['name'][0]))

        return {'name': name, 'ticker': ticker}

    def __transformation_of_financial_summary(self,
                                              financial_summary: dict) -> Dict:
        """
        Transform raw financial summary information into structured data.

        This method processes raw financial summary information, including market valuation,
        enterprise valuation, number of shares, the last financial statement date, sector,
        and subsector, into a dictionary with InformationItem instances. It handles the cleaning
        and formatting of the raw data to ensure it is properly structured and ready for further
        financial analysis or storage.

        Args:
            financial_summary (dict): A dictionary containing the raw financial summary
            information with keys such as 'market_valuation', 'enterprise_valuation',
            'number_of_shares', 'last_financial_statement', 'sector', and 'subsector'.
            Each key is associated with a list of raw data values including a title,
            tooltip, and value.

        Returns:
            Dict: A dictionary with keys like 'market_valuation', 'enterprise_valuation',
            'number_of_shares', 'last_financial_statement', 'sector', and 'subsector',
            where each key is associated with an InformationItem instance containing
            cleaned and structured data.
        """

        market_valuation = InformationItem(
            title=self.__string_processing(financial_summary['market_valuation'][0]),
            tooltip=self.__string_processing(financial_summary['market_valuation'][1]),
            value=self.__number_processing(financial_summary['market_valuation'][2]))

        enterprise_valuation = InformationItem(
            title=self.__string_processing(financial_summary['enterprise_valuation'][0]),
            tooltip=self.__string_processing(financial_summary['enterprise_valuation'][1]),
            value=self.__number_processing(financial_summary['enterprise_valuation'][2]))

        number_of_shares = InformationItem(
            title=self.__string_processing(financial_summary['number_of_shares'][0]),
            tooltip=self.__string_processing(financial_summary['number_of_shares'][1]),
            value=self.__number_processing(financial_summary['number_of_shares'][2]))

        last_financial_statement = InformationItem(
            title=self.__string_processing(financial_summary['last_financial_statement'][0]),
            tooltip=self.__string_processing(financial_summary['last_financial_statement'][1]),
            value=self.__string_processing(financial_summary['last_financial_statement'][2]))

        sector = InformationItem(
            title=self.__string_processing(financial_summary['sector'][0]),
            tooltip=self.__string_processing(financial_summary['sector'][1]),
            value=self.__string_processing(financial_summary['sector'][2]))

        subsector = InformationItem(
            title=self.__string_processing(financial_summary['subsector'][0]),
            tooltip=self.__string_processing(financial_summary['subsector'][1]),
            value=self.__string_processing(financial_summary['subsector'][2]))

        return {
            'market_valuation': market_valuation,
            'enterprise_valuation': enterprise_valuation,
            'number_of_shares': number_of_shares,
            'last_financial_statement': last_financial_statement,
            'sector': sector,
            'subsector': subsector
        }

    def __transformation_of_price_information(self,
                                              price_information: Dict) -> Dict:
        """
        Transforms raw price information into a structured dictionary.

        This method processes the raw price information of a stock, including the stock's current
        price and the date of the price, and structures it into a dictionary with InformationItem
        instances. It handles cleaning and formatting of the raw data to ensure it is ready for
        further financial analysis or storage.

        Args:
            price_information (Dict): A dictionary containing the raw price information with keys
            'price' and 'date', each associated with a list of raw data values.

        Returns:
            Dict: A dictionary with keys 'price' and 'date', where each key is associated with an
            InformationItem instance containing cleaned and structured data.
        """

        price = InformationItem(
            title=self.__string_processing(price_information['price'][0]),
            tooltip=self.__string_processing(price_information['price'][1]),
            value=self.__number_processing(price_information['price'][2]))

        date = InformationItem(
            title=self.__string_processing(price_information['date'][0]),
            tooltip=self.__string_processing(price_information['date'][1]),
            value=self.__string_processing(price_information['date'][2]))

        return {'price': price, 'date': date}

    def __transformation_of_detailed_information(
            self, detailed_information: Dict) -> Dict:
        """
        Transform detailed information of a stock into structured data.

        Takes raw detailed information about a stock, including stock type,
        traded volume per day, equity value per share, and earnings per share,
        and converts it into a structured form using InformationItem contracts.

        Args:
            detailed_information (Dict): A dictionary containing raw detailed
                                         information of a stock.

        Returns:
            Dict: A dictionary of transformed detailed information structured
                  as InformationItem instances.
        """

        stock_type = InformationItem(
            title=self.__string_processing(
                detailed_information['stock_type'][0]),
            tooltip=self.__string_processing(
                detailed_information['stock_type'][1]),
            value=self.__string_processing(
                detailed_information['stock_type'][2]))

        traded_volume_per_day = InformationItem(
            title=self.__string_processing(
                detailed_information['traded_volume_per_day'][0]),
            tooltip=self.__string_processing(
                detailed_information['traded_volume_per_day'][1]),
            value=self.__number_processing(
                detailed_information['traded_volume_per_day'][2]))

        equity_value_per_share = InformationItem(
            title=self.__string_processing(
                detailed_information['equity_value_per_share'][0]),
            tooltip=self.__string_processing(
                detailed_information['equity_value_per_share'][1]),
            value=self.__number_processing(
                detailed_information['equity_value_per_share'][2]))

        earnings_per_share = InformationItem(
            title=self.__string_processing(
                detailed_information['earnings_per_share'][0]),
            tooltip=self.__string_processing(
                detailed_information['earnings_per_share'][1]),
            value=self.__number_processing(
                detailed_information['earnings_per_share'][2]))

        lowest_value = InformationItem(
            title='Mínimo',
            tooltip=self.__string_processing(
                detailed_information['variation_52_weeks']['lowest_value'][0]),
            value=self.__number_processing(
                detailed_information['variation_52_weeks']['lowest_value'][1]))

        highest_value = InformationItem(
            title='Máximo',
            tooltip=self.__string_processing(
                detailed_information['variation_52_weeks']['highest_value']
                [0]),
            value=self.__number_processing(
                detailed_information['variation_52_weeks']['highest_value']
                [1]))

        return {
            'stock_type': stock_type,
            'traded_volume_per_day': traded_volume_per_day,
            'equity_value_per_share': equity_value_per_share,
            'earnings_per_share': earnings_per_share,
            'variation_52_weeks': {
                'lowest_value': lowest_value,
                'highest_value': highest_value
            }
        }

    def __transformation_of_oscillations(
            self, oscillations_information: Dict) -> Dict:
        """
        Transform stock oscillation information into structured data.

        Processes raw data related to stock price oscillations over
        different time periods into a structured format, facilitating
        further analysis.

        Args:
            oscillations_information (Dict): Raw data about stock price oscillations.

        Returns:
            Dict: Structured oscillation information, organized into InformationItem
            instances for each time period.
        """

        variation_day = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_day'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_day'][1]))

        variation_month = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_month'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_month'][1]))

        variation_30_days = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_30_days'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_30_days'][1]))

        variation_12_months = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_12_months'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_12_months'][1]))

        variation_2022 = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_2022'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_2022'][1]))

        variation_2021 = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_2021'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_2021'][1]))

        variation_2020 = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_2020'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_2020'][1]))

        variation_2019 = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_2019'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_2019'][1]))

        variation_2018 = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_2018'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_2018'][1]))

        variation_2017 = InformationItem(
            title=self.__string_processing(
                oscillations_information['variation_2017'][0]),
            tooltip='',
            value=self.__number_processing(
                oscillations_information['variation_2017'][1]))

        return {
            'variation_day': variation_day,
            'variation_month': variation_month,
            'variation_30_days': variation_30_days,
            'variation_12_months': variation_12_months,
            'variation_2022': variation_2022,
            'variation_2021': variation_2021,
            'variation_2020': variation_2020,
            'variation_2019': variation_2019,
            'variation_2018': variation_2018,
            'variation_2017': variation_2017
        }

    def __transformation_of_valuation_indicators(
            self, valuation_indicators: Dict) -> Dict:
        """
        Transform valuation indicators into structured data for analysis.

        Converts raw valuation indicators, including price to earnings ratio,
        price to book value, and dividend yield, among others, into a structured
        and easily consumable format.

        Args:
            valuation_indicators (Dict): Raw valuation indicators of a stock.

        Returns:
            Dict: A dictionary containing structured valuation indicators,
                  each represented as an InformationItem.
    """

        price_divided_by_profit_title = InformationItem(
            title=self.__string_processing(
                valuation_indicators['price_divided_by_profit_title'][0]),
            tooltip=self.__string_processing(
                valuation_indicators['price_divided_by_profit_title'][1]),
            value=self.__number_processing(
                valuation_indicators['price_divided_by_profit_title'][2]))

        price_divided_by_asset_value = InformationItem(
            title=self.__string_processing(
                valuation_indicators['price_divided_by_asset_value'][0]),
            tooltip=self.__string_processing(
                valuation_indicators['price_divided_by_asset_value'][1]),
            value=self.__number_processing(
                valuation_indicators['price_divided_by_asset_value'][2]))

        price_divided_by_ebit = InformationItem(
            title=self.__string_processing(
                valuation_indicators['price_divided_by_ebit'][0]),
            tooltip=self.__string_processing(
                valuation_indicators['price_divided_by_ebit'][1]),
            value=self.__number_processing(
                valuation_indicators['price_divided_by_ebit'][2]))

        price_divided_by_net_revenue = InformationItem(
            title=self.__string_processing(
                valuation_indicators['price_divided_by_net_revenue'][0]),
            tooltip=self.__string_processing(
                valuation_indicators['price_divided_by_net_revenue'][1]),
            value=self.__number_processing(
                valuation_indicators['price_divided_by_net_revenue'][2]))

        price_divided_by_total_assets = InformationItem(
            title=self.__string_processing(
                valuation_indicators['price_divided_by_total_assets'][0]),
            tooltip=self.__string_processing(
                valuation_indicators['price_divided_by_total_assets'][1]),
            value=self.__number_processing(
                valuation_indicators['price_divided_by_total_assets'][2]))

        price_divided_by_net_current_assets = InformationItem(
            title=self.__string_processing(
                valuation_indicators['price_divided_by_net_current_assets']
                [0]),
            tooltip=self.__string_processing(
                valuation_indicators['price_divided_by_net_current_assets']
                [1]),
            value=self.__number_processing(
                valuation_indicators['price_divided_by_net_current_assets']
                [2]))

        dividend_yield = InformationItem(
            title=self.__string_processing(
                valuation_indicators['dividend_yield'][0]),
            tooltip=self.__string_processing(
                valuation_indicators['dividend_yield'][1]),
            value=self.__number_processing(
                valuation_indicators['dividend_yield'][2]))

        enterprise_value_by_ebitda = InformationItem(
            title=self.__string_processing(
                valuation_indicators['enterprise_value_by_ebitda'][0]),
            tooltip=self.__string_processing(
                valuation_indicators['enterprise_value_by_ebitda'][1]),
            value=self.__number_processing(
                valuation_indicators['enterprise_value_by_ebitda'][2]))

        enterprise_value_by_ebit = InformationItem(
            title=self.__string_processing(
                valuation_indicators['enterprise_value_by_ebit'][0]),
            tooltip=self.__string_processing(
                valuation_indicators['enterprise_value_by_ebit'][1]),
            value=self.__number_processing(
                valuation_indicators['enterprise_value_by_ebit'][2]))

        price_by_working_capital = InformationItem(
            title=self.__string_processing(
                valuation_indicators['price_by_working_capital'][0]),
            tooltip=self.__string_processing(
                valuation_indicators['price_by_working_capital'][1]),
            value=self.__number_processing(
                valuation_indicators['price_by_working_capital'][2]))

        return {
            'price_divided_by_profit_title': price_divided_by_profit_title,
            'price_divided_by_asset_value': price_divided_by_asset_value,
            'price_divided_by_ebit': price_divided_by_ebit,
            'price_divided_by_net_revenue': price_divided_by_net_revenue,
            'price_divided_by_total_assets': price_divided_by_total_assets,
            'price_divided_by_net_current_assets':
            price_divided_by_net_current_assets,
            'dividend_yield': dividend_yield,
            'enterprise_value_by_ebitda': enterprise_value_by_ebitda,
            'enterprise_value_by_ebit': enterprise_value_by_ebit,
            'price_by_working_capital': price_by_working_capital
        }

    def __transformation_of_profitability_indicators(
            self, profitability_indicators: Dict) -> Dict:
        """
        Transform profitability indicators into structured data.

        Takes raw data on profitability metrics such as return on equity,
        return on invested capital, and net revenue growth, and structures
        them for easy analysis.

        Args:
            profitability_indicators (Dict): Raw profitability indicators of a stock.

        Returns:
            Dict: Structured profitability indicators, each encapsulated
                  in an InformationItem.
        """

        return_on_equity = InformationItem(
            title=self.__string_processing(
                profitability_indicators['return_on_equity'][0]),
            tooltip=self.__string_processing(
                profitability_indicators['return_on_equity'][1]),
            value=self.__number_processing(
                profitability_indicators['return_on_equity'][2]))

        return_on_invested_capital = InformationItem(
            title=self.__string_processing(
                profitability_indicators['return_on_invested_capital'][0]),
            tooltip=self.__string_processing(
                profitability_indicators['return_on_invested_capital'][1]),
            value=self.__number_processing(
                profitability_indicators['return_on_invested_capital'][2]))

        ebit_divided_by_total_assets = InformationItem(
            title=self.__string_processing(
                profitability_indicators['ebit_divided_by_total_assets'][0]),
            tooltip=self.__string_processing(
                profitability_indicators['ebit_divided_by_total_assets'][1]),
            value=self.__number_processing(
                profitability_indicators['ebit_divided_by_total_assets'][2]))

        net_revenue_growth_last_5_years = InformationItem(
            title=self.__string_processing(
                profitability_indicators['net_revenue_growth_last_5_years']
                [0]),
            tooltip=self.__string_processing(
                profitability_indicators['net_revenue_growth_last_5_years']
                [1]),
            value=self.__number_processing(
                profitability_indicators['net_revenue_growth_last_5_years']
                [2]))

        net_revenue_divided_by_total_assets = InformationItem(
            title=self.__string_processing(
                profitability_indicators['net_revenue_divided_by_total_assets']
                [0]),
            tooltip=self.__string_processing(
                profitability_indicators['net_revenue_divided_by_total_assets']
                [1]),
            value=self.__number_processing(
                profitability_indicators['net_revenue_divided_by_total_assets']
                [2]))

        gross_profit_divided_by_net_revenue = InformationItem(
            title=self.__string_processing(
                profitability_indicators['gross_profit_divided_by_net_revenue']
                [0]),
            tooltip=self.__string_processing(
                profitability_indicators['gross_profit_divided_by_net_revenue']
                [1]),
            value=self.__number_processing(
                profitability_indicators['gross_profit_divided_by_net_revenue']
                [2]))

        ebit_divided_by_net_revenue = InformationItem(
            title=self.__string_processing(
                profitability_indicators['ebit_divided_by_net_revenue'][0]),
            tooltip=self.__string_processing(
                profitability_indicators['ebit_divided_by_net_revenue'][1]),
            value=self.__number_processing(
                profitability_indicators['ebit_divided_by_net_revenue'][2]))

        net_income_divided_by_net_revenue = InformationItem(
            title=self.__string_processing(
                profitability_indicators['net_income_divided_by_net_revenue']
                [0]),
            tooltip=self.__string_processing(
                profitability_indicators['net_income_divided_by_net_revenue']
                [1]),
            value=self.__number_processing(
                profitability_indicators['net_income_divided_by_net_revenue']
                [2]))

        return {
            'return_on_equity': return_on_equity,
            'return_on_invested_capital': return_on_invested_capital,
            'ebit_divided_by_total_assets': ebit_divided_by_total_assets,
            'net_revenue_growth_last_5_years': net_revenue_growth_last_5_years,
            'net_revenue_divided_by_total_assets':
            net_revenue_divided_by_total_assets,
            'gross_profit_divided_by_net_revenue':
            gross_profit_divided_by_net_revenue,
            'ebit_divided_by_net_revenue': ebit_divided_by_net_revenue,
            'net_income_divided_by_net_revenue':
            net_income_divided_by_net_revenue
        }

    def __transformation_of_indebtedness_indicators(
            self, indebtedness_indicators: Dict) -> Dict:
        """
        Transform indebtedness indicators into structured data.

        Processes raw data on a company's indebtedness, such as
        current liquidity and debt to equity ratios, into a structured
        format for further financial analysis.

        Args:
            indebtedness_indicators (Dict): Raw indebtedness indicators.

        Returns:
            Dict: A dictionary of structured indebtedness indicators,
                  organized as InformationItem instances.
        """

        current_liquidity = InformationItem(
            title=self.__string_processing(
                indebtedness_indicators['current_liquidity'][0]),
            tooltip=self.__string_processing(
                indebtedness_indicators['current_liquidity'][1]),
            value=self.__number_processing(
                indebtedness_indicators['current_liquidity'][2]))

        gross_debt_by_equity = InformationItem(
            title=self.__string_processing(
                indebtedness_indicators['gross_debt_by_equity'][0]),
            tooltip=self.__string_processing(
                indebtedness_indicators['gross_debt_by_equity'][1]),
            value=self.__number_processing(
                indebtedness_indicators['gross_debt_by_equity'][2]))

        net_debt_by_equity = InformationItem(
            title=self.__string_processing(
                indebtedness_indicators['net_debt_by_equity'][0]),
            tooltip=self.__string_processing(
                indebtedness_indicators['net_debt_by_equity'][1]),
            value=self.__number_processing(
                indebtedness_indicators['net_debt_by_equity'][2]))

        net_debt_by_ebitda = InformationItem(
            title=self.__string_processing(
                indebtedness_indicators['net_debt_by_ebitda'][0]),
            tooltip=self.__string_processing(
                indebtedness_indicators['net_debt_by_ebitda'][1]),
            value=self.__number_processing(
                indebtedness_indicators['net_debt_by_ebitda'][2]))

        equity_by_total_assets = InformationItem(
            title=self.__string_processing(
                indebtedness_indicators['equity_by_total_assets'][0]),
            tooltip=self.__string_processing(
                indebtedness_indicators['equity_by_total_assets'][1]),
            value=self.__number_processing(
                indebtedness_indicators['equity_by_total_assets'][2]))

        return {
            'current_liquidity': current_liquidity,
            'gross_debt_by_equity': gross_debt_by_equity,
            'net_debt_by_equity': net_debt_by_equity,
            'net_debt_by_ebitda': net_debt_by_ebitda,
            'equity_by_total_assets': equity_by_total_assets
        }

    def __transformation_of_balance_sheet(self,
                                          balance_sheet: Dict) -> Dict:
        """
        Transform balance sheet data into a structured format.

        Converts raw balance sheet data, including total assets,
        current assets, and liabilities, into structured information
        suitable for financial analysis.

        Args:
            balance_sheet (Dict): Raw balance sheet data of a company.

        Returns:
            Dict: Structured balance sheet information, formatted
                  as InformationItem instances.
        """

        if len(balance_sheet) == 4:
            total_assets = InformationItem(
                title=self.__string_processing(balance_sheet['total_assets'][0]),
                tooltip=self.__string_processing(balance_sheet['total_assets'][1]),
                value=self.__number_processing(balance_sheet['total_assets'][2]))

            credit_portfolio = InformationItem(
                title=self.__string_processing(balance_sheet['credit_portfolio'][0]),
                tooltip=self.__string_processing(balance_sheet['credit_portfolio'][1]),
                value=self.__number_processing(balance_sheet['credit_portfolio'][2]))

            deposits = InformationItem(
                title=self.__string_processing(balance_sheet['deposits'][0]),
                tooltip=self.__string_processing(balance_sheet['deposits'][1]),
                value=self.__number_processing(balance_sheet['deposits'][2]))
            equity = InformationItem(
                title=self.__string_processing(balance_sheet['equity'][0]),
                tooltip=self.__string_processing(balance_sheet['equity'][1]),
                value=self.__number_processing(balance_sheet['equity'][2]))

            return {
                'total_assets': total_assets,
                'credit_portfolio': credit_portfolio,
                'deposits': deposits,
                'equity': equity
            }

        total_assets = InformationItem(
            title=self.__string_processing(balance_sheet['total_assets'][0]),
            tooltip=self.__string_processing(balance_sheet['total_assets'][1]),
            value=self.__number_processing(balance_sheet['total_assets'][2]))

        current_assets = InformationItem(
            title=self.__string_processing(balance_sheet['current_assets'][0]),
            tooltip=self.__string_processing(balance_sheet['current_assets'][1]),
            value=self.__number_processing(balance_sheet['current_assets'][2]))

        cash = InformationItem(
            title=self.__string_processing(balance_sheet['cash'][0]),
            tooltip=self.__string_processing(balance_sheet['cash'][1]),
            value=self.__number_processing(balance_sheet['cash'][2]))

        gross_debt = InformationItem(
            title=self.__string_processing(balance_sheet['gross_debt'][0]),
            tooltip=self.__string_processing(balance_sheet['gross_debt'][1]),
            value=self.__number_processing(balance_sheet['gross_debt'][2]))

        net_debt = InformationItem(
            title=self.__string_processing(balance_sheet['net_debt'][0]),
            tooltip=self.__string_processing(balance_sheet['net_debt'][1]),
            value=self.__number_processing(balance_sheet['net_debt'][2]))

        equity = InformationItem(
            title=self.__string_processing(balance_sheet['equity'][0]),
            tooltip=self.__string_processing(balance_sheet['equity'][1]),
            value=self.__number_processing(balance_sheet['equity'][2]))

        return {
            'total_assets': total_assets,
            'current_assets': current_assets,
            'cash': cash,
            'gross_debt': gross_debt,
            'net_debt': net_debt,
            'equity': equity
        }

    def __transformation_of_income_statement(self,
                                             income_statement: Dict) -> Dict:
        """
        Transform income statement data into a structured format.

        Processes raw income statement data, detailing revenue, EBIT,
        and net income over specific periods, into a structured format
        for easy access and analysis.

        Args:
            income_statement (Dict): Raw data of a company's income statement.

        Returns:
            Dict: Structured income statement information, encapsulated
                  in InformationItem instances.
        """

        twelve_months_revenue = InformationItem(
            title=self.__string_processing(
                income_statement['twelve_months']['revenue'][0]),
            tooltip=self.__string_processing(
                income_statement['twelve_months']['revenue'][1]),
            value=self.__number_processing(
                income_statement['twelve_months']['revenue'][2]))

        twelve_months_ebit = InformationItem(
            title=self.__string_processing(
                income_statement['twelve_months']['ebit'][0]),
            tooltip=self.__string_processing(
                income_statement['twelve_months']['ebit'][1]),
            value=self.__number_processing(
                income_statement['twelve_months']['ebit'][2]))

        twelve_months_net_income = InformationItem(
            title=self.__string_processing(
                income_statement['twelve_months']['net_income'][0]),
            tooltip=self.__string_processing(
                income_statement['twelve_months']['net_income'][1]),
            value=self.__number_processing(
                income_statement['twelve_months']['net_income'][2]))

        three_months_net_revenue = InformationItem(
            title=self.__string_processing(
                income_statement['three_months']['revenue'][0]),
            tooltip=self.__string_processing(
                income_statement['three_months']['revenue'][1]),
            value=self.__number_processing(
                income_statement['three_months']['revenue'][2]))

        three_months_net_ebit = InformationItem(
            title=self.__string_processing(
                income_statement['three_months']['ebit'][0]),
            tooltip=self.__string_processing(
                income_statement['three_months']['ebit'][1]),
            value=self.__number_processing(
                income_statement['three_months']['ebit'][2]))

        three_months_net_net_income = InformationItem(
            title=self.__string_processing(
                income_statement['three_months']['net_income'][0]),
            tooltip=self.__string_processing(
                income_statement['three_months']['net_income'][1]),
            value=self.__number_processing(
                income_statement['three_months']['net_income'][2]))

        return {
            'three_months': {
                'revenue': three_months_net_revenue,
                'ebit': three_months_net_ebit,
                'net_income': three_months_net_net_income
            },
            'twelve_months': {
                'revenue': twelve_months_revenue,
                'ebit': twelve_months_ebit,
                'net_income': twelve_months_net_income
            }
        }

    def __make_transformation(self, raw_information: Dict) -> Dict:
        """
        Perform the comprehensive transformation of raw financial information.

        This method orchestrates the transformation of raw financial data into a
        structured format across multiple dimensions, including price information,
        detailed stock metrics, oscillations, valuation indicators, profitability
        indicators, indebtedness indicators, balance sheet details, and income statements.
        It leverages other private methods within the class to process each segment
        of data individually and then combines them into a comprehensive, structured
        dictionary ready for further analysis or storage.

        The method ensures that all relevant financial information is processed
        and structured uniformly, facilitating easy access and analysis of financial
        metrics for the stocks in question.

        Args:
            raw_information (Dict): A dictionary containing all the raw financial
            data for a stock, organized by data categories (e.g., price information,
            detailed information, etc.).

        Returns:
            Dict: A dictionary containing all the transformed financial information,
            where each category of data is structured into dictionaries or
            InformationItem instances, providing a comprehensive view of the
            financial metrics for further analysis.

        Raises:
            TransformException: An exception is raised if any part of the
            transformation process fails, encapsulating the original
            exception for debugging purposes.

        Example:
            >>> raw_info = {
                    "price": {"price": ["Price", "", "100"],
                    "date": ["Date", "", "2021-01-01"]},
                    "detailed_information": {"stock_type": ["Stock Type", "", "Common"]},
                    ...
                }
            >>> transformed_info = __make_transformation(raw_info)
            >>> print(transformed_info.keys())
            dict_keys(['price_information', 'detailed_information', 'oscillations', ...])
        """

        # Processing stock identification information.
        stock_identification = self.__transformation_of_stock_identification(
            raw_information['identification'])

        # Processing stock Financial Summary.
        financial_summary = self.__transformation_of_financial_summary(
            raw_information['financial_summary'])

        # Processing stock price information.
        price_information = self.__transformation_of_price_information(
            raw_information['price'])

        # Processing detailed stock information.
        detailed_information = self.__transformation_of_detailed_information(
            raw_information['detailed_information'])

        # Processing stock price oscillation information.
        oscillations = self.__transformation_of_oscillations(
            raw_information['oscillations'])

        # Processing stock valuation indicators.
        valuation_indicators = self.__transformation_of_valuation_indicators(
            raw_information['valuation_indicators'])

        # Processing stock profitability indicators.
        profitability_indicators = self.__transformation_of_profitability_indicators(
            raw_information['profitability_indicators'])

        # Processing stock indebtedness indicators.
        indebtedness_indicators = self.__transformation_of_indebtedness_indicators(
            raw_information['indebtedness_indicators'])

        # Processing stock balance sheet indicators.
        balance_sheet = self.__transformation_of_balance_sheet(
            raw_information['balance_sheet'])

        # Processing stock income statement information.
        income_statement = self.__transformation_of_income_statement(
            raw_information['income_statement'])

        return {
            'stock_identification': stock_identification,
            'financial_summary': financial_summary,
            'price_information': price_information,
            'detailed_information': detailed_information,
            'oscillations': oscillations,
            'valuation_indicators': valuation_indicators,
            'profitability_indicators': profitability_indicators,
            'indebtedness_indicators': indebtedness_indicators,
            'balance_sheet': balance_sheet,
            'income_statement': income_statement
        }

    def __make_transformation_companies(self, raw_information: str) -> List[Dict[str, str]]:
        """
        Transforms raw company information into a structured list of dictionaries.

        Each dictionary in the list contains cleaned and structured information about a company,
        including its code, name, corporate name, and a link to its detailed page.

        Args:
            raw_information (str): Raw string information about companies.

        Returns:
            List[Dict[str, str]]: A list of dictionaries, where each dictionary contains structured
            information about a company.
        """

        transformed = []
        for information in raw_information:
            code = self.__remove_all_spaces(
                self.__remove_new_lines(information['code']))
            name = self.__remove_new_lines(information['name']).strip().upper()
            corporate_name = self.__remove_new_lines(
                information['corporate_name']).strip().upper()
            partial_link = self.__remove_all_spaces(
                self.__remove_new_lines(information['link']))
            full_link = f'https://www.fundamentus.com.br/{partial_link}'

            transformed.append({
                'code': code,
                'name': name,
                'corporate_name': corporate_name,
                'link': full_link
            })

        return transformed

    def __make_transformation_property_funds(self,
                                             raw_information: str) -> List[Dict[str, str]]:
        """
        Transforms raw property fund information into a structured list of dictionaries.

        This method processes information related to property funds, structuring it into a list where
        each item is a dictionary containing the fund's code, name, and a link to its detailed information.

        Args:
            raw_information (str): Raw string information about property funds.

        Returns:
            List[Dict[str, str]]: A list of dictionaries, each containing structured information
            about a property fund.
        """

        transformed = []
        for information in raw_information:
            code = self.__remove_all_spaces(
                self.__remove_new_lines(information['code']))
            name = self.__remove_new_lines(information['name']).strip().upper()
            partial_link = self.__remove_all_spaces(
                self.__remove_new_lines(information['link']))
            full_link = f'https://www.fundamentus.com.br/{partial_link}'

            transformed.append({'code': code, 'name': name, 'link': full_link})

        return transformed

    def transform_all_information(
            self, extract_contract: ExtractContract) -> TransformContract:
        """
        Transforms all extracted information from an ExtractContract into a structured TransformContract.

        This comprehensive transformation covers all aspects of financial data, including price info,
        detailed stock information, oscillations, and various indicators relevant for financial analysis.

        Args:
            extract_contract (ExtractContract): The contract containing all raw extracted information.

        Returns:
            TransformContract: A contract containing all transformed information, structured for easy
                               access and analysis.

        Raises:
            TransformException: If an error occurs during the transformation process.
        """

        try:
            transform_information = self.__make_transformation(
                extract_contract.raw_information)

            transform_contract = TransformContract(
                transformed_information=transform_information)

            return transform_contract
        except Exception as exception:
            raise TransformException(exception) from exception

    def transform_companies(
            self, extract_contract: ExtractContract) -> TransformContract:
        """
        Transforms extracted company information from an ExtractContract into a TransformContract.

        Specifically focuses on transforming information related to companies, preparing it for further
        analysis or database storage.

        Args:
            extract_contract (ExtractContract): The contract containing raw extracted company information.

        Returns:
            TransformContract: A contract with transformed company information, structured and ready for use.

        Raises:
            TransformException: If an error occurs during the transformation of company information.
        """

        try:
            transform_information = self.__make_transformation_companies(
                extract_contract.raw_information)

            transform_contract = TransformContract(
                transformed_information=transform_information)

            return transform_contract
        except Exception as exception:
            raise TransformException(exception) from exception

    def transform_property_funds(
            self, extract_contract: ExtractContract) -> TransformContract:
        """
        Transforms extracted property fund information from an ExtractContract into a TransformContract.

        Processes raw data about property funds, structuring it for further analysis or inclusion in
        financial databases.

        Args:
            extract_contract (ExtractContract): The contract containing raw extracted information about property funds.

        Returns:
            TransformContract: A contract containing structured information on property funds, ready for further use.

        Raises:
            TransformException: If an error occurs during the transformation of property fund information.
        """

        try:
            transform_information = self.__make_transformation_property_funds(
                extract_contract.raw_information)
            transform_contract = TransformContract(
                transformed_information=transform_information)

            return transform_contract
        except Exception as exception:
            raise TransformException(exception) from exception
