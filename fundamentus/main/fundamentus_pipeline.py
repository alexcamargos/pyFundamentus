#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: fundamentus_pipeline.py
#  Version: 0.0.4
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

"""Python Fundamentus is a Python API that allows you to quickly access the main
fundamental indicators of the main stocks in the Brazilian market.
"""
from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.drivers.html_collector import HtmlCollector
from fundamentus.drivers.http_requester import HttpRequester
from fundamentus.stages.extraction.extractor_html_information import \
    ExtractorHtmlInformation as Extractor
from fundamentus.stages.transformation.transform_raw_information import \
    TransformRawInformation as Transformer


class FundamentusPipeline:

    def __init__(self, url: str, params: dict) -> None:
        """Initialize the class.

        :param url: str: URL to make the request.
        :param params: dict: Parameters to make the request.
        """

        self.__extractor = Extractor(requester=HttpRequester(url=url,
                                                             params=params),
                                     collector=HtmlCollector())
        self.__transformer = Transformer()

    def get_all_information(self) -> TransformContract:
        """Get the stock information.

        :return: dict: Stock information.
        """

        extract_contract = self.__extractor.extract_all_information()

        return self.__transformer.transform_all_information(extract_contract)

    def list_all_companies(self) -> TransformContract:
        """Get the list of all companies.

        :return: list: List of all companies.
        """

        extract_contract = self.__extractor.extract_companies()

        return self.__transformer.transform_companies(extract_contract)

    def list_all_property_funds(self) -> TransformContract:
        """Get the list of all companies.

        :return: list: List of all companies.
        """

        extract_contract = self.__extractor.extract_property_funds()

        return self.__transformer.transform_property_funds(extract_contract)
