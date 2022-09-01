#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: http_requester.py
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

"""HTTP Requester - This module is responsible for making HTTP requests."""

import requests

from .interfaces.http_requester import HttpRequesterInterface
from .random_user_agent import get_random_user_agent


# pylint: disable=too-few-public-methods
class HttpRequester(HttpRequesterInterface):
    """Represents a complete HTTP request."""

    def __init__(self, url: str, params: dict) -> None:
        """Initialize the class.

        :param url: str: URL to make the request.
        :param params: dict: Parameters to make the request.
        """

        self.url = url
        self.params = params
        self.__url = url
        self.__params = params
        self.__headers = {"User-Agent": get_random_user_agent()}

    def make_request(self) -> dict:
        """Make request to the url and return the response.

        :return: dict: Response of the request.
        :raises HTTPError: If the request fails.
        """

        try:
            response = requests.get(self.__url,
                                    params=self.__params,
                                    headers=self.__headers,
                                    timeout=10) # 10 seconds
            response.raise_for_status()

            return {
                'status_code': response.status_code,
                'content': response.text
            }
        except requests.exceptions.HTTPError as error:
            print(error)
            return None
