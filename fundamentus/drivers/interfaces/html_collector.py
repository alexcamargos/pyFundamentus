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

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class HtmlCollectorInterface(ABC):

    @abstractmethod
    def collect_information(self, html: str):
        """Collect information from the html."""

        raise NotImplementedError("You should implement this method.")
