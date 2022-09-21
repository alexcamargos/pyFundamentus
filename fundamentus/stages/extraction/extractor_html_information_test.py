#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extractor_html_information_test.py
#  Version: 0.0.7
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
from fundamentus.drivers.mocks.companies_list import COMPANIES_LIST_MOCK
from fundamentus.drivers.mocks.html_collector import HTML_COLLECTOR_MOCK
from fundamentus.exceptions.extract_exception import ExtractException
from fundamentus.stages.extraction.extractor_html_information import \
    ExtractorHtmlInformation


def test_extract_html_information(requests_mock) -> None:
    """Test extractor html information.

    :param requests_mock (Mock): Mock requests.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'papel': 'MGLU3', 'interface': 'mobile'}

    requests_mock.get(url=url,
                      status_code=HTML_COLLECTOR_MOCK['status_code'],
                      text=HTML_COLLECTOR_MOCK['content'])

    requester = HttpRequester(url=url, params=payload)
    collector = HtmlCollector()
    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    response = extractor.extract_all_information()

    assert isinstance(response, ExtractContract)
    assert isinstance(response.extraction_date, int)
    assert isinstance(response.raw_information, dict)


def test_extract_html_information_exception(requests_mock) -> None:
    """Test extractor html information with exception.

    :param requests_mock (Mock): Mock requests.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'papel': 'MGLU3', 'interface': 'mobile'}

    requests_mock.get(url=url,
                      status_code=HTML_COLLECTOR_MOCK['status_code'],
                      text='Extract Exception')

    requester = HttpRequester(url=url, params=payload)
    collector = HtmlCollector()
    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)

    try:
        response = extractor.extract_all_information()  # pylint: disable=unused-variable
    except ExtractException as exception:
        assert isinstance(exception, ExtractException)


def test_extract_html_information_companies(requests_mock) -> None:
    """Test extractor html information companies."""

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'interface': 'mobile'}

    requests_mock.get(url=url,
                      status_code=COMPANIES_LIST_MOCK['status_code'],
                      text=COMPANIES_LIST_MOCK['content'])

    requester = HttpRequester(url=url, params=payload)
    collector = HtmlCollector()
    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    response = extractor.extract_companies()

    assert isinstance(response, ExtractContract)
    assert isinstance(response.raw_information, list)
    assert isinstance(response.raw_information[0], dict)
    assert isinstance(response.extraction_date, int)

    assert ['code', 'name', 'corporate_name',
            'link'] == list(response.raw_information[0].keys())


def test_extract_html_information_companies_exception(requests_mock) -> None:
    """Test extractor html information companies with exception.

    :param requests_mock (Mock): Mock requests.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'interface': 'classic'}

    requests_mock.get(url=url,
                      status_code=HTML_COLLECTOR_MOCK['status_code'],
                      text='Extract Exception')

    requester = HttpRequester(url=url, params=payload)
    collector = HtmlCollector()
    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)

    try:
        response = extractor.extract_companies()  # pylint: disable=unused-variable
    except ExtractException as exception:
        assert isinstance(exception, ExtractException)


def test_extract_html_information_property_funds(requests_mock) -> None:
    """Test extractor html information companies."""

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'interface': 'mobile'}

    requests_mock.get(url=url,
                      status_code=COMPANIES_LIST_MOCK['status_code'],
                      text=COMPANIES_LIST_MOCK['content'])

    requester = HttpRequester(url=url, params=payload)
    collector = HtmlCollector()
    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    response = extractor.extract_property_funds()

    assert isinstance(response, ExtractContract)
    assert isinstance(response.raw_information, list)
    assert isinstance(response.raw_information[0], dict)
    assert isinstance(response.extraction_date, int)

    assert ['code', 'name', 'link'] == list(response.raw_information[0].keys())


def test_extract_html_information_property_funds_exception(
        requests_mock) -> None:
    """Test extractor html information companies with exception.

    :param requests_mock (Mock): Mock requests.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'interface': 'classic'}

    requests_mock.get(url=url,
                      status_code=HTML_COLLECTOR_MOCK['status_code'],
                      text='Extract Exception')

    requester = HttpRequester(url=url, params=payload)
    collector = HtmlCollector()
    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)

    try:
        response = extractor.extract_property_funds()  # pylint: disable=unused-variable
    except ExtractException as exception:
        assert isinstance(exception, ExtractException)
