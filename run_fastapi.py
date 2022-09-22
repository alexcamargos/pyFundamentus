#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: run_fastapi.py
#  Version: 0.0.7
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

"""Fundamentus Command line interface."""

from fastapi import FastAPI

from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.main.fundamentus_pipeline import \
    FundamentusPipeline as Fundamentus

app = FastAPI()


def get_stock_data(symbol: str) -> TransformContract:
    """Get the stock data.

    :param symbol: str: Stock symbol.
    :return: dict: Stock data.
    """

    url = 'https://www.fundamentus.com.br/detalhes.php'
    params = {'papel': symbol}

    main_pipeline = Fundamentus(url=url, params=params)
    response = main_pipeline.get_stock_information()

    return response


@app.get("/stock/{symbol}")
async def stock(symbol: str):

    return get_stock_data(symbol)[0]
