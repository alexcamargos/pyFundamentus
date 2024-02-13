#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: __init__.py
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
Python Fundamentus API

Instant access to key financial indicators of Brazilian stocks,
empowering investors with comprehensive market analysis.

"""

from fundamentus.main.fundamentus_pipeline import FundamentusPipeline as Pipeline


__all__ = ['Pipeline']
