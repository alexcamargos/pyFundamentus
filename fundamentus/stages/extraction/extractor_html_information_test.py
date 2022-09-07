#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extractor_html_information_test.py
#  Version: 0.0.2
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

"""Test of extractor HTML Information."""

from fundamentus.contracts.extract_contract import ExtractContract
from fundamentus.drivers.html_collector import HtmlCollector
from fundamentus.drivers.http_requester import HttpRequester
from fundamentus.drivers.mocks.html_collector import HTML_COLLECTOR_MOCK
from fundamentus.stages.extraction.extractor_html_information import \
    ExtractorHtmlInformation


def test_extract_html_information(requests_mock) -> None:
    """Test extractor html information.

    :param requests_mock (Mock): Mock requests.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'papel': 'MGLU3'}

    requests_mock.get(url=url,
                      status_code=HTML_COLLECTOR_MOCK['status_code'],
                      text=HTML_COLLECTOR_MOCK['content'])

    requester = HttpRequester(url=url, params=payload)
    collector = HtmlCollector()

    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    response = extractor.extract()

    assert isinstance(response, ExtractContract)
    assert isinstance(response.extraction_date, int)
    assert isinstance(response.raw_information, dict)
