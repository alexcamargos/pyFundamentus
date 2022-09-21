#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: http_requester.py
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

"""HTTP Requester Interface."""

from abc import ABC, abstractmethod
from typing import Dict


# pylint: disable=too-few-public-methods
class HttpRequesterInterface(ABC):
    """Represents a complete HTTP request."""

    @abstractmethod
    def make_request(self) -> Dict:
        """Make request to the url and return the response."""

        raise NotImplementedError("You should implement this method.")
