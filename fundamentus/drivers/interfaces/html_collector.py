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

"""Html Collector Interface."""

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class HtmlCollectorInterface(ABC):
    """Represents a complete HTML collector."""

    @abstractmethod
    def collect_information(self, html: str) -> dict:
        """Collect information from the html."""

        raise NotImplementedError("You should implement this method.")

    @abstractmethod
    def collect_list_of_companies(self, html: str) -> list[dict]:
        """Collect list of companies from Fundamentus website."""

        raise NotImplementedError("You should implement this method.")

    @abstractmethod
    def collect_list_of_property_funds(self, html: str) -> list[dict]:
        """Collect list of companies from Fundamentus website."""

        raise NotImplementedError("You should implement this method.")
