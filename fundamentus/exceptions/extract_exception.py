#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: extract_exception.py
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

"""Extract Exception."""


class ExtractException(Exception):
    """Exception class for extract stage."""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.mensagem = args[0]
        self.exception_type = 'ExtractException'
