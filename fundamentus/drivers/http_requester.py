#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: http_requester.py
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
"""HTTP Requester - This module is responsible for making HTTP requests."""

import requests
import requests_cache

from fundamentus.contracts.request_contract import RequestContract
from fundamentus.utilities.random_user_agent import get_random_user_agent
from .interfaces.http_requester import HttpRequesterInterface


# pylint: disable=too-few-public-methods
class HttpRequester(HttpRequesterInterface):
    """Represents a complete HTTP request."""

    def __init__(self, url: str, params: dict) -> None:
        """Initialize the class.

        :param url: str: URL to make the request.
        :param params: dict: Parameters to make the request.
        """

        self.__url = url
        self.__params = params
        self.__headers = {"User-Agent": get_random_user_agent()}
        self.__fundamentus_request = RequestContract

    @staticmethod
    def __send_http_request(prepared_request: requests.PreparedRequest) -> requests.Response:
        """Send the HTTP request.

        :param prepared_request: requests.PreparedRequest: Prepared request.
        :return: requests.Response: Response of the request.
        :raises HTTPError: If the request fails.
        """

        # Cache is expired after 12 hours (43200 seconds).
        requests_cache.install_cache(cache_name='fundamentus_cache',
                                     backend='sqlite',
                                     expire_after=43200)

        with requests.Session() as session:
            response = session.send(prepared_request)

            response.raise_for_status()

            return response

    def make_request(self) -> RequestContract:
        """Make request to the url and return the response.

        :return: dict: Response of the request.
        :raises RequestException: If the request fails.
        """

        try:
            request = requests.Request(method="GET",
                                       url=self.__url,
                                       params=self.__params,
                                       headers=self.__headers)

            prepared_request = request.prepare()
            response = self.__send_http_request(prepared_request)

            return self.__fundamentus_request(status_code=response.status_code,
                                              request=request,
                                              response=response)
        except requests.exceptions.RequestException as error:
            raise error
