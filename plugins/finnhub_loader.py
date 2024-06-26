import finnhub


def scrape_news():
    finnhub_client = finnhub.Client(api_key="cponuahr01qiv403hug0cponuahr01qiv403hugg")

    news = finnhub_client.general_news('general', min_id=0)

    return news
