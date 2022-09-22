#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: transform_raw_information.py
#  Version: 0.0.10
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
    """Represents a raw information transformer."""

    @staticmethod
    def __remove_new_lines(string: str) -> str:
        """Remove all newline from the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace('\n', '')

    @staticmethod
    def __remove_all_spaces(string: str) -> str:
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

    @staticmethod
    def __remove_dot(string: str) -> str:
        """Remove the dot from the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace('.', '')

    @staticmethod
    def __change_comma_to_dot(string: str) -> str:
        """Change the comma to dot in the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace(',', '.')

    @staticmethod
    def __to_decimal(value: str) -> Decimal:
        """Construct a new Decimal object based from value.

        :param value: value to be processed.
        :return: Decimal object.
        """

        if value.endswith('%'):
            value = value[:-1]

            return Decimal(value) / 100

        return Decimal(value) if value is not None else None

    @staticmethod
    def __remove_currency_symbol(number: str) -> str:
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
        """Make the transformation.

        :param detailed_information: raw information to be processed.
        :return: processed information.
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
        """Make the transformation.

        :param oscillations_information: raw information to be processed.
        :return: processed information.
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
        """Make the transformation.

        :param valuation_indicators: raw information to be processed.
        :return: processed information.
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
        """Make the transformation.

        :param profitability_indicators: raw information to be processed.
        :return: processed information.
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
        """Make the transformation.

        :param indebtedness_indicators: raw information to be processed.
        :return: processed information.
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

    def __transformation_of_balance_sheet(self, balance_sheet: Dict) -> Dict:
        """Make the transformation.

        :param balance_sheet: raw information to be processed.
        :return: processed information.
        """

        total_assets = InformationItem(
            title=self.__string_processing(balance_sheet['total_assets'][0]),
            tooltip=self.__string_processing(balance_sheet['total_assets'][1]),
            value=self.__number_processing(balance_sheet['total_assets'][2]))

        current_assets = InformationItem(
            title=self.__string_processing(balance_sheet['current_assets'][0]),
            tooltip=self.__string_processing(
                balance_sheet['current_assets'][1]),
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
        """Make the transformation.

        :param income_statement: raw information to be processed.
        :return: processed information.
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
        """Make the transformation.

        :param raw_information: Dict: Raw information.
        :return: Dict: Transformed information.
        """

        # Processando informações do preço da ação.
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

        # Processando informações dos indicadores de rentabilidade da ação.
        profitability_indicators = self.__transformation_of_profitability_indicators(
            raw_information['profitability_indicators'])

        # Processando informações dos indicadores de endividamento da ação.
        indebtedness_indicators = self.__transformation_of_indebtedness_indicators(
            raw_information['indebtedness_indicators'])

        # Processando informações dos indicadores de balanço patrimonial da ação.
        balance_sheet = self.__transformation_of_balance_sheet(
            raw_information['balance_sheet'])

        # Processando informações dos demostrativos de resultados da ação.
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

    def __make_transformation_companies(self, raw_information: str) -> List[Dict[str, str]]:
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
                                             raw_information: str) -> List[Dict[str, str]]:
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

    def transform_all_information(
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
