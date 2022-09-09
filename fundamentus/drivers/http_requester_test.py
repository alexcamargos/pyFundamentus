#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: http_requester_test.py
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

"""HTTP Requester Test."""

import pytest
from requests.exceptions import RequestException

from .http_requester import HttpRequester
from .mocks.http_requester import REQUESTER_MOCK


# Disable requests_cache for tests.
@pytest.fixture(scope='function')
def test_make_request(requests_mock) -> None:
    """Test make_request method.

    :param requests_mock.Mocker requests_mock: Mock requests.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'papel': 'MGLU3'}

    requests_mock.get(url=url,
                      status_code=REQUESTER_MOCK['status_code'],
                      text=REQUESTER_MOCK['content'])

    requester = HttpRequester(url=url, params=payload)
    fundamentus_response = requester.make_request()

    assert fundamentus_response.request.method == 'GET'
    assert fundamentus_response.request.url == url
    assert fundamentus_response.request.params == payload
    assert fundamentus_response.status_code == REQUESTER_MOCK['status_code']
    assert fundamentus_response.response.text == REQUESTER_MOCK['content']


def test_make_request_error(requests_mock) -> None:
    """Test make_request method with error.

    :param requests_mock.Mocker requests_mock: Mock requests.
    """

    url = 'http://invalid_url.com'
    payload = {'papel': 'MGLU3'}

    requests_mock.get(url=url,
                      status_code=404,
                      json={'detail': 'something went wrong.'})
    try:
        requester = HttpRequester(url=url, params=payload)
        requester.make_request()
    except RequestException as error:
        assert error is not None
