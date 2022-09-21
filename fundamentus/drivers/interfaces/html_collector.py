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

"""Html Collector Interface."""

from abc import ABC, abstractmethod
from typing import Dict, List


# pylint: disable=too-few-public-methods
class HtmlCollectorInterface(ABC):
    """Represents a complete HTML collector."""

    @abstractmethod
    def collect_all_information(self, html: str) -> Dict:
        """Collect all information from single stock from Fundamentus website."""

        raise NotImplementedError("You should implement this method.")

    @abstractmethod
    def collect_list_of_companies(self, html: str) -> List[Dict]:
        """Collect list of companies from Fundamentus website."""

        raise NotImplementedError("You should implement this method.")

    @abstractmethod
    def collect_list_of_property_funds(self, html: str) -> List[Dict]:
        """Collect list of companies from Fundamentus website."""

        raise NotImplementedError("You should implement this method.")
