#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: transform_contract.py
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

"""
Transform Contract Module for Python Fundamentus API.

This module defines the `TransformContract` data structure, which is used throughout
the Python Fundamentus API to encapsulate the result of transforming raw financial
data into a structured format. The contract ensures consistency and predictability
in data handling across different components of the API.
"""

from collections import namedtuple

# Define the TransformContract as a namedtuple.
# It encapsulates transformed financial information into a standardized structure.
TransformContract = namedtuple('TransformContract',
                               ['transformed_information'])
