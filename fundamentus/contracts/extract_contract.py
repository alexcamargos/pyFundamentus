#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extractor_html_information.py
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

"""Extract Contract Module.

Defines the structure for storing raw information extracted from HTML sources along
with the date of extraction, streamlining the initial data gathering phase within
the Python Fundamentus API.
"""

from collections import namedtuple

# A contract for raw extracted information.
ExtractContract = namedtuple('ExtractContract',
                             ['raw_information', 'extraction_date'])
