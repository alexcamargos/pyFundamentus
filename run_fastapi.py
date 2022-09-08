from fastapi import FastAPI

from fundamentus.main.fundamentus_pipeline import \
    FundamentusPipeline as Fundamentus

app = FastAPI()


def get_stock_data(symbol: str) -> dict:
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
