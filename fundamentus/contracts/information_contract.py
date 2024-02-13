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

"""Information Contract Module.

Provides a data structure for storing and managing collected financial information
within the Python Fundamentus API, using a dataclass for enhanced readability and
efficiency.
"""

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class InformationItem:
    """Represents a single item of collected financial information.

    Attributes:
        title (str): The name or title of the information.
        tooltip (str): A brief description or tooltip associated with the information.
        value (Decimal): The numeric value of the information, stored as
                         a Decimal for precision.
    """

    title: str
    tooltip: str
    value: Decimal
