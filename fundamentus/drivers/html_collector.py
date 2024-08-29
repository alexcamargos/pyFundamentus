#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: http_requester.py
#  Version: 0.1.1
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
"""HTTP Collector.

This module is responsible for collecting the HTML information from the response.

"""

from typing import Dict, List

from bs4 import BeautifulSoup as bs

from .interfaces.html_collector import HtmlCollectorInterface


# pylint: disable=too-many-locals
class HtmlCollector(HtmlCollectorInterface):
    """Represents a HTML collector."""

    @staticmethod
    def __processing_data_title(soup: bs) -> str:
        """Process data title information.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        return soup.find('span', {'class': 'data-title'}).text

    @staticmethod
    def __processing_data_tooltip(soup: bs) -> str:
        """Process data tooltip information.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        tooltip = soup.find('span', {'class': 'data-tooltip'})['title']

        if tooltip == '':
            tooltip = soup.find(
                'span', {'class': 'data-tooltip'})['data-original-title']

        return tooltip

    @staticmethod
    def __processing_data_value(soup: bs) -> str:
        """Process data value information.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        return soup.find('span', {'class': 'data-value'}).text

    def __extraction_stock_identification(self, soup: bs) -> str:
        """Extract the name of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        # Extract the symbol of the stock.
        ticket_symbol = soup.find('h1', {'class': 'acao-papel'}).text
        # Extract the name of the company.
        company_name = soup.find('span', {'class': 'acao-nome'}).text

        return {
            'symbol': [ticket_symbol],
            'name': [company_name]
        }

    def __extraction_financial_summary(self, soup: bs) -> Dict:
        """Extract the financial summary of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        frame_financial_summary = soup.find('div', {'class': 'frame'})
        information = frame_financial_summary.find_all('div', {'class': 'data'})

        # Extract the market value of the stock.
        market_valuation_title = self.__processing_data_title(information[0])
        market_valuation_tooltip = self.__processing_data_tooltip(information[0])
        market_valuation_value = self.__processing_data_value(information[0])

        # Extract the enterprise valuation of the stock.
        enterprise_valuation_title = self.__processing_data_title(information[1])
        enterprise_valuation_tooltip = self.__processing_data_tooltip(information[1])
        enterprise_valuation_value = self.__processing_data_value(information[1])

        # Extract the number of shares of the stock.
        number_of_shares_title = self.__processing_data_title(information[2])
        number_of_shares_tooltip = self.__processing_data_tooltip(information[2])
        number_of_shares_value = self.__processing_data_value(information[2])

        # Extract the last financial statement of the stock.
        last_financial_statement_title = self.__processing_data_title(information[3])
        last_financial_statement_tooltip = self.__processing_data_tooltip(information[3])
        last_financial_statement_value = self.__processing_data_value(information[3])

        # Extract the sector of the stock.
        sector_title = self.__processing_data_title(information[4])
        sector_tooltip = self.__processing_data_tooltip(information[4])
        sector_value = self.__processing_data_value(information[4])

        # Extract the subsector of the stock.
        subsector_title = self.__processing_data_title(information[5])
        subsector_tooltip = self.__processing_data_tooltip(information[5])
        subsector_value = self.__processing_data_value(information[5])

        return {
            'market_valuation': [market_valuation_title,
                                 market_valuation_tooltip,
                                 market_valuation_value],
            'enterprise_valuation': [enterprise_valuation_title,
                                     enterprise_valuation_tooltip,
                                     enterprise_valuation_value],
            'number_of_shares': [number_of_shares_title,
                                 number_of_shares_tooltip,
                                 number_of_shares_value],
            'last_financial_statement': [last_financial_statement_title,
                                         last_financial_statement_tooltip,
                                         last_financial_statement_value],
            'sector': [sector_title,
                       sector_tooltip,
                       sector_value],
            'subsector': [subsector_title,
                          subsector_tooltip,
                          subsector_value],
        }

    def __extraction_price(self, soup: bs) -> Dict:
        """Extract the price of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (dict): Dictionary with the processed information.
        """

        frame_cotacao = soup.find('div', {'class': 'frame-cotacao'})
        information = frame_cotacao.find_all('div', {'class': 'data'})

        # Extract the price of the stock.
        price_title = self.__processing_data_title(information[0])
        price_tooltip = self.__processing_data_tooltip(information[0])
        price_value = self.__processing_data_value(information[0])

        # Extract the date of the last trading session
        date_title = self.__processing_data_title(information[1])
        date_tooltip = self.__processing_data_tooltip(information[1])
        date_value = self.__processing_data_value(information[1])

        return {
            'price': [price_title, price_tooltip, price_value],
            'date': [date_title, date_tooltip, date_value]
        }

    def __processing_stock_type(self, soup: bs) -> List[str]:
        """Process stock type information.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        title = self.__processing_data_title(soup)
        tooltip = self.__processing_data_tooltip(soup)
        value = self.__processing_data_value(soup)

        return [title, tooltip, value]

    def __processing_traded_volume_per_day(self, soup: bs) -> List[str]:
        """Process traded volume per day information.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        title = self.__processing_data_title(soup)
        tooltip = self.__processing_data_tooltip(soup)
        value = self.__processing_data_value(soup)

        return [title, tooltip, value]

    def __processing_equity_value_per_share(self, soup: bs) -> List[str]:
        """Process Equity Value per Share information.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        title = self.__processing_data_title(soup)
        tooltip = self.__processing_data_tooltip(soup)
        value = self.__processing_data_value(soup)

        return [title, tooltip, value]

    def __processing_earnings_per_share(self, soup: bs) -> List[str]:
        """Process Earnings per Share information.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        title = self.__processing_data_title(soup)
        tooltip = self.__processing_data_tooltip(soup)
        value = self.__processing_data_value(soup)

        return [title, tooltip, value]

    def __processing_variation_52_weeks(self, soup: bs) -> Dict[str, List[str]]:
        """Process variation 52 weeks information.

        :param soup (bs): BeautifulSoup object.
        :return (str): String with the processed information.
        """

        information = soup.find_all('div', {'class': 'data'})

        # Extract the lowest value at 52 weeks.
        lowest_value_tooltip = self.__processing_data_tooltip(information[0])
        lowest_value_value = self.__processing_data_value(information[0])

        # Extract the highest value at 52 weeks.
        highest_value_tooltip = self.__processing_data_tooltip(information[1])
        highest_value_value = self.__processing_data_value(information[1])

        return {
            'lowest_value': [lowest_value_tooltip, lowest_value_value],
            'highest_value': [highest_value_tooltip, highest_value_value]
        }

    def __extraction_detailed_information(self, soup: bs) -> Dict:
        """Extract the detailed information of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (dict): Dictionary with the processed information.
        """

        detailed_information = soup.find(
            'div', {'class': 'col col-xl-auto vpalpa2-estilo'})
        information = detailed_information.find_all('div', {'class': 'data'})

        # Extract the stock type.
        stock_type = self.__processing_stock_type(information[0])

        # Extract the traded volume per day.
        traded_volume_per_day = self.__processing_traded_volume_per_day(
            information[1])

        # Extract the equity value per share.
        equity_value_per_share = self.__processing_equity_value_per_share(
            information[2])

        # Extract the earnings per share.
        earnings_per_share = self.__processing_earnings_per_share(
            information[3])

        # Extract the variation 52 weeks.
        variation_52_weeks = self.__processing_variation_52_weeks(
            information[4])

        return {
            'stock_type': stock_type,
            'traded_volume_per_day': traded_volume_per_day,
            'equity_value_per_share': equity_value_per_share,
            'earnings_per_share': earnings_per_share,
            'variation_52_weeks': variation_52_weeks
        }

    def __extraction_oscillations(self, soup: bs) -> Dict:
        """Extract the oscillations of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (dict): Dictionary with the processed information.
        """

        oscillations = soup.find('div', {'class': 'oscilacoes'})
        information = oscillations.find_all('div', {'class': 'data'})

        # Extract the variation of the day.
        variation_day_value = self.__processing_data_value(information[0])
        variation_day_title = information[0].find(
            'span', {'class': 'data-text'}).text

        # Extract the variation of the month.
        variation_month_value = self.__processing_data_value(information[1])
        variation_month_title = information[1].find(
            'span', {'class': 'data-text'}).text

        # Extract the variation of the 30 days.
        variation_30_days_value = self.__processing_data_value(information[2])
        variation_30_days_title = information[2].find(
            'span', {'class': 'data-text'}).text

        # Extract the variation of the 12 months.
        variation_12_months_value = self.__processing_data_value(
            information[3])
        variation_12_months_title = information[3].find(
            'span', {'class': 'data-text'}).text

        # Extract the variation on 2022.
        variation_2022_value = self.__processing_data_value(information[4])
        variation_2022_title = information[4].find(
            'span', {'class': 'data-text'}).text

        # Extract the variation on 2021.
        variation_2021_value = self.__processing_data_value(information[5])
        variation_2021_title = information[5].find(
            'span', {'class': 'data-text'}).text

        # Extract the variation on 2020.
        variation_2020_value = self.__processing_data_value(information[6])
        variation_2020_title = information[6].find(
            'span', {'class': 'data-text'}).text

        # Extract the variation on 2019.
        variation_2019_value = self.__processing_data_value(information[7])
        variation_2019_title = information[7].find(
            'span', {'class': 'data-text'}).text

        # Extract the variation on 2018.
        variation_2018_value = self.__processing_data_value(information[8])
        variation_2018_title = information[8].find(
            'span', {'class': 'data-text'}).text

        # Extract the variation on 2017.
        variation_2017_value = self.__processing_data_value(information[9])
        variation_2017_title = information[9].find(
            'span', {'class': 'data-text'}).text

        return {
            'variation_day': [variation_day_title, variation_day_value],
            'variation_month': [variation_month_title, variation_month_value],
            'variation_30_days': [variation_30_days_title, variation_30_days_value],
            'variation_12_months': [variation_12_months_title, variation_12_months_value],
            'variation_2022': [variation_2022_title, variation_2022_value],
            'variation_2021': [variation_2021_title, variation_2021_value],
            'variation_2020': [variation_2020_title, variation_2020_value],
            'variation_2019': [variation_2019_title, variation_2019_value],
            'variation_2018': [variation_2018_title, variation_2018_value],
            'variation_2017': [variation_2017_title, variation_2017_value]
        }

    def __extraction_valuation_indicators(self, soup: bs) -> Dict:
        """Extract the valuation indicators of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (dict): Dictionary with the processed information.
        """

        valuation_indicators = soup.find_all('div', {'class': 'frame'})[4]
        information = valuation_indicators.find_all(
            'div', {'class': 'col-6 col-sm-4 col-md-2'})

        # Preço da ação dividido pelo lucro por ação.
        price_divided_by_profit_title = self.__processing_data_title(
            information[0])
        price_divided_by_profit_tooltip = self.__processing_data_tooltip(
            information[0])
        price_divided_by_profit_value = self.__processing_data_value(
            information[0])

        # Preço da ação dividido pelo Valor Patrimonial por ação.
        price_divided_by_asset_value_title = self.__processing_data_title(
            information[1])
        price_divided_by_asset_value_tooltip = self.__processing_data_tooltip(
            information[1])
        price_divided_by_asset_value_value = self.__processing_data_value(
            information[1])

        # Preço da ação dividido pelo EBIT por ação.
        price_divided_by_ebit_title = self.__processing_data_title(
            information[2])
        price_divided_by_ebit_tooltip = self.__processing_data_tooltip(
            information[2])
        price_divided_by_ebit_value = self.__processing_data_value(
            information[2])

        # Preço da ação dividido pela Receita Líquida por ação.
        price_divided_by_net_revenue_title = self.__processing_data_title(
            information[3])
        price_divided_by_net_revenue_tooltip = self.__processing_data_tooltip(
            information[3])
        price_divided_by_net_revenue_value = self.__processing_data_value(
            information[3])

        # Preço da ação dividido pelos Ativos totais por ação.
        price_divided_by_total_assets_title = self.__processing_data_title(
            information[4])
        price_divided_by_total_assets_tooltip = self.__processing_data_tooltip(
            information[4])
        price_divided_by_total_assets_value = self.__processing_data_value(
            information[4])

        # Preço da ação dividido pelos Ativos Circulantes Líquidos por ação.
        price_divided_by_net_current_assets_title = self.__processing_data_title(
            information[5])
        price_divided_by_net_current_assets_tooltip = self.__processing_data_tooltip(
            information[5])
        price_divided_by_net_current_assets_value = self.__processing_data_value(
            information[5])

        # Dividendo pago por ação dividido pelo preço da ação.
        dividend_yield_title = self.__processing_data_title(information[6])
        dividend_yield_tooltip = self.__processing_data_tooltip(
            information[6])
        dividend_yield_value = self.__processing_data_value(information[6])

        # Valor da Firma (Enterprise Value dividido pelo EBITDA).

        enterprise_value_by_ebitda_title = self.__processing_data_title(
            information[7])
        enterprise_value_by_ebitda_tooltip = self.__processing_data_tooltip(
            information[7])
        enterprise_value_by_ebitda_value = self.__processing_data_value(
            information[7])

        # Valor da Firma (Enterprise Value dividido pelo EBIT).
        enterprise_value_by_ebit_title = self.__processing_data_title(
            information[8])
        enterprise_value_by_ebit_tooltip = self.__processing_data_tooltip(
            information[8])
        enterprise_value_by_ebit_value = self.__processing_data_value(
            information[8])

        # Preço da ação dividido pelo capital de giro por ação.
        price_by_working_capital_title = self.__processing_data_title(
            information[9])
        price_by_working_capital_tooltip = self.__processing_data_tooltip(
            information[9])
        price_by_working_capital_value = self.__processing_data_value(
            information[9])

        return {
            'price_divided_by_profit_title': [
                price_divided_by_profit_title, price_divided_by_profit_tooltip,
                price_divided_by_profit_value
            ],
            'price_divided_by_asset_value': [
                price_divided_by_asset_value_title,
                price_divided_by_asset_value_tooltip,
                price_divided_by_asset_value_value
            ],
            'price_divided_by_ebit': [
                price_divided_by_ebit_title, price_divided_by_ebit_tooltip,
                price_divided_by_ebit_value
            ],
            'price_divided_by_net_revenue': [
                price_divided_by_net_revenue_title,
                price_divided_by_net_revenue_tooltip,
                price_divided_by_net_revenue_value
            ],
            'price_divided_by_total_assets': [
                price_divided_by_total_assets_title,
                price_divided_by_total_assets_tooltip,
                price_divided_by_total_assets_value
            ],
            'price_divided_by_net_current_assets': [
                price_divided_by_net_current_assets_title,
                price_divided_by_net_current_assets_tooltip,
                price_divided_by_net_current_assets_value
            ],
            'dividend_yield': [
                dividend_yield_title, dividend_yield_tooltip,
                dividend_yield_value
            ],
            'enterprise_value_by_ebitda': [
                enterprise_value_by_ebitda_title,
                enterprise_value_by_ebitda_tooltip,
                enterprise_value_by_ebitda_value
            ],
            'enterprise_value_by_ebit': [
                enterprise_value_by_ebit_title,
                enterprise_value_by_ebit_tooltip,
                enterprise_value_by_ebit_value
            ],
            'price_by_working_capital': [
                price_by_working_capital_title,
                price_by_working_capital_tooltip,
                price_by_working_capital_value
            ]
        }

    def __extraction_profitability_indicators(self, soup) -> Dict:
        """Extract the profitability indicators of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (dict): Dictionary with the processed information.
        """

        profitability_indicators = soup.find_all('div', {'class': 'frame'})[5]
        information = profitability_indicators.find_all(
            'div', {'class': 'col-6 col-sm-4 col-md-2'})

        # Retorno sobre o Patrimônio Líquido (ROE).
        return_on_equity_title = self.__processing_data_title(information[0])
        return_on_equity_tooltip = self.__processing_data_tooltip(
            information[0])
        return_on_equity_value = self.__processing_data_value(information[0])

        # Retorno sobre o Capital Investido (ROIC).
        return_on_invested_capital_title = self.__processing_data_title(
            information[1])
        return_on_invested_capital_tooltip = self.__processing_data_tooltip(
            information[1])
        return_on_invested_capital_value = self.__processing_data_value(
            information[1])

        # EBIT dividido por Ativos totais.
        ebit_divided_by_total_assets_title = self.__processing_data_title(
            information[2])
        ebit_divided_by_total_assets_tooltip = self.__processing_data_tooltip(
            information[2])
        ebit_divided_by_total_assets_value = self.__processing_data_value(
            information[2])

        # Crescimento da Receita Líquida nos últimos 5 anos.
        net_revenue_growth_last_5_years_title = self.__processing_data_title(
            information[3])
        net_revenue_growth_last_5_years_tooltip = self.__processing_data_tooltip(
            information[3])
        net_revenue_growth_last_5_years_value = self.__processing_data_value(
            information[3])

        # Receita Líquida dividido por Ativos Totais.
        net_revenue_divided_by_total_assets_title = self.__processing_data_title(
            information[4])
        net_revenue_divided_by_total_assets_tooltip = self.__processing_data_tooltip(
            information[4])
        net_revenue_divided_by_total_assets_value = self.__processing_data_value(
            information[4])

        # Lucro Bruto dividido pela Receita Líquida.
        gross_profit_divided_by_net_revenue_title = self.__processing_data_title(
            information[5])
        gross_profit_divided_by_net_revenue_tooltip = self.__processing_data_tooltip(
            information[5])
        gross_profit_divided_by_net_revenue_value = self.__processing_data_value(
            information[5])

        # EBIT dividido pela Receita Líquida.
        ebit_divided_by_net_revenue_title = self.__processing_data_title(
            information[6])
        ebit_divided_by_net_revenue_tooltip = self.__processing_data_tooltip(
            information[6])
        ebit_divided_by_net_revenue_value = self.__processing_data_value(
            information[6])

        # Lucro Líquido dividido pela Receita Líquida.
        net_income_divided_by_net_revenue_title = self.__processing_data_title(
            information[7])
        net_income_divided_by_net_revenue_tooltip = self.__processing_data_tooltip(
            information[7])
        net_income_divided_by_net_revenue_value = self.__processing_data_value(
            information[7])

        return {
            'return_on_equity': [
                return_on_equity_title, return_on_equity_tooltip,
                return_on_equity_value
            ],
            'return_on_invested_capital': [
                return_on_invested_capital_title,
                return_on_invested_capital_tooltip,
                return_on_invested_capital_value
            ],
            'ebit_divided_by_total_assets': [
                ebit_divided_by_total_assets_title,
                ebit_divided_by_total_assets_tooltip,
                ebit_divided_by_total_assets_value
            ],
            'net_revenue_growth_last_5_years': [
                net_revenue_growth_last_5_years_title,
                net_revenue_growth_last_5_years_tooltip,
                net_revenue_growth_last_5_years_value
            ],
            'net_revenue_divided_by_total_assets': [
                net_revenue_divided_by_total_assets_title,
                net_revenue_divided_by_total_assets_tooltip,
                net_revenue_divided_by_total_assets_value
            ],
            'gross_profit_divided_by_net_revenue': [
                gross_profit_divided_by_net_revenue_title,
                gross_profit_divided_by_net_revenue_tooltip,
                gross_profit_divided_by_net_revenue_value
            ],
            'ebit_divided_by_net_revenue': [
                ebit_divided_by_net_revenue_title,
                ebit_divided_by_net_revenue_tooltip,
                ebit_divided_by_net_revenue_value
            ],
            'net_income_divided_by_net_revenue': [
                net_income_divided_by_net_revenue_title,
                net_income_divided_by_net_revenue_tooltip,
                net_income_divided_by_net_revenue_value
            ]
        }

    def __extraction_indebtedness_indicators(self, soup) -> Dict:
        """Extract the indebtedness indicators of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (dict): Dictionary with the processed information.
        """

        indebtedness_indicators = soup.find_all('div', {'class': 'frame'})[6]
        information = indebtedness_indicators.find_all(
            'div', {'class': 'col-6 col-sm-4 col-md-2'})

        # Ativo Circulante dividido pelo Passivo Circulante.
        current_liquidity_title = self.__processing_data_title(information[0])
        current_liquidity_tooltip = self.__processing_data_tooltip(
            information[0])
        current_liquidity_value = self.__processing_data_value(information[0])

        # Dívida Bruta total (Dívida + Debêntures) dividido pelo Patrimônio Líquido.
        gross_debt_by_equity_title = self.__processing_data_title(
            information[1])
        gross_debt_by_equity_tooltip = self.__processing_data_tooltip(
            information[1])
        gross_debt_by_equity_value = self.__processing_data_value(
            information[1])

        # Dívida Bruta total (Dívida + Debêntures) menos caixa dividido pelo Patrimônio Líquido.
        net_debt_by_equity_title = self.__processing_data_title(information[2])
        net_debt_by_equity_tooltip = self.__processing_data_tooltip(
            information[2])
        net_debt_by_equity_value = self.__processing_data_value(information[2])

        # Dívida Bruta total (Dívida + Debêntures) menos caixa dividido pelo EBITDA.
        net_debt_by_ebitda_title = self.__processing_data_title(information[3])
        net_debt_by_ebitda_tooltip = self.__processing_data_tooltip(
            information[3])
        net_debt_by_ebitda_value = self.__processing_data_value(information[3])

        # Patrimônio Líquido sobre Ativos totais.
        equity_by_total_assets_title = self.__processing_data_title(
            information[4])
        equity_by_total_assets_tooltip = self.__processing_data_tooltip(
            information[4])
        equity_by_total_assets_value = self.__processing_data_value(
            information[4])

        return {
            'current_liquidity': [
                current_liquidity_title, current_liquidity_tooltip,
                current_liquidity_value
            ],
            'gross_debt_by_equity': [
                gross_debt_by_equity_title, gross_debt_by_equity_tooltip,
                gross_debt_by_equity_value
            ],
            'net_debt_by_equity': [
                net_debt_by_equity_title, net_debt_by_equity_tooltip,
                net_debt_by_equity_value
            ],
            'net_debt_by_ebitda': [
                net_debt_by_ebitda_title, net_debt_by_ebitda_tooltip,
                net_debt_by_ebitda_value
            ],
            'equity_by_total_assets': [
                equity_by_total_assets_title, equity_by_total_assets_tooltip,
                equity_by_total_assets_value
            ]
        }

    def __extraction_balance_sheet(self, soup) -> Dict:
        """Extract the balance_sheet of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (dict): Dictionary with the processed information.
        """

        balance_sheet = soup.find_all('div', {'class': 'frame'})[7]
        information = balance_sheet.find_all('div', {'class': 'col-sm'})
        column_left = information[0].find_all('div', {'class': 'data'})
        column_right = information[1].find_all('div', {'class': 'data'})

        # Todos os bens, direitos e valores a receber de uma entidade.
        total_assets_title = self.__processing_data_title(column_left[0])
        total_assets_tooltip = self.__processing_data_tooltip(column_left[0])
        total_assets_value = self.__processing_data_value(column_left[0])

        if len(column_left) != 3:
            # Carteira de crédito.
            credit_portfolio_title = self.__processing_data_title(
                column_left[1])
            credit_portfolio_tooltip = self.__processing_data_tooltip(
                column_left[1])
            credit_portfolio_value = self.__processing_data_value(
                column_left[1])
        else:
            # Bens ou direitos que podem ser convertido em dinheiro em curto prazo.
            current_assets_title = self.__processing_data_title(column_left[1])
            current_assets_tooltip = self.__processing_data_tooltip(
                column_left[1])
            current_assets_value = self.__processing_data_value(column_left[1])

            # Contas que representam bens numerários (Dinheiro).
            cash_title = self.__processing_data_title(column_left[2])
            cash_tooltip = self.__processing_data_tooltip(column_left[2])
            cash_value = self.__processing_data_value(column_left[2])

        if len(column_right) != 3:
            # Operação financeira em que um banco recebe determinada quantia em dinheiro,
            # comprometendo-se a guardá-la e se obrigando a restituí-la quando solicitado
            # pelo depositante ou em data prefixada.
            deposits_title = self.__processing_data_title(column_right[0])
            deposits_tooltip = self.__processing_data_tooltip(column_right[0])
            deposits_value = self.__processing_data_value(column_right[0])

            # Patrimônio Líquido.
            equity_title = self.__processing_data_title(column_right[1])
            equity_tooltip = self.__processing_data_tooltip(column_right[1])
            equity_value = self.__processing_data_value(column_right[1])
        else:
            # Dívida Bruta.
            gross_debt_title = self.__processing_data_title(column_right[0])
            gross_debt_tooltip = self.__processing_data_tooltip(
                column_right[0])
            gross_debt_value = self.__processing_data_value(column_right[0])

            # Dívida Líquida.
            net_debt_title = self.__processing_data_title(column_right[1])
            net_debt_tooltip = self.__processing_data_tooltip(column_right[1])
            net_debt_value = self.__processing_data_value(column_right[1])

            # Patrimônio Líquido.
            equity_title = self.__processing_data_title(column_right[2])
            equity_tooltip = self.__processing_data_tooltip(column_right[2])
            equity_value = self.__processing_data_value(column_right[2])

        if len(column_left) != 3 or len(column_right) != 3:
            return_value = {
                'total_assets': [total_assets_title,
                                 total_assets_tooltip,
                                 total_assets_value],
                'credit_portfolio': [credit_portfolio_title,
                                     credit_portfolio_tooltip,
                                     credit_portfolio_value],
                'deposits': [deposits_title,
                             deposits_tooltip,
                             deposits_value],
                'equity': [equity_title,
                           equity_tooltip,
                           equity_value]
            }
        else:
            return_value = {
                'total_assets': [total_assets_title,
                                 total_assets_tooltip,
                                 total_assets_value],
                'current_assets': [current_assets_title,
                                   current_assets_tooltip,
                                   current_assets_value],
                'cash': [cash_title,
                         cash_tooltip,
                         cash_value],
                'gross_debt': [gross_debt_title,
                               gross_debt_tooltip,
                               gross_debt_value],
                'net_debt': [net_debt_title,
                             net_debt_tooltip,
                             net_debt_value],
                'equity': [equity_title,
                           equity_tooltip,
                           equity_value]
            }

        return return_value

    @staticmethod
    def __extraction_income_statement(soup) -> Dict:
        """Extract the income statement of the stock.

        :param soup (bs): BeautifulSoup object.
        :return (dict): Dictionary with the processed information.
        """

        income_statement = soup.find_all('div', {'class': 'frame'})[8]
        information_contents = income_statement.find_all('span',
                                                         {'class': 'dt-value'})
        information_titles = income_statement.find_all('span',
                                                       {'class': 'dt-title'})
        information_tooltip = income_statement.find_all('span',
                                                        {'class': 'data-tooltip'})

        # Títulos e Tooltips.
        revenue_title = information_titles[0].text
        revenue_tooltip = information_tooltip[0]['title']

        ebit_title = information_titles[1].text
        ebit_tooltip = information_tooltip[1]['title']

        net_income_title = information_titles[2].text
        net_income_tooltip = information_tooltip[2]['title']

        # Receita Líquida nos últimos 12 meses.
        revenue_value = information_contents[0].text
        # EBIT nos últimos 12 meses.
        ebit_value = information_contents[2].text
        # Lucro Líquido nos últimos 12 meses.
        net_income_value = information_contents[4].text

        # Receita Líquida nos últimos 03 meses.
        revenue_3m_value = information_contents[1].text
        # Receita Líquida nos últimos 03 meses.
        ebit_3m_value = information_contents[3].text
        # EBIT nos últimos 03 meses.
        net_income_3m_value = information_contents[5].text

        twelve_months = {
            'revenue': [revenue_title, revenue_tooltip, revenue_value],
            'ebit': [ebit_title, ebit_tooltip, ebit_value],
            'net_income':
            [net_income_title, net_income_tooltip, net_income_value]
        }

        three_months = {
            'revenue': [revenue_title, revenue_tooltip, revenue_3m_value],
            'ebit': [ebit_title, ebit_tooltip, ebit_3m_value],
            'net_income':
            [net_income_title, net_income_tooltip, net_income_3m_value]
        }

        return {'twelve_months': twelve_months, 'three_months': three_months}

    def collect_all_information(self, html: str) -> Dict:
        """Collect information from the html.

        param: html (str): HTML content.

        :return: dict: Dictionary with the collected information.
        """

        soup = bs(html, 'html.parser')

        if soup.find('table',
                     {'class': 'table table-default table-sort table-resultados-trimestrais'}):
            raise ValueError('The HTML content is not from a stock.')

        # Extract the identification of the stock.
        stock_identification = self.__extraction_stock_identification(soup)

        # Extract the financial summary of the stock.
        financial_summary = self.__extraction_financial_summary(soup)

        # Extract the price of the stock.
        price = self.__extraction_price(soup)

        # Extract the detailed information of the stock.
        detailed_information = self.__extraction_detailed_information(soup)

        # Extract the oscillations of the stock.
        oscillations = self.__extraction_oscillations(soup)

        # Extract the stock valuation indicators.
        valuation_indicators = self.__extraction_valuation_indicators(soup)

        # Extract the stock profitability indicators.
        profitability_indicators = self.__extraction_profitability_indicators(
            soup)

        # Extract the stock indebtedness indicators.
        indebtedness_indicators = self.__extraction_indebtedness_indicators(
            soup)

        # Extract the stock balance sheet.
        balance_sheet = self.__extraction_balance_sheet(soup)

        # Extract the stock income statement.
        income_statement = self.__extraction_income_statement(soup)

        return {
            'identification': stock_identification,
            'financial_summary': financial_summary,
            'price': price,
            'detailed_information': detailed_information,
            'oscillations': oscillations,
            'valuation_indicators': valuation_indicators,
            'profitability_indicators': profitability_indicators,
            'indebtedness_indicators': indebtedness_indicators,
            'balance_sheet': balance_sheet,
            'income_statement': income_statement
        }

    def collect_list_of_companies(self, html: str) -> List[Dict]:
        """Collect list of companies from Fundamentus website.

         param: html (str): HTML content.
        :return: list: list of companies collected.
        """

        soup = bs(html, 'html.parser')
        tables = soup.find_all('table', {
            'class':
            'table table-default table-sort table-resultados-trimestrais'
        })
        companies = tables[0].find_all('tr')

        companies_list = []
        for company in companies[1:]:
            company_code, company_name, corporate_name = company.find_all('td')
            company_link = company_code.find('a')['href']

            companies_list.append({
                'code': company_code.text,
                'name': company_name.text,
                'corporate_name': corporate_name.text,
                'link': company_link
            })

        return companies_list

    def collect_list_of_property_funds(self, html: str) -> List[Dict]:
        """Collect list of companies from Fundamentus website.

         param: html (str): HTML content.
        :return: list: list of companies collected.
        """

        soup = bs(html, 'html.parser')
        tables = soup.find_all('table', {
            'class':
            'table table-default table-sort table-resultados-trimestrais'
        })
        funds = tables[1].find_all('tr')

        funds_list = []
        for fund in funds[1:]:
            fund_code, fund_name = fund.find_all('td')
            fund_link = fund_code.find('a')['href']

            funds_list.append({
                'code': fund_code.text,
                'name': fund_name.text,
                'link': fund_link
            })

        return funds_list
