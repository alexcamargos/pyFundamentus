#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extractor_html_information.py
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

from datetime import datetime as dt

from fundamentus.contracts.extract_contract import ExtractContract
from fundamentus.drivers.interfaces.html_collector import \
    HtmlCollectorInterface
from fundamentus.drivers.interfaces.http_requester import \
    HttpRequesterInterface
from fundamentus.exceptions.extract_exception import ExtractException


#pylint: disable=too-few-public-methods
class ExtractorHtmlInformation:

    def __init__(self,
                 requester: HttpRequesterInterface,
                 collector: HtmlCollectorInterface):
        self.__requester = requester
        self.__collector = collector

    def extract(self) -> ExtractContract:
        try:
            html_information = self.__requester.make_request()
            collect_information = self.__collector.collect_information(html_information['content'])

            return ExtractContract(raw_information=collect_information,
                                   extraction_date=dt.today().toordinal())
        except Exception as exception:
            raise ExtractException(exception) from exception
