#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: information_contract.py
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

"""Information Contract"""

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class InformationItem:
    """Class for keeping track of collected information."""

    title: str
    tooltip: str
    value: Decimal
