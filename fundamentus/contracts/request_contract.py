#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: request_contract.py
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

"""Request Contract Module.

Defines a contract for HTTP requests within the Python Fundamentus API, encapsulating
the outcome of an HTTP request including its status, request details, and response content.

This structured approach facilitates the handling and analysis of HTTP request operations
across the API.
"""

from collections import namedtuple

# A contract for HTTP request results.
RequestContract = namedtuple('RequestContract',
                             ['status_code', 'request', 'response'])
