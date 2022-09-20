#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: transform_raw_information.py
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
"""Transform raw information from the HTTP requester."""

from typing import Dict

from decimal import Decimal

from fundamentus.contracts.extract_contract import ExtractContract
from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.exceptions.transform_exception import TransformException


# pylint: disable=too-few-public-methods
# pylint: disable=too-many-statements
class TransformRawInformation:
    """Represents a raw information transformer."""

    def __remove_new_lines(self, string: str) -> str:
        """Remove all newline from the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace('\n', '')

    def __remove_all_spaces(self, string: str) -> str:
        """Remove all spaces from the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace(' ', '')

    def __string_processing(self, string: str) -> str:
        """Process the string.

        :param string: string to be processed.
        :return: processed string.
        """

        # Remove all \n from the string.
        if '\n' in string:
            string = self.__remove_new_lines(string)

        # Remove question mark from the string.
        if '?' in string:
            string = string.replace('?', '')

        return string.strip()

    def __remove_dot(self, string: str) -> str:
        """Remove the dot from the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace('.', '')

    def __change_comma_to_dot(self, string: str) -> str:
        """Change the comma to dot in the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace(',', '.')

    def __to_decimal(self, value: str) -> Decimal:
        """Construct a new Decimal object based from value.

        :param value: value to be processed.
        :return: Decimal object.
        """

        if value.endswith('%'):
            value = value[:-1]

            return Decimal(value) / 100

        return Decimal(value) if value is not None else None

    def __remove_currency_symbol(self, number: str) -> str:
        """Remove the currency symbol from the number.

        :param number: number to be processed.
        :return: processed number.
        """

        return number.replace('R$', '')

    def __number_processing(self, number: str) -> Decimal:
        """Process the number.

        :param number: number to be processed.
        :return: processed number.
        """

        return self.__to_decimal(
            self.__remove_currency_symbol(
                self.__change_comma_to_dot(
                    self.__remove_dot(self.__remove_new_lines(number)))))

    def __transformation_of_price_information(self,
                                              price_information: Dict) -> Dict:
        """Make the transformation.

        :param price_information: raw information to be processed.
        :return: processed information.
        """

        price_information['price'][0] = self.__string_processing(
            price_information['price'][0])
        price_information['price'][1] = self.__string_processing(
            price_information['price'][1])
        price_information['price'][2] = self.__number_processing(
            price_information['price'][2])

        price_information['date'][0] = self.__string_processing(
            price_information['date'][0])
        price_information['date'][1] = self.__string_processing(
            price_information['date'][1])
        price_information['date'][2] = self.__string_processing(
            price_information['date'][2])

        return price_information

    def __transformation_of_detailed_information(
            self, detailed_information: Dict) -> Dict:
        """Make the transformation.

        :param detailed_information: raw information to be processed.
        :return: processed information.
        """

        detailed_information['stock_type'][0] = self.__string_processing(
            detailed_information['stock_type'][0])
        detailed_information['stock_type'][1] = self.__string_processing(
            detailed_information['stock_type'][1])
        detailed_information['stock_type'][2] = self.__string_processing(
            detailed_information['stock_type'][2])

        detailed_information['traded_volume_per_day'][
            0] = self.__string_processing(
                detailed_information['traded_volume_per_day'][0])
        detailed_information['traded_volume_per_day'][
            1] = self.__string_processing(
                detailed_information['traded_volume_per_day'][1])
        detailed_information['traded_volume_per_day'][
            2] = self.__number_processing(
                detailed_information['traded_volume_per_day'][2])

        detailed_information['equity_value_per_share'][
            0] = self.__string_processing(
                detailed_information['equity_value_per_share'][0])
        detailed_information['equity_value_per_share'][
            1] = self.__string_processing(
                detailed_information['equity_value_per_share'][1])
        detailed_information['equity_value_per_share'][
            2] = self.__number_processing(
                detailed_information['equity_value_per_share'][2])

        detailed_information['earnings_per_share'][
            0] = self.__string_processing(
                detailed_information['earnings_per_share'][0])
        detailed_information['earnings_per_share'][
            1] = self.__string_processing(
                detailed_information['earnings_per_share'][1])
        detailed_information['earnings_per_share'][
            2] = self.__number_processing(
                detailed_information['earnings_per_share'][2])

        detailed_information['variation_52_weeks']['lowest_value'][
            0] = self.__string_processing(
                detailed_information['variation_52_weeks']['lowest_value'][0])
        detailed_information['variation_52_weeks']['lowest_value'][
            1] = self.__number_processing(
                detailed_information['variation_52_weeks']['lowest_value'][1])

        detailed_information['variation_52_weeks']['highest_value'][
            0] = self.__string_processing(
                detailed_information['variation_52_weeks']['highest_value'][0])
        detailed_information['variation_52_weeks']['highest_value'][
            1] = self.__number_processing(
                detailed_information['variation_52_weeks']['highest_value'][1])

        return detailed_information

    def __transformation_of_oscillations(
            self, oscillations_information: Dict) -> Dict:
        """Make the transformation.

        :param oscillations_information: raw information to be processed.
        :return: processed information.
        """

        oscillations_information['variation_day'] = self.__number_processing(
            oscillations_information['variation_day'])
        oscillations_information['variation_month'] = self.__number_processing(
            oscillations_information['variation_month'])
        oscillations_information[
            'variation_30_days'] = self.__number_processing(
                oscillations_information['variation_30_days'])
        oscillations_information[
            'variation_12_months'] = self.__number_processing(
                oscillations_information['variation_12_months'])
        oscillations_information['variation_2022'] = self.__number_processing(
            oscillations_information['variation_2022'])
        oscillations_information['variation_2021'] = self.__number_processing(
            oscillations_information['variation_2021'])
        oscillations_information['variation_2020'] = self.__number_processing(
            oscillations_information['variation_2020'])
        oscillations_information['variation_2019'] = self.__number_processing(
            oscillations_information['variation_2019'])
        oscillations_information['variation_2018'] = self.__number_processing(
            oscillations_information['variation_2018'])
        oscillations_information['variation_2017'] = self.__number_processing(
            oscillations_information['variation_2017'])

        return oscillations_information

    def __transformation_of_valuation_indicators(
            self, valuation_indicators: Dict) -> Dict:
        """Make the transformation.

        :param valuation_indicators: raw information to be processed.
        :return: processed information.
        """

        valuation_indicators['price_divided_by_profit_title'][
            0] = self.__string_processing(
                valuation_indicators['price_divided_by_profit_title'][0])
        valuation_indicators['price_divided_by_profit_title'][
            1] = self.__string_processing(
                valuation_indicators['price_divided_by_profit_title'][1])
        valuation_indicators['price_divided_by_profit_title'][
            2] = self.__number_processing(
                valuation_indicators['price_divided_by_profit_title'][2])

        valuation_indicators['price_divided_by_asset_value'][
            0] = self.__string_processing(
                valuation_indicators['price_divided_by_asset_value'][0])
        valuation_indicators['price_divided_by_asset_value'][
            1] = self.__string_processing(
                valuation_indicators['price_divided_by_asset_value'][1])
        valuation_indicators['price_divided_by_asset_value'][
            2] = self.__number_processing(
                valuation_indicators['price_divided_by_asset_value'][2])

        valuation_indicators['price_divided_by_ebit'][
            0] = self.__string_processing(
                valuation_indicators['price_divided_by_ebit'][0])
        valuation_indicators['price_divided_by_ebit'][
            1] = self.__string_processing(
                valuation_indicators['price_divided_by_ebit'][1])
        valuation_indicators['price_divided_by_ebit'][
            2] = self.__number_processing(
                valuation_indicators['price_divided_by_ebit'][2])

        valuation_indicators['price_divided_by_net_revenue'][
            0] = self.__string_processing(
                valuation_indicators['price_divided_by_net_revenue'][0])
        valuation_indicators['price_divided_by_net_revenue'][
            1] = self.__string_processing(
                valuation_indicators['price_divided_by_net_revenue'][1])
        valuation_indicators['price_divided_by_net_revenue'][
            2] = self.__number_processing(
                valuation_indicators['price_divided_by_net_revenue'][2])

        valuation_indicators['price_divided_by_total_assets'][
            0] = self.__string_processing(
                valuation_indicators['price_divided_by_total_assets'][0])
        valuation_indicators['price_divided_by_total_assets'][
            1] = self.__string_processing(
                valuation_indicators['price_divided_by_total_assets'][1])
        valuation_indicators['price_divided_by_total_assets'][
            2] = self.__number_processing(
                valuation_indicators['price_divided_by_total_assets'][2])

        valuation_indicators['price_divided_by_net_current_assets'][
            0] = self.__string_processing(
                valuation_indicators['price_divided_by_net_current_assets'][0])
        valuation_indicators['price_divided_by_net_current_assets'][
            1] = self.__string_processing(
                valuation_indicators['price_divided_by_net_current_assets'][1])
        valuation_indicators['price_divided_by_net_current_assets'][
            2] = self.__number_processing(
                valuation_indicators['price_divided_by_net_current_assets'][2])

        valuation_indicators['dividend_yield'][0] = self.__string_processing(
            valuation_indicators['dividend_yield'][0])
        valuation_indicators['dividend_yield'][1] = self.__string_processing(
            valuation_indicators['dividend_yield'][1])
        valuation_indicators['dividend_yield'][2] = self.__number_processing(
            valuation_indicators['dividend_yield'][2])

        valuation_indicators['enterprise_value_by_ebitda'][
            0] = self.__string_processing(
                valuation_indicators['enterprise_value_by_ebitda'][0])
        valuation_indicators['enterprise_value_by_ebitda'][
            1] = self.__string_processing(
                valuation_indicators['enterprise_value_by_ebitda'][1])
        valuation_indicators['enterprise_value_by_ebitda'][
            2] = self.__number_processing(
                valuation_indicators['enterprise_value_by_ebitda'][2])

        valuation_indicators['enterprise_value_by_ebit'][
            0] = self.__string_processing(
                valuation_indicators['enterprise_value_by_ebit'][0])
        valuation_indicators['enterprise_value_by_ebit'][
            1] = self.__string_processing(
                valuation_indicators['enterprise_value_by_ebit'][1])
        valuation_indicators['enterprise_value_by_ebit'][
            2] = self.__number_processing(
                valuation_indicators['enterprise_value_by_ebit'][2])

        valuation_indicators['price_by_working_capital'][
            0] = self.__string_processing(
                valuation_indicators['price_by_working_capital'][0])
        valuation_indicators['price_by_working_capital'][
            1] = self.__string_processing(
                valuation_indicators['price_by_working_capital'][1])
        valuation_indicators['price_by_working_capital'][
            2] = self.__number_processing(
                valuation_indicators['price_by_working_capital'][2])

        return valuation_indicators

    def __transformation_of_profitability_indicators(
            self, profitability_indicators: Dict) -> Dict:
        """Make the transformation.

        :param profitability_indicators: raw information to be processed.
        :return: processed information.
        """

        profitability_indicators['return_on_equity'][
            0] = self.__string_processing(
                profitability_indicators['return_on_equity'][0])
        profitability_indicators['return_on_equity'][
            1] = self.__string_processing(
                profitability_indicators['return_on_equity'][1])
        profitability_indicators['return_on_equity'][
            2] = self.__number_processing(
                profitability_indicators['return_on_equity'][2])

        profitability_indicators['return_on_invested_capital'][
            0] = self.__string_processing(
                profitability_indicators['return_on_invested_capital'][0])
        profitability_indicators['return_on_invested_capital'][
            1] = self.__string_processing(
                profitability_indicators['return_on_invested_capital'][1])
        profitability_indicators['return_on_invested_capital'][
            2] = self.__number_processing(
                profitability_indicators['return_on_invested_capital'][2])

        profitability_indicators['ebit_divided_by_total_assets'][
            0] = self.__string_processing(
                profitability_indicators['ebit_divided_by_total_assets'][0])
        profitability_indicators['ebit_divided_by_total_assets'][
            1] = self.__string_processing(
                profitability_indicators['ebit_divided_by_total_assets'][1])
        profitability_indicators['ebit_divided_by_total_assets'][
            2] = self.__number_processing(
                profitability_indicators['ebit_divided_by_total_assets'][2])

        profitability_indicators['net_revenue_growth_last_5_years'][
            0] = self.__string_processing(
                profitability_indicators['net_revenue_growth_last_5_years'][0])
        profitability_indicators['net_revenue_growth_last_5_years'][
            1] = self.__string_processing(
                profitability_indicators['net_revenue_growth_last_5_years'][1])
        profitability_indicators['net_revenue_growth_last_5_years'][
            2] = self.__number_processing(
                profitability_indicators['net_revenue_growth_last_5_years'][2])

        profitability_indicators['net_revenue_divided_by_total_assets'][
            0] = self.__string_processing(
                profitability_indicators['net_revenue_divided_by_total_assets']
                [0])
        profitability_indicators['net_revenue_divided_by_total_assets'][
            1] = self.__string_processing(
                profitability_indicators['net_revenue_divided_by_total_assets']
                [1])
        profitability_indicators['net_revenue_divided_by_total_assets'][
            2] = self.__number_processing(
                profitability_indicators['net_revenue_divided_by_total_assets']
                [2])

        profitability_indicators['gross_profit_divided_by_net_revenue'][
            0] = self.__string_processing(
                profitability_indicators['gross_profit_divided_by_net_revenue']
                [0])
        profitability_indicators['gross_profit_divided_by_net_revenue'][
            1] = self.__string_processing(
                profitability_indicators['gross_profit_divided_by_net_revenue']
                [1])
        profitability_indicators['gross_profit_divided_by_net_revenue'][
            2] = self.__number_processing(
                profitability_indicators['gross_profit_divided_by_net_revenue']
                [2])

        profitability_indicators['ebit_divided_by_net_revenue'][
            0] = self.__string_processing(
                profitability_indicators['ebit_divided_by_net_revenue'][0])
        profitability_indicators['ebit_divided_by_net_revenue'][
            1] = self.__string_processing(
                profitability_indicators['ebit_divided_by_net_revenue'][1])
        profitability_indicators['ebit_divided_by_net_revenue'][
            2] = self.__number_processing(
                profitability_indicators['ebit_divided_by_net_revenue'][2])

        profitability_indicators['net_income_divided_by_net_revenue'][
            0] = self.__string_processing(
                profitability_indicators['net_income_divided_by_net_revenue']
                [0])
        profitability_indicators['net_income_divided_by_net_revenue'][
            1] = self.__string_processing(
                profitability_indicators['net_income_divided_by_net_revenue']
                [1])
        profitability_indicators['net_income_divided_by_net_revenue'][
            2] = self.__number_processing(
                profitability_indicators['net_income_divided_by_net_revenue']
                [2])

        return profitability_indicators

    def __transformation_of_indebtedness_indicators(
            self, indebtedness_indicators: Dict) -> Dict:
        """Make the transformation.

        :param indebtedness_indicators: raw information to be processed.
        :return: processed information.
        """

        indebtedness_indicators['current_liquidity'][
            0] = self.__string_processing(
                indebtedness_indicators['current_liquidity'][0])
        indebtedness_indicators['current_liquidity'][
            1] = self.__string_processing(
                indebtedness_indicators['current_liquidity'][1])
        indebtedness_indicators['current_liquidity'][
            2] = self.__number_processing(
                indebtedness_indicators['current_liquidity'][2])

        indebtedness_indicators['gross_debt_by_equity'][
            0] = self.__string_processing(
                indebtedness_indicators['gross_debt_by_equity'][0])
        indebtedness_indicators['gross_debt_by_equity'][
            1] = self.__string_processing(
                indebtedness_indicators['gross_debt_by_equity'][1])
        indebtedness_indicators['gross_debt_by_equity'][
            2] = self.__number_processing(
                indebtedness_indicators['gross_debt_by_equity'][2])

        indebtedness_indicators['net_debt_by_equity'][
            0] = self.__string_processing(
                indebtedness_indicators['net_debt_by_equity'][0])
        indebtedness_indicators['net_debt_by_equity'][
            1] = self.__string_processing(
                indebtedness_indicators['net_debt_by_equity'][1])
        indebtedness_indicators['net_debt_by_equity'][
            2] = self.__number_processing(
                indebtedness_indicators['net_debt_by_equity'][2])

        indebtedness_indicators['net_debt_by_ebitda'][
            0] = self.__string_processing(
                indebtedness_indicators['net_debt_by_ebitda'][0])
        indebtedness_indicators['net_debt_by_ebitda'][
            1] = self.__string_processing(
                indebtedness_indicators['net_debt_by_ebitda'][1])
        indebtedness_indicators['net_debt_by_ebitda'][
            2] = self.__number_processing(
                indebtedness_indicators['net_debt_by_ebitda'][2])

        indebtedness_indicators['equity_by_total_assets'][
            0] = self.__string_processing(
                indebtedness_indicators['equity_by_total_assets'][0])
        indebtedness_indicators['equity_by_total_assets'][
            1] = self.__string_processing(
                indebtedness_indicators['equity_by_total_assets'][1])
        indebtedness_indicators['equity_by_total_assets'][
            2] = self.__number_processing(
                indebtedness_indicators['equity_by_total_assets'][2])

        return indebtedness_indicators

    def __transformation_of_balance_sheet(self, balance_sheet: Dict) -> Dict:
        """Make the transformation.

        :param balance_sheet: raw information to be processed.
        :return: processed information.
        """

        balance_sheet['total_assets'][0] = self.__string_processing(
            balance_sheet['total_assets'][0])
        balance_sheet['total_assets'][1] = self.__string_processing(
            balance_sheet['total_assets'][1])
        balance_sheet['total_assets'][2] = self.__number_processing(
            balance_sheet['total_assets'][2])

        balance_sheet['current_assets'][0] = self.__string_processing(
            balance_sheet['current_assets'][0])
        balance_sheet['current_assets'][1] = self.__string_processing(
            balance_sheet['current_assets'][1])
        balance_sheet['current_assets'][2] = self.__number_processing(
            balance_sheet['current_assets'][2])

        balance_sheet['cash'][0] = self.__string_processing(
            balance_sheet['cash'][0])
        balance_sheet['cash'][1] = self.__string_processing(
            balance_sheet['cash'][1])
        balance_sheet['cash'][2] = self.__number_processing(
            balance_sheet['cash'][2])

        balance_sheet['gross_debt'][0] = self.__string_processing(
            balance_sheet['gross_debt'][0])
        balance_sheet['gross_debt'][1] = self.__string_processing(
            balance_sheet['gross_debt'][1])
        balance_sheet['gross_debt'][2] = self.__number_processing(
            balance_sheet['gross_debt'][2])

        balance_sheet['net_debt'][0] = self.__string_processing(
            balance_sheet['net_debt'][0])
        balance_sheet['net_debt'][1] = self.__string_processing(
            balance_sheet['net_debt'][1])
        balance_sheet['net_debt'][2] = self.__number_processing(
            balance_sheet['net_debt'][2])

        balance_sheet['equity'][0] = self.__string_processing(
            balance_sheet['equity'][0])
        balance_sheet['equity'][1] = self.__string_processing(
            balance_sheet['equity'][1])
        balance_sheet['equity'][2] = self.__number_processing(
            balance_sheet['equity'][2])

        return balance_sheet

    def __transformation_of_income_statement(self,
                                             income_statement: Dict) -> Dict:
        """Make the transformation.

        :param income_statement: raw information to be processed.
        :return: processed information.
        """

        income_statement['twelve_months']['revenue'][
            0] = self.__string_processing(
                income_statement['twelve_months']['revenue'][0])
        income_statement['twelve_months']['revenue'][
            1] = self.__string_processing(
                income_statement['twelve_months']['revenue'][1])
        income_statement['twelve_months']['revenue'][
            2] = self.__number_processing(
                income_statement['twelve_months']['revenue'][2])

        income_statement['twelve_months']['ebit'][
            0] = self.__string_processing(
                income_statement['twelve_months']['ebit'][0])
        income_statement['twelve_months']['ebit'][
            1] = self.__string_processing(
                income_statement['twelve_months']['ebit'][1])
        income_statement['twelve_months']['ebit'][
            2] = self.__number_processing(
                income_statement['twelve_months']['ebit'][2])

        income_statement['twelve_months']['net_income'][
            0] = self.__string_processing(
                income_statement['twelve_months']['net_income'][0])
        income_statement['twelve_months']['net_income'][
            1] = self.__string_processing(
                income_statement['twelve_months']['net_income'][1])
        income_statement['twelve_months']['net_income'][
            2] = self.__number_processing(
                income_statement['twelve_months']['net_income'][2])

        income_statement['three_months']['revenue'][
            0] = self.__string_processing(
                income_statement['three_months']['revenue'][0])
        income_statement['three_months']['revenue'][
            1] = self.__string_processing(
                income_statement['three_months']['revenue'][1])
        income_statement['three_months']['revenue'][
            2] = self.__number_processing(
                income_statement['three_months']['revenue'][2])

        income_statement['three_months']['ebit'][0] = self.__string_processing(
            income_statement['three_months']['ebit'][0])
        income_statement['three_months']['ebit'][1] = self.__string_processing(
            income_statement['three_months']['ebit'][1])
        income_statement['three_months']['ebit'][2] = self.__number_processing(
            income_statement['three_months']['ebit'][2])

        income_statement['three_months']['net_income'][
            0] = self.__string_processing(
                income_statement['three_months']['net_income'][0])
        income_statement['three_months']['net_income'][
            1] = self.__string_processing(
                income_statement['three_months']['net_income'][1])
        income_statement['three_months']['net_income'][
            2] = self.__number_processing(
                income_statement['three_months']['net_income'][2])

        return income_statement

    def __make_transformation(self, raw_information: Dict) -> Dict:
        """Make the transformation.

        :param raw_information: Dict: Raw information.
        :return: Dict: Transformed information.
        """

        # Processando as informação do preço da ação.
        price_information = self.__transformation_of_price_information(
            raw_information['price'])

        # Processando informações detalhadas da ação.
        detailed_information = self.__transformation_of_detailed_information(
            raw_information['detailed_information'])

        # Processando informações das oscilações da contação da ação.
        oscillations = self.__transformation_of_oscillations(
            raw_information['oscillations'])

        # Processando informações dos indicadores de avaliação da ação.
        valuation_indicators = self.__transformation_of_valuation_indicators(
            raw_information['valuation_indicators'])

        # Processando informações dos indicadores de indicadores de rentabilidade da ação.
        profitability_indicators = self.__transformation_of_profitability_indicators(
            raw_information['profitability_indicators'])

        # Processando informações dos indicadores de indicadores de endividamento da ação.
        indebtedness_indicators = self.__transformation_of_indebtedness_indicators(
            raw_information['indebtedness_indicators'])

        # Processando informações dos indicadores de indicadores de balanço patrimonial da ação.
        balance_sheet = self.__transformation_of_balance_sheet(
            raw_information['balance_sheet'])

        # Processando informações dos indicadores de indicadores de
        # demostrativo de resultados da ação.
        income_statement = self.__transformation_of_income_statement(
            raw_information['income_statement'])

        return {
            'price_information': price_information,
            'detailed_information': detailed_information,
            'oscillations': oscillations,
            'valuation_indicators': valuation_indicators,
            'profitability_indicators': profitability_indicators,
            'indebtedness_indicators': indebtedness_indicators,
            'balance_sheet': balance_sheet,
            'income_statement': income_statement
        }

    def __make_transformation_companies(self, raw_information: str) -> Dict:
        """Make the transformation.

        :param raw_information: raw information to be processed.
        :return: processed information.
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
                                             raw_information: str) -> Dict:
        """Make the transformation.

        :param raw_information: raw information to be processed.
        :return: processed information.
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

    def transform_information(
            self, extract_contract: ExtractContract) -> TransformContract:
        """Transform the raw information.

        :param extract_contract: ExtractContract: Extract contract.
        :return: TransformContract: Transform contract.
        :raises TransformException: if the transform fails.
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
        """Transform the raw information of companies.

        :param extract_contract: ExtractContract: Extract contract.
        :return: TransformContract: Transform contract.

        :raises TransformException: if the transform fails.
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
        """Transform the raw information of property funds.

        :param extract_contract: ExtractContract: Extract contract.
        :return: TransformContract: Transform contract.

        :raises TransformException: if the transform fails.
        """

        try:
            transform_information = self.__make_transformation_property_funds(
                extract_contract.raw_information)
            transform_contract = TransformContract(
                transformed_information=transform_information)

            return transform_contract
        except Exception as exception:
            raise TransformException(exception) from exception
