#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: http_requester_test.py
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

from .http_requester import HttpRequester
from .mocks.http_requester import REQUESTER_MOCK


def test_make_request(requests_mock):
    """Test make_request method."""

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'papel': 'MGLU3'}

    requests_mock.get(url=url,
                      status_code=REQUESTER_MOCK['status_code'],
                      text=REQUESTER_MOCK['content'])

    requester = HttpRequester(url=url, params=payload)
    response = requester.make_request()

    assert response['status_code'] == REQUESTER_MOCK['status_code']
    assert response['content'] == REQUESTER_MOCK['content']

    assert response['content'].startswith('<!DOCTYPE html>')
    assert response['content'].endswith('</html>\n')
