#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: fundamentus_pipeline.py
#  Version: 0.0.5
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
Python Fundamentus API

This module provides a programmatic interface to access and analyze key financial and
fundamental indicators of companies listed on the Brazilian stock exchange (Bovespa).
Using this API, investors and analysts can quickly obtain detailed data to assist in
investment decision-making.
"""

from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.drivers.html_collector import HtmlCollector
from fundamentus.drivers.http_requester import HttpRequester
from fundamentus.stages.extraction.extractor_html_information import \
    ExtractorHtmlInformation as Extractor
from fundamentus.stages.transformation.transform_raw_information import \
    TransformRawInformation as Transformer

from fundamentus.utilities.config import URL, INTERFACE


class FundamentusPipeline:
    """
    A pipeline for accessing and processing financial information
    of companies listed on Bovespa.

    This class orchestrates the collection and transformation of
    financial data from the Fundamentus website, providing a simplified
    interface to access fundamental indicators, company lists,
    and real estate investment funds.

    Attributes:
        ticker (str): The ticker symbol of the company.
        url (str): The base URL for the HTTP requests.
        interface (str): The interface for the HTTP requests.

    Methods:
        get_all_information: Returns detailed financial information of companies.
        list_all_companies: Lists all companies with available data.
        list_all_property_funds: Lists all real estate investment funds
                                    with available data.
    """

    def __init__(self, ticker: str = None, url: str = URL, interface: str = INTERFACE) -> None:
        """Initializes the FundamentusPipeline object.

        Args:
            ticker (str): The ticker symbol of the company.
            url (str): The base URL for the HTTP requests.
            interface (str): The interface for the HTTP requests.
        """

        # A HTML information extractor.
        self.__extractor = Extractor(requester=HttpRequester(url=url,
                                                             params={'papel': ticker,
                                                                     'interface': interface}),
                                     collector=HtmlCollector())
        # A raw information transformer.
        self.__transformer = Transformer()

    def get_all_information(self) -> TransformContract:
        """Retrieves detailed financial information of listed companies.

        This method extracts and transforms financial data of companies,
        including indicators such as net profit, net revenue, among others,
        providing a comprehensive view of the companies' financial and economic state.

        Returns:
            TransformContract: A contract containing the transformed financial data.
        """

        extract_contract = self.__extractor.extract_all_information()

        return self.__transformer.transform_all_information(extract_contract)

    def list_all_companies(self) -> TransformContract:
        """Lists all companies with available data.

        Extracts and transforms a list of companies listed on Bovespa,
        facilitating the identification of potential investments.

        Returns:
            TransformContract: A contract containing the transformed list of companies.
        """

        extract_contract = self.__extractor.extract_companies()

        return self.__transformer.transform_companies(extract_contract)

    def list_all_property_funds(self) -> TransformContract:
        """Lists all real estate investment funds with available data.

        Similar to the company listing, this method focuses on real estate
        investment funds, providing relevant information for investors interested
        in this segment.

        Returns:
            TransformContract: A contract containing the transformed list
                               of real estate investment funds.
        """

        extract_contract = self.__extractor.extract_property_funds()

        return self.__transformer.transform_property_funds(extract_contract)
