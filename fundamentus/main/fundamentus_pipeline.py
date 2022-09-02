#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: fundamentus_pipeline.py
#  Version: 0.0.1
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

from fundamentus.drivers.html_collector import HtmlCollector
from fundamentus.drivers.http_requester import HttpRequester
from fundamentus.stages.extraction.extractor_html_information import \
    ExtractorHtmlInformation as Extractor
from fundamentus.stages.transformation.transform_raw_information import \
    TransformRawInformation as Transformer


#pylint: disable=too-few-public-methods
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

    def get_stock_information(self) -> dict:
        """Get the stock information.

        :return: dict: Stock information.
        """

        extract_contract = self.__extractor.extract()

        return self.__transformer.transform(extract_contract)
